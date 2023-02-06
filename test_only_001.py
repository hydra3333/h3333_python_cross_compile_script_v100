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

# Global Variables and Functions and Objects
global logging_handler 	# the handler for the logger, only used for initialization
global logger 			# the logger object

###################################################################################################
class settings:
	# https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables
	# Variables set here are Class Variables and are shared across all instances
	
	def errorExit(self, msg): # logger is not up and running yer, so use our own self.errorExit instead
		#logger.error(msg)
		print("Settings Error: " + msg)
		sys.exit(1)
	
	def __init__(self):

		# NOTE:	here we fully flesh out all variables
		#		nothing is left with !CMDxxxCMD! or !VARxxxVAR! type stuff in it
		#		so, we do not rely on functions like replaceVariables or replaceVariables

		self.debugMode = False											# True or False
		if self.debugMode:
			self.initial_logging_mode = logging.DEBUG					# at what level to start logging initially. logging.INFO logging.DEBUG
		else:
			self.initial_logging_mode = logging.INFO					# at what level to start logging initially. logging.INFO logging.DEBUG
		self.current_logging_mode = self.initial_logging_mode			# to keep track of the prevailing logging mode, if changed

		# mostly fixed variables first, calculated variables later
		
		self.bitness = 64												# bits to build ffmpeg etc
		self.toolchain_bitness = self.bitness							# bits to build the toolchain
		self.targetBitness = self.bitness
		self.cpu_count = cpu_count()									# number of CPUs on this machine
		self.projectRoot = Path(os.getcwd())							# root folder for this script eg /home/u/Desktop/working
		self.originalPATH = os.environ["PATH"] 							# the original environment path, used for resets

		self.packages_subfolder = 'packages'							# 'packages' is the subfolder where the .py files reside
		self.patches_subfolder = 'patches'								# 'patches' is the subfolder where the patch files reside
		
		self.additionalheaders_subfolder = 'additional_headers'		# 'additional_headers' is where additional headers reside
		self.sources_subfolder = 'sources'								# 'sources' is where some sources reside
		self.tools_subfolder = 'tools'									# 'tools' is where some tools reside
		
		self.workdir_subfolder ='workdir'								# 'workdir'  is the subfolder where actual build stuff happens
		self.bitnessStr = "x86_64"										# eg x86_64 underneath workdir_subfolder
		self.bitnessStr2 = "x86_64"										# just for vpx... underneath workdir_subfolder
		self.bitnessStr3 = "mingw64"									# just for openssl... underneath workdir_subfolder
		self.targetOSStr = "mingw64"									# 2019.12.13 just for "--target-os=" 
		self.bitnessStrWin = "win64"									# eg 'win64'

		self.targetHostStr = F"{self.bitnessStr}-w64-mingw32"  			# e.g x86_64-w64-mingw32

		self.original_cflags = '-O3'
		self.original_stack_protector = '-fstack-protector-all'
		self.original_fortify_source = '-D_FORTIFY_SOURCE=2'
		
		self.toolchain_mingw_subfolder = 'toolchain'					# for output, eg 'toolchain' underneath self.workdir_subfolder
		self.toolchain_mingw_toolchain_script_subfolder = "mingw_toolchain_script"
		self.toolchain_mingw_toolchain_script_name = 'mingw_toolchain_script_v100_002_like_zeranoe.py'
		self.toolchain_mingw_commit = None				# specify a commit, or None which leaves that up to the toolchain builder
		self.toolchain_mingw_debug_build = False
		self.toolchain_mingw_custom_cflags = None
		
		self.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
		self.log_format = '[%(asctime)s][%(levelname)s]%(type)s %(message)s'
		self.log_date_format = '%H:%M:%S'

		# calculated variables next

		self.mingw_toolchain_script_folder = self.projectRoot.joinpath(self.toolchain_mingw_toolchain_script_subfolder)
		self.mingw_toolchain_script_path = self.mingw_toolchain_script_folder.joinpath(self.toolchain_mingw_toolchain_script_name)
	
		self.packagesFolder = self.projectRoot.joinpath(self.packages_subfolder)	# for input, eg /home/u/Desktop/working/packages
		self.prodFolder     = self.packagesFolder.joinpath("products")					# for input, eg /home/u/Desktop/working/packages/products
		self.depsFolder     = self.packagesFolder.joinpath("dependencies")				# for input, eg /home/u/Desktop/working/packages/dependencies
		self.varsPath       = self.packagesFolder.joinpath("variables.py")				# for input, eg /home/u/Desktop/working/packages/variables.py
		self.patchesFolder	= self.projectRoot.joinpath(self.patches_subfolder)			# for input, eg /home/u/Desktop/working/packages
		self.additionalheadersFolder	= self.projectRoot.joinpath(self.additionalheaders_subfolder)			# for input, eg /home/u/Desktop/working/packages
		self.sourcesFolder	= self.projectRoot.joinpath(self.sources_subfolder)			# for input, eg /home/u/Desktop/working/packages
		self.toolsFolder	= self.projectRoot.joinpath(self.tools_subfolder)			# for input, eg /home/u/Desktop/working/packages

		self.fullWorkDir    = self.projectRoot.joinpath(self.workdir_subfolder)			# for output, eg /home/u/Desktop/working/workdir

		self.bitnessPath = self.fullWorkDir.joinpath(self.bitnessStr)	# for output, eg /home/u/Desktop/working/workdir/x86_64
		self.fullProductDir = self.bitnessPath.joinpath('_products')	# for output, eg /home/u/Desktop/working/workdir/x86_64_products
		self.fullDependencyDir = self.bitnessPath.joinpath('')			# to be compatible with deadsix27, rather than use a new 'x86_64_dependencies'

		self.toolchain_output_path = self.fullWorkDir.joinpath(self.bitnessStrWin + "_output")

		#if not os.path.isdir(self.packagesFolder):	# for input, eg /home/u/Desktop/working/packages
		#	self.errorExit(f"Packages folder '{self.packagesFolder}' does not exist.")
		#if not os.path.isdir(self.prodFolder):	# for input, eg /home/u/Desktop/working/packages/products
		#	self.errorExit(f"Packages Products folder '{self.prodFolder}' does not exist.")
		#if not os.path.isdir(delf.depsFolder):	# for input, eg /home/u/Desktop/working/packages/dependencies
		#	self.errorExit(f"Packages Dependencies folder '{self.depsFolder}' does not exist.")
		#if not os.path.isfile(self.varsPath):	# for input, eg /home/u/Desktop/working/packages/variables.py
		#	self.errorExit(f"Variables file '{self.varsPath}' does not exist." )
		#if not os.path.isdir(self.patchesFolder):	# for input, eg /home/u/Desktop/working/packages
		#	self.errorExit(f"Patches folder '{self.patchesFolder}' does not exist." )
		#if not os.path.isdir(self.additionalheadersFolder):	# for input, eg /home/u/Desktop/working/additional_headers
		#	self.errorExit(f"additional_headers folder '{self.additionalheadersFolder}' does not exist." )
		#if not os.path.isdir(self.sourcesFolder):	# for input, eg /home/u/Desktop/working/sources
		#	self.errorExit(f"Patches folder '{self.sourcesFolder}' does not exist." )
		#if not os.path.isdir(self.toolsFolder):	# for input, eg /home/u/Desktop/working/tools
		#	self.errorExit(f"Patches folder '{self.toolsFolder}' does not exist." )
		## ??? hmm, this next subfolder may need to be created during setup for building, not here at settings
		#if not os.path.isdir(self.fullWorkDir):	# for output, eg /home/u/Desktop/working/workdir
		#	self.errorExit(f"Working folder '{self.fullWorkDir}' does not exist.")
		## ??? hmm, this next subfolder may need to be created during setup for building, not here at settings
		#if not os.path.isdir(self.bitnessPath):	# for output, eg /home/u/Desktop/working/workdir/x86_64
		#	self.errorExit(f"Working folder '{self.bitnessPath}' does not exist.")
		## ??? hmm, this next subfolder may need to be created during setup for building, not here at settings
		#if not os.path.isdir(self.fullProductDir):	# for output, eg /home/u/Desktop/working/workdir/x86_64_products
		#	self.errorExit(f"Working folder '{self.fullProductDir}' does not exist.")
		## ??? hmm, this next subfolder may need to be created during setup for building, not here at settings
		#if not os.path.isdir(self.fullDependencyDir):	# to be compatible with deadsix27, rather than use a new 'x86_64_dependencies'
		#	self.errorExit(f"Working folder '{self.fullDependencyDir}' does not exist.")
		#if not os.path.isdir(self.mingw_toolchain_script_folder):	# the subfolder where the toolchain build script resides
		#	self.errorExit(f"mingw build script folder '{self.mingw_toolchain_script_folder}' does not exist.")
		#if not os.path.isfile(self.mingw_toolchain_script_path):	# the full path to the toolchain build script
		#	self.errorExit(f"mingw build script file '{self.mingw_toolchain_script_path}' does not exist." )
		## ??? hmm, this subfolder may need to be created during setup for building, not here at settings
		#if not os.path.isdir(self.toolchain_output_path):			# the subfolder where the toolchain building happens
		#	self.errorExit(f"mingw build folder '{self.toolchain_output_path}' does not exist.")

		return

	def dump_vars(self, heading='VARIABLES DUMP:'):
		global_dump_object_variables(self, heading)

