#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the 
# GNU General Public License version 3 or any later version.
# If a copy of the GPLv3 was not distributed with this
# file, You may obtain one at https://www.gnu.org/licenses/gpl-3.0.html
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Subject to and governed by the GPLv3,
# Unless required by applicable law or agreed to
# in writing, software distributed under the License is available
# and/or distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND either express or implied.
#
# Subject to and governed by the GPLv3,
# Under no circumstance and/or theory of any kind
# is the author and/or authors and/or distributer and/or distributers
# to be considered and/or held liable at any time for any matter of any
# and all kinds, including direct or indirect, connected in any
# and all ways with this software.
#
# ONLY and ONLY from an ADMINISTRATOR account cmd:
# pip3 install --upgrade  pip-review
# pip3 list
# pip-review
# pip3 install --upgrade pip3
# pip3 install --upgrade setuptools
# pip3 install --upgrade numpy
# pip3 install --upgrade progressbar2
# pip3 install --upgrade PyYAML
# pip3 install --upgrade pymediainfo
# pip3 install --upgrade Pillow
#
#

import argparse
import ast
import codecs
import glob
import hashlib
import importlib
import logging
import os # 2020.05.20 import full os since we want mkdir; was #import os.path
import re
import shutil
import stat
import subprocess
import sys
import traceback
import urllib.parse
import urllib.request
from collections import defaultdict
from multiprocessing import cpu_count
from pathlib import Path
from urllib.parse import urlparse
import requests  # Run pip3 install requests
import json
# installed via pip3 --upgrade install  ...
import progressbar
import yaml

#
# work out what the GLOBAL variables should be set to, based on current working directory
bitness=64
bitnessStr = "x86_64"
projectRoot = Path(os.getcwd())
fullWorkDir = projectRoot.joinpath('workdir')
bitnessPath = fullWorkDir.joinpath(bitnessStr)
fullProductDir = bitnessPath.joinpath('_products')
fullDependencyDir = bitnessPath.joinpath('')	# to be compatible with deadsix27, rather than '_dependencies'

# define GLOBAL variables
G_DEBUG = False
G_bitness = bitness							# eg 64
G_bitnessStr = bitnessStr					# eg x86_64
G_projectRoot = projectRoot					# eg /home/u/Desktop/working
G_fullWorkDir = fullWorkDir					# eg /home/u/Desktop/working/workdir
G_bitnessPath = bitnessPath					# eg /home/u/Desktop/working/workdir/x86_64
G_fullProductDir = fullProductDir			# eg /home/u/Desktop/working/workdir/x86_64_products
G_fullDependencyDir = fullDependencyDir		# eg /home/u/Desktop/working/workdir/x86_64
#

##################################################
class Colors:  # ansi colors
	RESET = '\033[0m'
	BLACK = '\033[30m'
	RED = '\033[31m'
	GREEN = '\033[32m'
	YELLOW = '\033[33m'
	BLUE = '\033[34m'
	MAGENTA = '\033[35m'
	CYAN = '\033[36m'
	WHITE = '\033[37m'
	LIGHTBLACK_EX = '\033[90m'  # those seem to work on the major OS so meh.
	LIGHTRED_EX = '\033[91m'
	LIGHTGREEN_EX = '\033[92m'
	LIGHTYELLOW_EX = '\033[93m'
	LIGHTBLUE_EX = '\033[94m'
	LIGHTMAGENTA_EX = '\033[95m'
	LIGHTCYAN_EX = '\033[96m'
	LIGHTWHITE_EX = '\033[9m'
	#eg print(f"{Colors.RESET}Someting normal {Colors.LIGHTCYAN_EX}Something LIGHTCYAN_EX {Colors.RESET}Something back to normal")

#################################################
# This function is consumed within objects so the code does not have to repeated.
# Called like:	global_dump_object_variables(self,"this is a heading")
def global_dump_object_variables(obj, heading='VARIABLES DUMP:'):
	def name_of_object(xx):		# get the name of the object instantiated with this class https://stackoverflow.com/posts/16139159/revisions
		object_name = ''
		for objname, oid in globals().items():
			if oid is xx:
				object_name = objname
		return objname
	print(f"DEBUG: {heading}  Class='{type(obj).__name__}'  Object='{name_of_object(obj)}'")
	#members = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
	#print(members)
	max_var_len = 0
	for key,val in vars(obj).items():
		max_var_len = max(max_var_len,len(key))
	for key,val in vars(obj).items():
		k = key.ljust(max_var_len,' ')
		print(f"DEBUG: {k} = '{val}'")
	return