##################################################################################################
# This function is consumed within objects so the code does not have to repeated.
# Called in a class like:	global_dump_object_variables(self,"this is a heading")
def global_dump_object_variables(obj, heading='VARIABLES DUMP:'):
	def name_of_object(xx):		# get the name of the object instantiated with a class https://stackoverflow.com/posts/16139159/revisions
		object_name = ''
		for objname, oid in globals().items():
			if oid is xx:
				object_name = objname
		return object_name
	object_name = name_of_object(obj)
	if object_name == '':
		object_name = 'Undetermined'
	print(f"DEBUG: {heading}  Class='{type(obj).__name__}'  ObjectName='{name_of_object(obj)}'")
	#members = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
	#print(members)
	max_var_len = 0
	for key,val in vars(obj).items():
		max_var_len = max(max_var_len,len(key))
	for key,val in vars(obj).items():
		k = key.ljust(max_var_len,' ')
		print(f"DEBUG: {k} = '{val}'")
	return

###################################################################################################
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

###################################################################################################
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

###################################################################################################
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


###################################################################################################
class MissingDependency(Exception):
	__module__ = 'exceptions'

	def __init__(self, message):
		self.message = message

	def dump_vars(self, heading='VARIABLES DUMP:'):
		global_dump_object_variables(self, heading)

###################################################################################################

class MyLogFormatter(logging.Formatter):
	def __init__(self, l, ld):
		MyLogFormatter.log_format = l
		MyLogFormatter.log_date_format = ld
		MyLogFormatter.inf_fmt = Colors.RESET + Colors.LIGHTCYAN_EX + MyLogFormatter.log_format + Colors.RESET
		MyLogFormatter.err_fmt = Colors.RESET + Colors.LIGHTRED_EX + MyLogFormatter.log_format + Colors.RESET
		MyLogFormatter.dbg_fmt = Colors.RESET + Colors.LIGHTYELLOW_EX + MyLogFormatter.log_format + Colors.RESET
		MyLogFormatter.war_fmt = Colors.RESET + Colors.YELLOW + MyLogFormatter.log_format + Colors.RESET
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

###################################################################################################
class epiFormatter(argparse.RawDescriptionHelpFormatter):
	w = shutil.get_terminal_size((120, 10))[0]
	def __init__(self, max_help_position=w, width=w, *args, **kwargs):
		kwargs['max_help_position'] = max_help_position
		kwargs['width'] = width
		super(epiFormatter, self).__init__(*args, **kwargs)
	def _split_lines(self, text, width):
		return text.splitlines()


###################################################################################################
def errorExit(msg):
	logger.error(msg)
	sys.exit(1)