##################################################
# how to set the name of an instance: https://stackoverflow.com/posts/38599196/revisions
class settings:
	# https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables
	# Variables set here are Class Variables and are shared across all instances
	
	def __init__(self):
		self.DEBUG = G_DEBUG										# True or False
		self.bitness = G_bitness									# eg 64
		self.bitnessStr = G_bitnessStr								# eg x86_64
		self.projectRoot = G_projectRoot							# eg /home/u/Desktop/working
		self.fullWorkDir = G_fullWorkDir							# eg /home/u/Desktop/working/workdir
		self.bitnessPath = G_bitnessPath							# eg /home/u/Desktop/working/workdir/x86_64
		self.fullProductDir = G_fullProductDir						# eg /home/u/Desktop/working/workdir/x86_64_products
		self.fullDependencyDir = G_fullDependencyDir				# eg /home/u/Desktop/working/workdir/x86_64"
		return

	def dump_vars(self, heading='VARIABLES DUMP:'):
		global_dump_object_variables(self, heading)

##################################################
class dot_py_object:					# a single .py - name,  and json values in a dictionary
	# objDict = dict([('key1', val1),('key2',val2)])	# dict() constructor builds dictionaries directly from sequences of key-value pairs:
	# list(objDict)					# returns a list of all the keys used in the dictionary, in insertion order
	# list(sorted(objDict))			# returns a list of all the keys used in the dictionary, sorted
	# 'a_key' in objDict			# check whether a single key is in the dictionary
	# 'a_key' not in objDict		# check whether a single key is not in the dictionary
	# for k, v in objDict.items():	# key and corresponding value can be retrieved at the same time using the items() method.

	# https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables
	# Variables set here are Class Variables and are shared across all instances
	
	def __init__(self, Name='', Val={}):
		# Variables set here are Instance Variables and are unique to the instantiated Instance
		self.Name = ''
		#self.Val = OrderedDict()				# we can have the dictionary ordered if we want to
		self.Val = {}							# a dictionary of key/values pairs, in this case the filename/json-values-inside-the-.py
		print(f"DEBUG: dot_py_object __init__ Created dot_py_object")
		return

	def dump_vars(self, heading='VARIABLES DUMP:'):
		global_dump_object_variables(self, heading)

	def set_data_py(self, Name='', Val={}):
		# Variables set here are Instance Variables and are unique to the instantiated Instance
		self.Name = Name
		#self.Val = OrderedDict()				# we can have the dictionary ordered if we want to
		self.Val = Val							# a dictionary of key/values pairs, in this case the filename/json-values-inside-the-.py
		print(f"DEBUG: dot_py_object set_data_py added Name='{self.Name}'")
		for key2, val2 in self.Val.items():
			print(f"\t{key2}='{val2}'")
		return

	def dump_vars(self, heading='OBJECT VARIABLES DUMP'):
		print(f"DEBUG: {heading}")
		#members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
		#print(members)
		max_var_len = 0
		for key,val in vars(self).items():
			max_var_len = max(max_var_len,len(key))
		for key,val in vars(self).items():
			k = key.ljust(max_var_len,' ')
			print(f"DEBUG: {k} = '{val}'")