###################################################################################################
###################################################################################################
###################################################################################################

# Create some empty instances we can play with
#print(f" ")
#objProd =  dot_py_object()	# objProd.Name objProd.Val
#objDep  =  dot_py_object()	# objDep.Name  objDep.Val
#objVar  =  dot_py_object()	# objVar.Name  objVar.Val
# Create some empty instances of dictionaries of we can play with
#print(f" ")
#objProdsDict = dot_py_object_dict()
#objDepsDict  = dot_py_object_dict()
#objVarsDict  = dot_py_object_dict()
#print(f" ")
#print(f"--- ADD TYPE 1")
#objProd.Name = "abc_product_name"
#objProd.Val  = { 'repo_type' : 'git_abc', 'branch' : 'branch_abc', 'is_dep_inheriter' : False }
#objProdsDict.add_dot_py_obj(objProd)
#print(f" ")
#print(f"--- ADD TYPE 2")
#objProd.set_data_py(Name= "def_product_name", Val={ 'repo_type' : 'git_def', 'branch' : 'branch_def', 'is_dep_inheriter' : True })
#objProdsDict.add_dot_py_obj(objProd)
#print(f" ")
#print(f"about to instantiate settings()")
#global_settings = settings()
#global_settings.dump_vars("VARIABLES DUMP:")

if __name__ == "__main__":

	# Initialize python3 system stuff
	# initialize settings
	# initialize logging (with default loglevel)
	# process CMDLINE arguments
	# prepare ... 
	#	reset logging level after cmdline arguments, create folder trees
	#	set environment variables
	#	init and load products
	#	init and load dependencies
	#	init and load variables (the .py)
	# check and build the toolchain
	# execute build etc


	# initialize system stuff
	PY_REQUIRE = (3, 8)
	if sys.version_info < PY_REQUIRE:
		sys.exit("You need at least Python %s.%s or later to run this script.\n" % PY_REQUIRE)
	sys.dont_write_bytecode = True  # Avoid __pycache__ folder, never liked that solution

	# initial settings, they can be overridden later by commandline options
	global_settings = settings()
	if global_settings.debugMode:
		global_settings.dump_vars("SETTINGS in debugMode")

	# TEMPORARY ... REMOVE THIS LATER ...
	global_settings.dump_vars("SETTINGS in debugMode")
	
	# initialize Logging
	global logging_handler 	# the handler for the logger, only used for initialization
	global logger 			# the logger object
	logging_handler = logging.StreamHandler(sys.stdout)		# a handler for the logger
	fmt = MyLogFormatter(global_settings.log_format, global_settings.log_date_format)
	logging_handler.setFormatter(fmt)						# set the format into the handler for the logger
	logger = logging.getLogger(__name__)					# get an instance of the logger ?
	logger.addHandler(logging_handler)						# add our handler into the instance
	logger.setLevel(global_settings.initial_logging_mode)	# set trhe level in our instance
	logger.debug(f'__main__: logger.setLevel is {global_settings.initial_logging_mode} ... (logging.INFO={logging.INFO} logging.DEBUG={logging.DEBUG})')


	# process CMDLINE arguments
	
	
	#prepare ... 
	#
	# set environment variables
	#os.environ["PATH"] = "{0}:{1}".format(self.mingwBinpath, self.originalPATH)
	#os.environ["PKG_CONFIG_PATH"] = self.pkgConfigPath
	#os.environ["PKG_CONFIG_LIBDIR"] = ""
	#os.environ["COLOR"] = "ON"  # Force coloring on (for CMake primarily)
	#os.environ["CLICOLOR_FORCE"] = "ON"  # Force coloring on (for CMake primarily)



	#_epilog = 'Copyright (C) 2023-2024 hydra3333\n\n This Source Code Form is subject to the terms of the GNU General Public License version 3 or any later version. If a copy of the GPLv3 was not distributed with this file, You may obtain one at https://www.gnu.org/licenses/gpl-3.0.html'
	#parser = argparse.ArgumentParser(formatter_class=epiFormatter, epilog=_epilog)