##################################################
class dot_py_object_dict:			# a dictionary of build objects
	# objDict = dict([('key1', val1),('key2',val2)])	# dict() constructor builds dictionaries directly from sequences of key-value pairs:
	# list(objDict)					# returns a list of all the keys used in the dictionary, in insertion order
	# list(sorted(objDict))			# returns a list of all the keys used in the dictionary, sorted
	# 'a_key' in objDict			# check whether a single key is in the dictionary
	# 'a_key' not in objDict		# check whether a single key is not in the dictionary
	# for k, v in objDict.items():	# key and corresponding value can be retrieved at the same time using the items() method.

	# https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables
	# Variables set here are Class Variables and are shared across all instances

	def __init__(self):
		# Variables set here are Instance Variables and are unique to the instantiated Instance
		print(f"DEBUG: dot_py_object_dict __init__")
		#self.BO = OrderedDict()				# we can have the dictionary ordered if we want to
		self.BO = {}
		return

	def dump_vars(self, heading='VARIABLES DUMP:'):
		global_dump_object_variables(self, heading)

	def add_dot_py_obj(self, objBO):				# assumes objBO is of class dot_py_object
		#https://docs.python.org/3/whatsnew/3.9.html#dictionary-merge-update-operators
		#If a key appears in both operands, the last-seen value (i.e. that from the right-hand operand) wins:
		# Dict Union is not commutative
		#self.BO = self.BO | { objBO.Name : objBO.Val }
		self.BO |= { objBO.Name : objBO.Val }
		print(f"DEBUG: add_dot_py_obj: Added/updated dot_py_object_dict: key='{objBO.Name}' val='{objBO.Val}'")
		print(f"DEBUG: add_dot_py_obj: DICTIONARY DUMP:")
		for key, val in self.BO.items():
			#print(f"DEBUG: add_dot_py_obj: key='{key}' val='{val}'")
			print(f"DEBUG: add_dot_py_obj: Name='{key}'")
			for key2, val2 in val.items():
				print(f"\t{key2}='{val2}'")
		return

	def get_dot_py(self, package_name):
		print(f"DEBUG: get_dot_py")
		tmp = dot_py_object()					# create a new empty instance of a dot_py_object
		if package_name in self.BO:				# check whether a single key is in the dictionary
			tmp.Name = package_name				# yes, insert the package name into the tmp object
			tmp.Val = self.BO[the_key]			# yes, insert the doct of jason info into the tmp object
		return tmp								# return the new dot_py_object 


##################################################
class MissingDependency(Exception):
	__module__ = 'exceptions'

	def __init__(self, message):
		self.message = message

	def dump_vars(self, heading='VARIABLES DUMP:'):
		global_dump_object_variables(self, heading)

##################################################
class MyLogFormatter(logging.Formatter):
	def __init__(self, l, ld):
		MyLogFormatter.log_format = l
		MyLogFormatter.log_date_format = ld
		MyLogFormatter.inf_fmt = Colors.LIGHTCYAN_EX + MyLogFormatter.log_format + Colors.RESET
		MyLogFormatter.err_fmt = Colors.LIGHTRED_EX + MyLogFormatter.log_format + Colors.RESET
		MyLogFormatter.dbg_fmt = Colors.LIGHTYELLOW_EX + MyLogFormatter.log_format + Colors.RESET
		MyLogFormatter.war_fmt = Colors.YELLOW + MyLogFormatter.log_format + Colors.RESET
		super().__init__(fmt="%(levelno)d: %(msg)s", datefmt=MyLogFormatter.log_date_format, style='%')

	def dump_vars(self, heading='VARIABLES DUMP:'):
		global_dump_object_variables(self, heading)

	def format(self, record):
		if not hasattr(record, "type"):
			record.type = ""
		else:
			record.type = "[" + record.type.upper() + "]"

		format_orig = self._style._fmt
		if record.levelno == logging.DEBUG:
			self._style._fmt = MyLogFormatter.dbg_fmt
		elif record.levelno == logging.INFO:
			self._style._fmt = MyLogFormatter.inf_fmt
		elif record.levelno == logging.ERROR:
			self._style._fmt = MyLogFormatter.err_fmt
		elif record.levelno == logging.WARNING:
			self._style._fmt = MyLogFormatter.war_fmt
		result = logging.Formatter.format(self, record)
		self._style._fmt = format_orig
		return result

##################################################
##################################################
##################################################

# Create some empty instances we can play with
print(f" ")
objProd =  dot_py_object()	# objProd.Name objProd.Val
objDep  =  dot_py_object()	# objDep.Name  objDep.Val
objVar  =  dot_py_object()	# objVar.Name  objVar.Val

# Create some empty instances of dictionaries of we can play with
print(f" ")
objProdsDict = dot_py_object_dict()
objDepsDict  = dot_py_object_dict()
objVarsDict  = dot_py_object_dict()

print(f" ")
print(f"--- ADD TYPE 1")
objProd.Name = "abc_product_name"
objProd.Val  = { 'repo_type' : 'git_abc', 'branch' : 'branch_abc', 'is_dep_inheriter' : False }
objProdsDict.add_dot_py_obj(objProd)

print(f" ")
print(f"--- ADD TYPE 2")
objProd.set_data_py(Name= "def_product_name", Val={ 'repo_type' : 'git_def', 'branch' : 'branch_def', 'is_dep_inheriter' : True })
objProdsDict.add_dot_py_obj(objProd)

print(f" ")
print(f"about to instantiate settings()")
global_settings = settings()
global_settings.dump_vars("VARIABLES DUMP:")


