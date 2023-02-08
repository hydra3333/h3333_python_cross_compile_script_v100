#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ######################################################################################################
# Copyright (C) 2018-2024 DeadSix27 (https://github.com/DeadSix27/python_cross_compile_script)
# with additions by Hydra3333 (https://github.com/hydra3333/h3333_python_cross_compile_script_v100)
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ######################################################################################################
# Copyright (C) 2023-2024 hydra3333(https://github.com/hydra3333/h3333_python_cross_compile_script_v100)
# Based on work by Deadsix27.
#
# The following individual clauses only apply where they are compatible with
# the Mozilla Public License v. 2.0 (MPLv2) and they also limit to zero
# and/or reduce toward zero any and/or all liabiility arising in any way
# when applying the MPLv2 and the clauses above.
#
# Subject to and governed by the Mozilla Public License v. 2.0 (MPLv2),
# unless required by applicable law or agreed to in writing, software
# distributed under the License is available and/or distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND either
# express or implied.
# The meaning of this clause is to limit, under any theory, to zero
# and/or reduce toward zero any and/or all liabiility arising in any way 
# when applying the MPLv2.
# If a copy of the MPLv2 was not distributed with this file,
# you can obtain one at https://mozilla.org/MPL/2.0/
#
# Subject to and governed by the  Mozilla Public License v. 2.0 (MPLv2),
# under no circumstance and/or theory of any kind is the author and/or
# authors and/or distributer and/or distributers to be considered and/or
# held liable at any time for any matter of any and all kinds, including
# direct and/or indirect, connected in any and/or all ways with this software.
# The meaning of this clause is to limit, under any theory, to zero
# and/or reduce toward zero any and/or all liabiility arising in any way 
# when applying the MPLv2.
# If a copy of the MPLv2 was not distributed with this file,
# you can obtain one at https://mozilla.org/MPL/2.0/
#
# Subject to and governed by the  Mozilla Public License v. 2.0 (MPLv2),
# the GNU GENERAL PUBLIC LICENSE Version 3 or any later version (GPLv3) also
# applies only wherever it is compatible with the MPLv2 as is also compatible with
# clauses above and does not increase liability over MPLv2 in any way under any theory.
# If a copy of the GPLv3 was not distributed with this file, you can obtain one via 
# https://www.gnu.org/licenses/licenses.html or https://www.gnu.org/licenses/gpl-3.0.html
#
# ######################################################################################################

# Setup Notes:
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
# Global Variables and Functions and Objects
# Strictly, global declaration is not needed here (only inside functions)
# however it shows these can be found elsewhere where read&write globals are needed.

global objSETTINGS		# the SETTINGS object used everywhere
global logging_handler 	# the handler for the logger, only used for initialization
global logger 			# the logger object used everywhere
global objArgParser		# the ArgParser which may be used everywhere
global objParser		# the parser creat6ed by ArgParser which may be used everywhere
global dictProducts		# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for PRODUCTS only, of class dot_py_object_dict
global dictDependencies	# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for DEPENDENCIES only, of class dot_py_object_dict
global objVariables		# an object of the variables, of class dot_py_object
global objPrettyPrint	# facilitates formatting and printing of text and dicts etc
global TERMINAL_WIDTH	# for Console setup and PrettyPrint setup
TERMINAL_WIDTH = 132	# for Console setup and PrettyPrint setup

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
from collections import defaultdict, OrderedDict
from multiprocessing import cpu_count
from pathlib import Path
from urllib.parse import urlparse
import requests  # Run pip3 install requests
import json
# installed via pip3 --upgrade install  ...
import progressbar
import yaml
import pprint

###################################################################################################
class settings:
	# https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables
	# Variables set at the top here are Class Variables and apparently shared across all instances
	global objSETTINGS		# the SETTINGS object used everywhere
	global logging_handler 	# the handler for the logger, only used for initialization
	global logger 			# the logger object used everywhere
	global objArgParser		# the ArgParser which may be used everywhere
	global objParser		# the parser creat6ed by ArgParser which may be used everywhere
	global dictProducts		# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for PRODUCTS only, of class dot_py_object_dict
	global dictDependencies	# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for DEPENDENCIES only, of class dot_py_object_dict
	global objVariables		# an object of the variables, of class dot_py_object
	global objPrettyPrint	# facilitates formatting and printing of text and dicts etc
	global TERMINAL_WIDTH	# for Console setup and PrettyPrint setup

	def errorExit(self, msg): # logger is not up and running yer, so use our own self.errorExit instead
		#logger.error(msg)
		print("Settings Error: " + msg)
		sys.exit(1)

	def dump_vars(self, heading='### SETTINGS INTERNAL VARIABLES DUMP:'):
		global_dump_object_variables(self, heading)
	
	def __init__(self):
		# NOTE:	here we fully flesh out all variables
		#		nothing is left with !CMDxxxCMD! or !VARxxxVAR! type stuff in it
		#		so, we do not rely on functions like replaceVariables or replaceVariables

		# WORKING and STATUS stuff first
		self.debugMode = True											# True or False
		# be cautious, set the loglevel based on debugMode, but initDebugMode still needs to be called after the logger is initialized outside of this class
		if self.debugMode:
			self.initial_logging_mode = logging.DEBUG					# at what level to start logging initially. logging.INFO logging.DEBUG
		else:
			self.initial_logging_mode = logging.INFO					# at what level to start logging initially. logging.INFO logging.DEBUG
		self.current_logging_mode = self.initial_logging_mode			# to keep track of the prevailing logging mode, if changed
		self.lastError = None

		# mainly fixed variables first, do calculated variables later
		
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
		
		#self.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'		# old
		self.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'		# LTS as at 2023.02.07
		#self.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'	# as at 2023.02.07
		
		self.log_format = '[%(asctime)s][%(levelname)s]%(type)s %(message)s'
		self.log_date_format = '%H:%M:%S'

		# mainly calculated variables next

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
def errorExit(msg):
	logger.error(msg)
	sys.exit(1)

###################################################################################################
# This function is consumed within objects so the code does not need to repeated in them.
# Called in a class like:	global_dump_object_variables(self,"this is a heading")
def global_dump_object_variables(obj, heading='VARIABLES DUMP:'):
	global objSETTINGS		# the SETTINGS object used everywhere
	global logging_handler 	# the handler for the logger, only used for initialization
	global logger 			# the logger object used everywhere
	global objArgParser		# the ArgParser which may be used everywhere
	global objParser		# the parser creat6ed by ArgParser which may be used everywhere
	global dictProducts		# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for PRODUCTS only, of class dot_py_object_dict
	global dictDependencies	# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for DEPENDENCIES only, of class dot_py_object_dict
	global objVariables		# an object of the variables, of class dot_py_object
	global objPrettyPrint	# facilitates formatting and printing of text and dicts etc
	global TERMINAL_WIDTH	# for Console setup and PrettyPrint setup

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
def isPathDisabled(path):
	for part in path.parts:
		if part.lower().startswith("_disabled"):
			return True
	return False

###################################################################################################
def boolKey(d, k):
	if k in d:
		if d[k]:
			return True
	return False

###################################################################################################
class dot_py_object:					# a single .py - name,  and json values in a dictionary
	global objSETTINGS		# the SETTINGS object used everywhere
	global logging_handler 	# the handler for the logger, only used for initialization
	global logger 			# the logger object used everywhere
	global objArgParser		# the ArgParser which may be used everywhere
	global objParser		# the parser creat6ed by ArgParser which may be used everywhere
	global dictProducts		# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for PRODUCTS only, of class dot_py_object_dict
	global dictDependencies	# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for DEPENDENCIES only, of class dot_py_object_dict
	global objVariables		# an object of the variables, of class dot_py_object
	global objPrettyPrint	# facilitates formatting and printing of text and dicts etc
	global TERMINAL_WIDTH	# for Console setup and PrettyPrint setup

	# objDict = dict([('key1', val1),('key2',val2)])	# dict() constructor builds dictionaries directly from sequences of key-value pairs:
	# list(objDict)					# returns a list of all the keys used in the dictionary, in insertion order
	# list(sorted(objDict))			# returns a list of all the keys used in the dictionary, sorted
	# 'a_key' in objDict			# check whether a single key is in the dictionary
	# 'a_key' not in objDict		# check whether a single key is not in the dictionary
	# for k, v in objDict.items():	# key and corresponding value can be retrieved at the same time using the items() method.

	# https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables
	# Variables set here are Class Variables and are shared across all instances

	def errorExit(self, msg):
		logger.error(f"dot_py_object({self.name}): Error: " + msg)
		print(f"dot_py_object({self.name}): Error: " + msg)
		sys.exit(1)
		
	def __init__(self, name=None, Val={}):
		# Variables set here are Instance Variables and are unique to the instantiated Instance
		self.name = name
		self.Val = {}							# a dictionary of key/values pairs, in this case the filename/json-values-inside-the-.py
		#self.Val = OrderedDict()				# we can have the dictionary ordered if we want to, but NO since we want .Val content to print in the order originally created
		#logger.debug(f"DEBUG: dot_py_object __init__ object instatiation")
		return

	def __del__(self):
		#logger.debug(f"DEBUG: dot_py_object __del__ to delete this object")
		return

	def dump_vars(self, heading='VARIABLES DUMP:'):
		global_dump_object_variables(self, heading)
		return
	#def dump_vars(self, heading='OBJECT VARIABLES DUMP'):
	#	print(f"DEBUG: {heading}")
	#	#members = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
	#	#logger.debug(members)
	#	max_var_len = 0
	#	for key,val in vars(self).items():
	#		max_var_len = max(max_var_len,len(key))
	#	for key,val in vars(self).items():
	#		k = key.ljust(max_var_len,' ')
	#		print(f"DEBUG: {k} = '{val}'")
	#	return

	def set_data_py(self, name='', Val={}):
		# Variables set here are Instance Variables and are unique to the instantiated Instance
		self.name = name
		self.Val = Val							# self.Val is a dictionary of key/values pairs, in this case the filename/json-values-inside-the-.py
		#logger.debug(f"DEBUG: dot_py_object set_data_py added name='{self.name}'")
		#for key2, val2 in self.Val.items():
		#	logger.debug(f"\t{key2}='{val2}'")
		return

	def load_py_file(self, file='', heading=''):
		# Load the variables.py file from the specified folder tree
		if not os.path.isfile(file):
			self.errorExit(f"dot_py_object({self.name}): load_py_file: variables File '{file}' does not exist.")
		with open(file, "r", encoding="utf-8") as f:
			p = Path(file)
			packageName = p.stem.lower()
			try:
				objJSON = ast.literal_eval(f.read())
				if not isinstance(objJSON, dict):
					self.errorExit(f"dot_py_object({self.name}): {heading} variables File '{packageName}' is misformatted")
				else:
					if "_info" not in objJSON:
						logger.warning(f"load_py_file: dot_py_object({self.name}): {heading} variables File '{packageName}.py' is missing '_info' tag")
					if boolKey(objJSON, "is_dep_inheriter"):
						logger.warning(f"load_py_file: dot_py_object({self.name}): {heading} variables File {packageName} contains 'is_dep_inheriter'")
					if boolKey(objJSON, "_disabled"):
						logger.debug(f"load_py_file: dot_py_object({self.name}): Ignored {heading} variables File {packageName} due to '_disabled'")
					else:
						self.set_data_py(name=self.name, Val=objJSON)
						logger.debug(f"load_py_file: dot_py_object({self.name}): {heading} variables File '{packageName}.py' loaded")
			except SyntaxError:
				self.errorExit(f"load_py_file: dot_py_object({self.name}): Loading {heading} variables File '{packageName}' failed:\n\n{traceback.format_exc()}")
		logger.info(f"Loaded {heading} variables file into dictionary {self.name}")
		return
		
	def list_print(self, heading=''):
		print(f"")
		print(f"LIST: {heading}:\n")
		for key, val in self.Val.items():
			pkey = key.ljust(32,' ')
			print(f" {Colors.GREEN}{pkey}{Colors.RESET} ... '{val}'")
		return

###################################################################################################
class dot_py_object_dict:			# a dictionary of build objects
	global objSETTINGS		# the SETTINGS object used everywhere
	global logging_handler 	# the handler for the logger, only used for initialization
	global logger 			# the logger object used everywhere
	global objArgParser		# the ArgParser which may be used everywhere
	global objParser		# the parser creat6ed by ArgParser which may be used everywhere
	global dictProducts		# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for PRODUCTS only, of class dot_py_object_dict
	global dictDependencies	# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for DEPENDENCIES only, of class dot_py_object_dict
	global objVariables		# an object of the variables, of class dot_py_object
	global objPrettyPrint	# facilitates formatting and printing of text and dicts etc
	global TERMINAL_WIDTH	# for Console setup and PrettyPrint setup

	# objDict = dict([('key1', val1),('key2',val2)])	# dict() constructor builds dictionaries directly from sequences of key-value pairs:
	# list(objDict)					# returns a list of all the keys used in the dictionary, in insertion order
	# list(sorted(objDict))			# returns a list of all the keys used in the dictionary, sorted
	# 'a_key' in objDict			# check whether a single key is in the dictionary
	# 'a_key' not in objDict		# check whether a single key is not in the dictionary
	# for k, v in objDict.items():	# key and corresponding value can be retrieved at the same time using the items() method.

	# https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables
	# Variables set here are Class Variables and are shared across all instances

	def errorExit(self, msg):
		logger.error(f"dot_py_object_dict({self.name}): Error: " + msg)
		print(f"dot_py_object_dict({self.name}): Error: " + msg)
		sys.exit(1)

	def __init__(self, name=''):
		# Variables set here are Instance Variables and are unique to the instantiated Instance
		self.name = name
		#logger.debug(f"DEBUG: dot_py_object_dict({self.name}): __init__ object instatiation")
		#self.BO = {}							# or, not
		self.BO = OrderedDict({})				# we can have the dictionary ordered if we want to
		return

	def __del__(self):
		#logger.debug(f"DEBUG: dot_py_object_dict({self.name}): __del__ to delete this object")
		return

	def dump_vars(self, heading='VARIABLES DUMP:'):
		global_dump_object_variables(self, heading)
		return

	def add_dot_py_obj(self, objBO):
		# assumes the incoming objBO is of class dot_py_object
		#https://docs.python.org/3/whatsnew/3.9.html#dictionary-merge-update-operators
		#If a key appears in both operands, the last-seen value (i.e. that from the right-hand operand) wins:
		# Dict Union is not commutative
		#logger.debug(f"DEBUG: Entered add_dot_py_obj")
		#self.BO = self.BO | { objBO.name : objBO.Val }
		self.BO |= { objBO.name : objBO.Val } # the operator '|=' appends to the dict
		#logger.debug(f"DEBUG: add_dot_py_obj: Added/updated dot_py_object_dict({self.name}): key='{objBO.name}'")
		#logger.debug(f"DEBUG: add_dot_py_obj: Added/updated dot_py_object_dict({self.name}): val='{objBO.Val}'")
		#logger.debug(f"DEBUG: add_dot_py_obj: DICTIONARY DUMP:")
		#for key, val in self.BO.items():
		#	logger.debug(f"DEBUG: add_dot_py_obj: name='{key}'")
		#	for key2, val2 in val.items():
		#		logger.debug(f"\t{key2}='{val2}'")
		#return

	def get_dot_py_obj(self, package_name):	
		# return a key/value pair as an object of class dot_py_object
		#logger.debug(f"DEBUG: Entered get_dot_py_obj")
		tmp = dot_py_object()					# create a new instance of class dot_py_object
		if package_name in self.BO:				# check whether a single key is in the dictionary
			tmp.name = package_name				# yes, insert the package name into the tmp object
			tmp.Val = self.BO[package_name]		# yes, insert the dict of json info into the tmp object
		else:
			tmp.name = None						# this should be the object's default for class dot_py_object anyway
			tmp.Val = {}						# this should be the object's default for class dot_py_object anyway
		return tmp								# return the object of class dot_py_object, wither filled in or with values None

	def load_py_files(self, folder='', heading=''):
		# Load .py files from the specified folder tree, if they are not disabled
		if not os.path.isdir(folder):
			self.errorExit(f"dot_py_object_dict({self.name}): load_py_files: Folder '{folder}' does not exist.")
		# Locate and save non-disabled .py file paths from the specified folder tree
		tmp_file_list = []
		for path, subdirs, files in os.walk(folder):
			for name in files:
				p = Path(os.path.join(path, name))
				if p.suffix == ".py":
					#logger.debug(f"load_py_files: dot_py_object_dict({self.name}): Found {heading} .py filename '{name}'")
					if not isPathDisabled(p):
						tmp_file_list.append(p)
						#logger.debug(f"load_py_files: dot_py_object_dict({self.name}): Saved {heading} .py filename '{name}'")
					else:
						logger.debug(f"load_py_files: dot_py_object_dict({self.name}): Ignored {heading} {name}.py due to isPathDisabled")

		if len(tmp_file_list) < 1:
			self.errorExit(f"load_py_files: There are no non-disabled .py files in the folder '{folder}'" )
		# Parse the saved non-disabled .py file paths and load the parsed filename/json pairs into the local dictionary already created within __init__
		for d in tmp_file_list:
			with open(d, "r", encoding="utf-8") as f:
				p = Path(d)
				packageName = p.stem.lower()
				try:
					objJSON = ast.literal_eval(f.read())
					if not isinstance(objJSON, dict):
						self.errorExit(f"load_py_files: dot_py_object_dict({self.name}): {heading} File '{packageName}' is misformatted")
					else:
						if boolKey(objJSON, "is_dep_inheriter"):
							logger.debug(f"load_py_files: dot_py_object_dict({self.name}): {heading} File '{packageName}.py' contains 'is_dep_inheriter'")
						if "_info" not in objJSON: # somehow this combo fails if include: and not boolKey(objJSON, "is_dep_inheriter")  
							logger.warning(f"load_py_files: dot_py_object_dict({self.name}): {heading} File '{packageName}.py' is missing '_info' tag")
						if boolKey(objJSON, "_disabled"):
							logger.debug(f"load_py_files: dot_py_object_dict({self.name}): Ignored {heading} {packageName} due to '_disabled'")
						else:
							# do it the long way around with an interim object, instead of of directly with name/value pair in the call
							obj = dot_py_object(name=packageName)		# create an object with the name/value pair
							obj.set_data_py(name=packageName, Val=objJSON) 		# this may not work ... it's an object being passed :(
							self.add_dot_py_obj(obj)	# save name/value pair into the dictionary in this instance
							del obj
							logger.debug(f"load_py_files: dot_py_object_dict({self.name}): {heading} File '{packageName}.py' loaded")
				except SyntaxError:
					self.errorExit(f"load_py_files: dot_py_object_dict({self.name}): Loading {heading} File '{packageName}' failed:\n\n{traceback.format_exc()}")
		logger.info(f"Loaded {len(self.BO)} {heading} files into dictionary {self.name}")
		return

	def list_print(self, heading=''):
		print(f"")
		print(f"LIST: {heading}:\n")
		for key, val in self.BO.items():
			if '_info' in val:
				#print(f"val['_info'] = {val['_info']}")
				#print(f"val['_info']['fancy_name'] = {val['_info']['fancy_name']}")
				#print(f"val['_info']['version'] = {val['_info']['version']}")
				if 'fancy_name' in val['_info']:
					fn = val['_info']['fancy_name']
				else:
					fn = ''
				if 'version' in val['_info']:
					v = val['_info']['version']
				else:
					v = ''
				info = f"'{fn}' ... version: '{v}'"
			else:
				info = ''
			pkey = key.ljust(32,' ')
			print(f" {pkey} ... {info}")
		return

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
		return

	def dump_vars(self, heading='VARIABLES DUMP:'):
		global_dump_object_variables(self, heading)
		return

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
def initLogger():
	global objSETTINGS		# the SETTINGS object used everywhere
	global logging_handler 	# the handler for the logger, only used for initialization
	global logger 			# the logger object used everywhere
	global objArgParser		# the ArgParser which may be used everywhere
	global objParser		# the parser creat6ed by ArgParser which may be used everywhere
	global dictProducts		# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for PRODUCTS only, of class dot_py_object_dict
	global dictDependencies	# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for DEPENDENCIES only, of class dot_py_object_dict
	global objVariables		# an object of the variables, of class dot_py_object
	global objPrettyPrint	# facilitates formatting and printing of text and dicts etc
	global TERMINAL_WIDTH	# for Console setup and PrettyPrint setup

	#print(f"TEMPORARY MESSAGE: initialize logging")
	logging_handler = logging.StreamHandler(sys.stdout)		# a handler for the logger
	fmt = MyLogFormatter(objSETTINGS.log_format, objSETTINGS.log_date_format)	# this is a class, it returns an object
	logging_handler.setFormatter(fmt)						# set the format into the handler for the logger
	logger = logging.getLogger(__name__)					# get an instance of the logger ?
	logger.addHandler(logging_handler)						# add our handler into the instance
	if objSETTINGS.debugMode:								# if objSETTINGS.debugMode is true, set loglevel to logging.DEBUG regardless of initial_logging_mode
		setLogLevel(logging.DEBUG)
	else:
		setLogLevel(objSETTINGS.initial_logging_mode)
	return

###################################################################################################
def setLogLevel(new_mode):
	# set the loglevel and track its current state in objSETTINGS.current_logging_mode
	# call with new_mode = (in order) one of logging.DEBUG logging.INFO logging.WARNING logging.ERROR 
	# when logging, any level LESS than the prevailing set loglevel is not logged by the logger
	global objSETTINGS		# the SETTINGS object used everywhere
	global logging_handler 	# the handler for the logger, only used for initialization
	global logger 			# the logger object used everywhere
	global objArgParser		# the ArgParser which may be used everywhere
	global objParser		# the parser creat6ed by ArgParser which may be used everywhere
	global dictProducts		# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for PRODUCTS only, of class dot_py_object_dict
	global dictDependencies	# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for DEPENDENCIES only, of class dot_py_object_dict
	global objVariables		# an object of the variables, of class dot_py_object
	global objPrettyPrint	# facilitates formatting and printing of text and dicts etc
	global TERMINAL_WIDTH	# for Console setup and PrettyPrint setup

	if new_mode not in [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR]:
		logger.setLevel(logging.DEBUG)
		logger.debug(f"INVALID setLogLevel specified '{new_mode}' ... note: logging.DEBUG={logging.DEBUG} logging.INFO={logging.INFO} logging.WARNING={logging.WARNING} logging.ERROR={logging.ERROR}")
		logger.setLevel(objSETTINGS.current_logging_mode)
	else:
		objSETTINGS.current_logging_mode = new_mode
		logger.setLevel(objSETTINGS.current_logging_mode)
		logger.debug(f"logger.setLevel to '{objSETTINGS.initial_logging_mode}'")
	return

###################################################################################################
def setDebugMode(new_debugMode):
	global objSETTINGS		# the SETTINGS object used everywhere
	global logging_handler 	# the handler for the logger, only used for initialization
	global logger 			# the logger object used everywhere
	global objArgParser		# the ArgParser which may be used everywhere
	global objParser		# the parser creat6ed by ArgParser which may be used everywhere
	global dictProducts		# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for PRODUCTS only, of class dot_py_object_dict
	global dictDependencies	# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for DEPENDENCIES only, of class dot_py_object_dict
	global objVariables		# an object of the variables, of class dot_py_object
	global objPrettyPrint	# facilitates formatting and printing of text and dicts etc
	global TERMINAL_WIDTH	# for Console setup and PrettyPrint setup

	if objSETTINGS.debugMode:
		objSETTINGS.debugMode = True
		setLogLevel(logging.DEBUG)
	else:
		objSETTINGS.debugMode = False
		setLogLevel(objSETTINGS.current_logging_mode)
		logger.debug(f"")
	logger.warning(f"DebugMode explicitly set to '{objSETTINGS.debugMode}'")
	return

###################################################################################################
class epiFormatter(argparse.RawDescriptionHelpFormatter):	# this class needss to be declared at the root level or argparse.argumentparser spews
	w = shutil.get_terminal_size((TERMINAL_WIDTH, 10))[0]
	def __init__(self, max_help_position=w, width=w, *args, **kwargs):
		kwargs['max_help_position'] = max_help_position
		kwargs['width'] = width
		super(epiFormatter, self).__init__(*args, **kwargs)
	def _split_lines(self, text, width):
		return text.splitlines()
class processCmdLineArguments():
	# Process arguments on CommandLine and change global settings accordingly
	global objSETTINGS		# the SETTINGS object used everywhere
	global logging_handler 	# the handler for the logger, only used for initialization
	global logger 			# the logger object used everywhere
	global objArgParser		# the ArgParser which may be used everywhere
	global objParser		# the parser creat6ed by ArgParser which may be used everywhere
	global dictProducts		# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for PRODUCTS only, of class dot_py_object_dict
	global dictDependencies	# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for DEPENDENCIES only, of class dot_py_object_dict
	global objVariables		# an object of the variables, of class dot_py_object
	global objPrettyPrint	# facilitates formatting and printing of text and dicts etc
	global TERMINAL_WIDTH	# for Console setup and PrettyPrint setup

	def dump_vars(self, heading='VARIABLES DUMP:'):
		global_dump_object_variables(self, heading)
		return
		
	def __init__(self):
		logger.debug(f"Entered processCmdLineArguments")

		# Create a neew main parser
		logger.debug(f"Creating the ArgumentParser with parser = argparse.ArgumentParser")
		self.parser_programname = 'h3333_python_cross_compile_script'
		self.parser_program_description = Colors.RESET + Colors.CYAN + self.parser_programname + Colors.RESET + "" \
										'\nExample usages:' \
										'\n "{0} list -p"                                   - lists all products' \
										'\n "{0} list -d"                                   - lists all dependencies' \
										'\n "{0} info --required_by avisynth_plus_headers"  - List all packages this dependency is required by' \
										'\n "{0} info --depends_on ffmpeg"                  - List all packages this package depends on (recursively)' \
										'\n "{0} --force --debug -d avisynth_plus_headers"  - forces rebuilding of dependency avisynth_plus_headers' \
										'\n "{0} --force -debug -p ffmpeg"                  - forces rebuilding of product ffmpeg' \
										'\n "{0} --cmd_help"                                - Do nothing but show help and exit' \
										''.format(self.parser_programname)
		self.parser_epilog = 'Copyright (C) 2023-2024 hydra3333 (https://github.com/hydra3333/h3333_python_cross_compile_script_v100)\n' \
						'This Source Code Form is subject to the terms of the\n' \
						'Mozilla Public License v. 2.0 (MPLv2).\n' \
						'If a copy of the MPLv2 was not distributed with this file,\n' \
						'You can obtain one at https://mozilla.org/MPL/2.0/ \n '
		self.parser = argparse.ArgumentParser(	formatter_class=epiFormatter, \
											prog=self.parser_programname, \
											description=self.parser_program_description, \
											epilog=self.parser_epilog )
		logger.debug(f"Created the ArgumentParser with argparse.ArgumentParser")

		# set a name in the top level main ArgumentParser
		logger.debug(f"Setting a name in the top level ArgumentParser")
		self.parser.set_defaults(which='main') # set a default argument "which" with a default value "main" in the main parser
		logger.debug(f"Set a name in the top level ArgumentParser")

		# add sub-parsers object to the main ArgumentParser object
		logger.debug(f"Add sub-parsers object to the top level ArgumentParser")
		self.subparsers = self.parser.add_subparsers(help='Sub commands')
		logger.debug(f"Added sub-parsers object to the top level ArgumentParser")

		# create and add the (sub)parser for the "list" command to the sub-parsers object 
		# and name it with which='list_p' ... parser.prog is the programname we set
		logger.debug(f"Create and add arguments to the (sub)parser for the 'list' command")
		self.list_p = self.subparsers.add_parser('list', help='Type: \'' + self.parser.prog + ' list')
		self.list_p.set_defaults(which='list')
		# add arguments to the 'list' command parser which='list_p'
		# Note: the second argument contains the variable-name to check later eg 'if args.dependencies'
		list_p_group1 = self.list_p.add_mutually_exclusive_group(required=True)
		list_p_group1.add_argument('-p', '--products',     help='List all products',     action='store_true', default=False)
		list_p_group1.add_argument('-d', '--dependencies', help='List all dependencies', action='store_true', default=False)
		# called like:	program.py list -d
		# 				program.py list -p
		logger.debug(f"Created and added arguments to the (sub)parser for the 'list' command")

		# create and add the (sub)parser for the "info" command to the sub-parsers object 
		# and name it with which='list_p' ... parser.prog is the programname we set
		logger.debug(f"Create and add arguments to the (sub)parser for the 'info' command")
		self.info_p = self.subparsers.add_parser('info', help='Type: \'' + self.parser.prog + ' info')
		self.info_p.set_defaults(which='info')
		# add arguments to the 'info' command parser which='info_p'
		# Note: the second argument contains the variable-name to check later eg 'args.required_by'
		self.info_p_group1 = self.info_p.add_mutually_exclusive_group(required=True)
		self.info_p_group1.add_argument('-r', '--required_by', help='List all packages this dependency is required by',        default=None)
		self.info_p_group1.add_argument('-d', '--depends_on',  help='List all packages this package depends on (recursively)', default=None)
		# called like:	program.py info -r avisynth_plus_headers
		# 				program.py info -d ffmpeg
		logger.debug(f"Created and added arguments to the (sub)parser for the 'info' command")

		# *** Now it is time for arguments to initiate the build process
		# create and add a mutually exclusive group to the main ArgumentParser object
		logger.debug(f"Create and add arguments to the top level ArgumentParser for building stuff")
		self.group2 = self.parser.add_mutually_exclusive_group(required=False)
		# add arguments to the mutially exclusive group, to build a dependency or a product
		# Note: the second argument contains the variable-name to check later eg 'if args.build_product'
		self.group2.add_argument('-p', '--build_product',    dest='PRODUCT',    help='Build the specificed product package(s)',	default=None)	# dest='PRODUCT', 
		self.group2.add_argument('-d', '--build_dependency', dest='DEPENDENCY', help='Build the specificed dependency package(s)',	default=None)	# dest='DEPENDENCY',
		self.group2.add_argument('-c', '--cmd_help', help='Do nothing but show help', action='store_true', default=False) # use '-c' since -h and --help CONFLICT with system stuff
		# called like:	program.py -d avisynth_plus_headers
		# 				program.py -p ffmpeg
		logger.debug(f"Created and added arguments to the top level ArgumentParser for building stuff")

		# *** Now it is time for generic arguments
		# add generic arguments to the main ArgumentParser object. 
		# Note the '-g' for debug, since "-d" is already taken for dependency processing
		# Note: the second argument contains the variable-name to check later eg 'if args.debug'
		logger.debug(f"Create and add arguments to the top level ArgumentParser for generic use")
		self.parser.add_argument('-g', '--debug',        help='Show debug information',										action='store_true', default=False)
		self.parser.add_argument('-f', '--force',        help='Force rebuild, deletes already existing files (recommended)',	action='store_true', default=False)
		self.parser.add_argument('-s', '--skip_depends', help='Skip dependencies when building',								action='store_true', default=False)
		# called like:	program.py --force --debug -d avisynth_plus_headers
		# 				program.py --force --debug -p ffmpeg
		# 				program.py --force --debug --skip-depends -p ffmpeg
		logger.debug(f"Created and added arguments to the top level ArgumentParser for generic use")

		# OK now we've setup the ArgumentParser stuff, lets parse the arguments and set variables in global objSETTINGS
		# We use that since it's commonly global, rather than another global object
		# note to self: ensure in objSETTINGS that all arguments are catered for and preset to None or something

		#
		self.args = self.parser.parse_args()		# ACTUALLY PARSE THE ARGUMENTS

		# Process generic args first
		if self.args.force:
			self.force = True
		else:
			self.force = False
		logger.debug(f"CMDLINE Processed arg self.args.force='{self.args.force}'")

		if self.args.skip_depends:
			self.skip_depends = True
		else:
			self.skip_depends = False
		logger.debug(f"CMDLINE Processed arg self.args.skip_depends='{self.args.skip_depends}'")

		if self.args.debug:
			self.debug = True
		else:
			self.debug = False
		# check and possibly over-ride any debug mode 
		logger.debug(f"CMDLINE Processing arg self.args.debug='{self.args.debug}' self.debug='{self.debug}' objSETTINGS.debugMode='{objSETTINGS.debugMode}' ")
		or_debug_modes = objSETTINGS.debugMode or self.debug
		if or_debug_modes:	# one or the other is true, so make it all true, a one-way
			self.debug = True
			setDebugMode(self.debug)
		logger.debug(f"CMDLINE Processed arg self.args.debug='{self.args.debug}' self.debug='{self.debug}' objSETTINGS.debugMode='{objSETTINGS.debugMode}' ")

		# initialize for finding specific commands and parameters
		self.list = False
		self.list_products = False
		self.list_dependencies = False
		self.info = False
		self.info_required_by = None
		self.info_depends_on = None
		self.build = False
		self.build_PRODUCT = None
		self.build_DEPENDENCY = None

		# Note: the 'match' statement only works in Python 3.10 and above # https://learnpython.com/blog/python-match-case-statement/
		match self.args.which.lower():
			case "list":
				logger.debug(f"CMDLINE Processing arg self.args.which='{self.args.which}'='list_p'")
				self.list = True
				if self.args.products:
					logger.debug(f"CMDLINE Processing arg self.args.products='{self.args.products}' in 'list_p'")
					self.list_products = True
				elif self.args.dependencies:
					logger.debug(f"CMDLINE Processing arg self.args.dependencies='{self.args.dependencies}' in 'list_p'")
					self.list_dependencies = True
				else:
					msg = f"CMDLINE Processing arg self.args.which='{self.args.which}' BUT THERE IS NO MATCHED CMDLINE CONDITION ... exiting"
					logger.error(msg)
					sys.exit(1)
			case "info":
				logger.debug(f"CMDLINE Processing arg self.args.which='{self.args.which}'='info_p'")
				self.info = True
				if self.args.required_by:
					# the name of the thing to process with INFO is in self.args.required_by
					logger.debug(f"CMDLINE Processed arg self.args.required_by='{self.args.required_by}' in 'info_p'")
					self.info_required_by = self.args.required_by
				elif self.args.depends_on:
					# the name of the thing to process with INFO is in self.args.depends_on
					logger.debug(f"CMDLINE Processing arg self.args.depends_on='{self.args.depends_on}' in 'info_p'")
					self.info_depends_on = self.args.depends_on
				else:
					msg = f"CMDLINE Processed arg self.args.which='{self.args.which}' BUT THERE IS NO MATCHED CMDLINE CONDITION ... exiting"
					logger.error(msg)
					sys.exit(1)
			case "main":
				logger.debug(f"CMDLINE Processing arg self.args.which='{self.args.which}'='main'")
				self.build = True
				if self.args.PRODUCT:
					self.build_PRODUCT = self.args.PRODUCT
					logger.debug(f"CMDLINE Processing arg self.args.which='{self.args.which}'='main' self.build_PRODUCT='{self.build_PRODUCT}'")
				elif self.args.DEPENDENCY:
					self.build_DEPENDENCY = self.args.DEPENDENCY
					logger.debug(f"CMDLINE Processing arg self.args.which='{self.args.which}'='main' self.build_PRODUCT='{self.build_DEPENDENCY}'")
				else:
					msg = f"CMDLINE Processed arg self.args.which='{self.args.which}' BUT THERE IS NO MATCHED CMDLINE CONDITION ... exiting"
					logger.error(msg)
					sys.exit(1)
			case _:	# the "_" means a final "else"
				msg = f"CMDLINE Processed arg self.args.which='{self.args.which}' BUT THERE IS NO MATCHING CMDLINE CONDITION ... exiting"
				logger.error(msg)
				sys.exit(1)
				sys.exit(1)

		# If it gets to here, relevant 'self' variables have been set to inform us what to do.
		# The relevant 'self' variables can be queried from the newly instantiated object. 
		# NOTE: the only exception is --debug which is processed straight away to change the global setting
		
		#logger.debug(f"*processCmdLineArguments self.list='{self.list}' self.list_products='{self.list_products}' self.list_dependencies='{ self.list_dependencies}'")
		#logger.debug(f"*processCmdLineArguments self.info='{self.info}' self.info_required_by='{self.info_required_by}' self.info_depends_on='{self.info_depends_on}'")
		#logger.debug(f"*processCmdLineArguments self.build='{self.build}' self.build_PRODUCT='{self.build_PRODUCT}' self.build_DEPENDENCY='{self.build_DEPENDENCY}'")
		#logger.debug(f"*processCmdLineArguments self.debug='{self.debug}'")
		#logger.debug(f"*processCmdLineArguments self.force='{self.force}'")
		#logger.debug(f"*processCmdLineArguments self.skip_depends='{self.skip_depends}'")
		#if objSETTINGS.debugMode:
		#	self.dump_vars('### debugMode: processCmdLineArguments INTERNAL VARIABLES DUMP:')
		
		logger.debug(f"Returning from processCmdLineArguments")

		return

###################################################################################################
def info_print_required_by(packageName):
	# recurrently print what is required by nominated package name ... will all be in dependencies
	global objSETTINGS		# the SETTINGS object used everywhere
	global logging_handler 	# the handler for the logger, only used for initialization
	global logger 			# the logger object used everywhere
	global objArgParser		# the ArgParser which may be used everywhere
	global objParser		# the parser creat6ed by ArgParser which may be used everywhere
	global dictProducts		# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for PRODUCTS only, of class dot_py_object_dict
	global dictDependencies	# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for DEPENDENCIES only, of class dot_py_object_dict
	global objVariables		# an object of the variables, of class dot_py_object
	global objPrettyPrint	# facilitates formatting and printing of text and dicts etc
	global TERMINAL_WIDTH	# for Console setup and PrettyPrint setup

	#logger.debug(f"info_print_required_by: Entered with packageName='{packageName}'")
	is_recognised = False
	obj_top_Package = None
	if packageName in dictProducts.BO:
		is_recognised = True
		obj_top_Package = dictProducts.get_dot_py_obj(packageName)		# returns an object of class dot_py_object 
		logger.debug(f"info_print_required_by: recognised '{packageName}' in dictProducts.BO")
		#logger.debug(f"info_print_required_by: dictProducts.BO['{packageName}']=\n'{objPrettyPrint.pformat(dictProducts.BO[packageName])}'") 
	if packageName in dictDependencies.BO:
		is_recognised = True
		obj_top_Package = dictDependencies.get_dot_py_obj(packageName)	# returns an object of class dot_py_object 
		logger.debug(f"info_print_required_by: recognised '{packageName}' in dictDependencies.BO")
		#logger.debug(f"info_print_required_by: dictDependencies.BO['{packageName}']=\n'{objPrettyPrint.pformat(dictDependencies.BO[packageName])}'") 
	if not is_recognised:
		logger.error(f"info_print_required_by: '{packageName}' is NOT a recognised package name")
		sys.exit(1)
	if obj_top_Package.name is None:
		logger.error(f"info_print_required_by: SANITY CHECK: '{packageName}' was recognised but NOT retrieved from the dictionary")
		sys.exit(1)
	logger.debug(f"info_print_required_by: dot_py_object class object for '{obj_top_Package.name}' successfully retrieved from the dictionary")
	#logger.debug(f"info_print_required_by: dot_py_object class object for '{obj_top_Package.name} Val':\n'{objPrettyPrint.pformat(obj_top_Package.Val)}'") 

	bigDict = dictProducts.BO | dictDependencies.BO		# allow both products and dependencies to be searched as one
	def info_print_required_by_recursive(packageName, indent=1):
		if 'depends_on' not in bigDict[packageName]:
			return
		zz_depends_on = bigDict[packageName]['depends_on']
		if len(zz_depends_on) <= 0:
			return
		#if boolKey(bigDict[packageName], "is_dep_inheriter"):
		#	return ret
		for d in zz_depends_on:
			_spaces = ' '*(4*indent)
			print(f"{_spaces}'{d}' is a child of '{packageName}'")
			sub = info_print_required_by_recursive(d,indent+1)
		return
	print(f"")
	msg = f"INFO: REQUIRED BY: The following package tree is required by '{packageName}':\n\n'{packageName}'"
	print(msg)
	info_print_required_by_recursive(obj_top_Package.name, indent=1)

###################################################################################################
def info_print_depends_on(packageName):
	# recurrently print what depends on nominated package name ...
	global objSETTINGS		# the SETTINGS object used everywhere
	global logging_handler 	# the handler for the logger, only used for initialization
	global logger 			# the logger object used everywhere
	global objArgParser		# the ArgParser which may be used everywhere
	global objParser		# the parser creat6ed by ArgParser which may be used everywhere
	global dictProducts		# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for PRODUCTS only, of class dot_py_object_dict
	global dictDependencies	# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for DEPENDENCIES only, of class dot_py_object_dict
	global objVariables		# an object of the variables, of class dot_py_object
	global objPrettyPrint	# facilitates formatting and printing of text and dicts etc
	global TERMINAL_WIDTH	# for Console setup and PrettyPrint setup

	#logger.debug(f"info_print_depends_on: Entered with packageName='{packageName}'")
	is_recognised = False
	obj_top_Package = None
	
	if packageName in dictProducts.BO:
		is_recognised = True
		obj_top_Package = dictProducts.get_dot_py_obj(packageName)		# returns an object of class dot_py_object 
		logger.debug(f"info_print_depends_on: recognised '{packageName}' in dictProducts.BO")
		#logger.debug(f"info_print_depends_on: dictProducts.BO['{packageName}']=\n'{objPrettyPrint.pformat(dictProducts.BO[packageName])}'") 
	if packageName in dictDependencies.BO:
		is_recognised = True
		obj_top_Package = dictDependencies.get_dot_py_obj(packageName)	# returns an object of class dot_py_object 
		logger.debug(f"info_print_depends_on: recognised '{packageName}' in dictDependencies.BO")
		#logger.debug(f"info_print_depends_on: dictDependencies.BO['{packageName}']=\n'{objPrettyPrint.pformat(dictDependencies.BO[packageName])}'") 
	if not is_recognised:
		logger.error(f"info_print_depends_on: '{packageName}' is NOT a recognised package name")
		sys.exit(1)
	if obj_top_Package.name is None:
		logger.error(f"info_print_depends_on: SANITY CHECK: '{packageName}' was recognised but NOT retrieved from the dictionary")
		sys.exit(1)
	logger.debug(f"info_print_depends_on: dot_py_object class object for '{obj_top_Package.name}' successfully retrieved from the dictionary")
	#logger.debug(f"info_print_depends_on: dot_py_object class object for '{obj_top_Package.name} Val':\n'{objPrettyPrint.pformat(obj_top_Package.Val)}'") 

	bigDict = dictProducts.BO | dictDependencies.BO		# allow both products and dependencies to be searched as one
	#objPrettyPrint.pprint(bigDict['ffmpeg'])
	#for key, val in bigDict.items():
	#	print(f"key='{key}'")
	#for key, val in bigDict['ffmpeg'].items():
	#	print(f"ffmpeg key='{key}'")
	#print(bigDict['ffmpeg'])
	n = packageName
	def info_print_depends_on_recursive(y,indent=1):
		for k, v in bigDict.items():
			if "depends_on" in bigDict[k]:
				if len(bigDict[k]['depends_on']) > 0:
					if y in bigDict[k]['depends_on']:
						_spaces = ' '*(4*indent)
						print(f"{_spaces}'{k}' is a parent of '{y}'")
						sub = info_print_depends_on_recursive(k,indent+1)
		return
	print(f"")
	msg = f"INFO: DEPENDS_ON: The following packages depend on '{packageName}':\n\n'{packageName}'"
	print(msg)
	info_print_depends_on_recursive(obj_top_Package.name, indent=1)

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
#objSETTINGS = settings()
#objSETTINGS.dump_vars("VARIABLES DUMP:")

if __name__ == "__main__":
	# GLOBALS are already defined at the top, this is __main__ so it sees them
	# NOTE:
	#	Apparently, also specifying globals inside a function/class-instance permits these to see
	#	globals as read/write global variables rather than as read-only global variables if at all
	
	# Initialize system stuff
	PY_REQUIRE = (3, 10)
	if sys.version_info < PY_REQUIRE:
		print(f"ERROR: You need at least Python %s.%s or later to run this script." % PY_REQUIRE)
		print(f"       Python 3.10 upwards implemented a 'switch case' feature called 'structural pattern matching'.\n" \
			   "       This script depends on that feature with the Python3 'match' and 'case' keywords.\n")
		sys.exit("You need at least Python %s.%s or later to run this script.\n" % PY_REQUIRE)
	sys.dont_write_bytecode = True  # Avoid __pycache__ folder, never liked that solution

	# Initialize PrettyPrint at the start
	objPrettyPrint = pprint.PrettyPrinter(width=TERMINAL_WIDTH, compact=False, sort_dicts=False)	# facilitates formatting and printing of text and dicts etc

	# Initialize global settings, they can be overridden later by commandline options
	objSETTINGS = settings()
	if objSETTINGS.debugMode:
		objSETTINGS.dump_vars('### debugMode: SETTINGS INTERNAL VARIABLES DUMP:')
	
	# Initialize Logging, this depends on objSETTINGS being initialized first
	initLogger()

	# Initialize DEBUG mode ... do it ONLY ONLY AFTER initLogger() since that sets the initial loglevel inside the logger
	setDebugMode(objSETTINGS.debugMode)

	# Process CMDLINE arguments into variables in the processCmdLineArguments object
	logger.debug(f"Processing CommandLine arguments")
	objArgParser = processCmdLineArguments()
	#if objSETTINGS.debugMode:
	#	objArgParser.dump_vars('### processCmdLineArguments: SETTINGS INTERNAL VARIABLES DUMP:')
	#objParser = objArgParser.parser	# the actual parser object
	# And just because we can, retrieve the parser object from our new objArgParser object
	#if objSETTINGS.debugMode:
	#	global_dump_object_variables(objParser, "### objParser retrieved from objArgParser")
	logger.debug(f"*objArgParser.list='{objArgParser.list}' objArgParser.list_products='{objArgParser.list_products}' objArgParser.list_dependencies='{ objArgParser.list_dependencies}'")
	logger.debug(f"*objArgParser.info='{objArgParser.info}' objArgParser.info_required_by='{objArgParser.info_required_by}' objArgParser.info_depends_on='{objArgParser.info_depends_on}'")
	logger.debug(f"*objArgParser.build='{objArgParser.build}' objArgParser.build_PRODUCT='{objArgParser.build_PRODUCT}' objArgParser.build_DEPENDENCY='{objArgParser.build_DEPENDENCY}'")
	logger.debug(f"*objArgParser.debug='{objArgParser.debug}'")
	logger.debug(f"*objArgParser.force='{objArgParser.force}'")
	logger.debug(f"*objArgParser.skip_depends='{objArgParser.skip_depends}'")

	# Reset logging level and Debug_mode
	or_debug_modes = objSETTINGS.debugMode or objArgParser.debug
	if or_debug_modes:	# one or the other is true, so make it all true, a one-way
		setDebugMode(or_debug_modes)
		logger.debug(f"Prepare: Reset logging level after cmdline arguments")

	# Initialize and load Products - note the use of a fixed text string type="P" to identify it as a product
	logger.debug(f"Prepare: Initialize and load products")
	dictProducts = dot_py_object_dict(name='PRODUCTS')	# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for PRODUCTS only, of class dot_py_object_dict
	products_folder_to_parse = objSETTINGS.prodFolder	# for input, eg /home/u/Desktop/working/packages/products
	dictProducts.load_py_files(folder=products_folder_to_parse, heading='Product')
	#dictProducts.dump_vars(heading='PRODUCT VARIABLES DUMP:')

	# Initialize and load dependencies - note the use of a fixed text string type="D" to identify it as a dependencies
	logger.debug(f"Prepare: Initialize and load dependencies")
	dictDependencies = dot_py_object_dict(name='DEPENDENCIES')	# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for DEPENDENCIES only, of class dot_py_object_dict
	dependencies_folder_to_parse = objSETTINGS.depsFolder	# for input, eg /home/u/Desktop/working/packages/dependencies
	dictDependencies.load_py_files(folder=dependencies_folder_to_parse, heading='Dependency')
	#dictDependencies.dump_vars(heading='DEPENDENCY VARIABLES DUMP:')

	# Initialize and load the Variables - note the use of a fixed text string type="V" to identify it as a Variables
	logger.debug(f"Prepare: Initialize and load variables.py")
	objVariables = dot_py_object(name='VARIABLES') # an object of the variables, of class dot_py_object
	variables_file_to_parse = objSETTINGS.varsPath	# for input, eg /home/u/Desktop/working/packages/variables.py
	objVariables.load_py_file(file=variables_file_to_parse, heading='Variables')
	#objVariables.dump_vars(heading='variables.py VARIABLES DUMP:')

	# DEBUG: have a look at products and dependencies and variables
	#
	#for key in dictProducts.BO:
	#	print(f"dictProducts(key)={key}")
	#for key, val in dictProducts.BO.items():
	#	#objPrettyPrint.pprint(key)
	#	#objPrettyPrint.pprint(val)
	#	tmp = "##### PRODUCT ##### " + objPrettyPrint.pformat(key) + " #####\n" + objPrettyPrint.pformat(val)
	#	print(tmp)
	#
	#for key in dictDependencies.BO:
	#	print(f"dictDependencies(key)={key}")
	#for key, val in dictDependencies.BO.items():
	#	#objPrettyPrint.pprint(key)
	#	#objPrettyPrint.pprint(val)
	#	tmp = "##### DEPENDENCY ##### " + objPrettyPrint.pformat(key) + " #####\n" + objPrettyPrint.pformat(val)
	#	#print(tmp)
	#
	#tmp = "##### VARIABLES #####\n" + objPrettyPrint.pformat(objVariables.Val)
	#print(tmp)

	# SANITY CHECK to ensure names are unique across PRODUCTS and DEPENDENCIES
	is_duplicated = False
	for key in dictProducts.BO:
		if key in dictDependencies.BO:
			is_duplicated = True
			logger.error(f"SANITY CHECK: PRODUCT: {key} has a duplicate filename in DEPENDENCIES")
	for key in dictDependencies.BO:
		if key in dictProducts.BO:
			is_duplicated = True
			logger.error(f"SANITY CHECK: DEPENDENCY: {key} has a duplicate filename in PRODUCTS")
	if is_duplicated:
		logger.error(f"SANITY CHECK: duplicated PRODUCT and DEPENDENCY filenames ... exiting")
		sys.exit(1)
	logger.info(f"SANITY CHECK: passed. No duplicate PRODUCT and DEPENDENCY filenames detected")

	# If commandline says INFO then do INFO stuff and exit
	if objArgParser.info:
		if objArgParser.info_depends_on:			# ./this_script.py --debug info --depends_on avisynth_plus_headers
			info_print_depends_on(objArgParser.info_depends_on)		# pass the name of the package the subject of the query
		if 	objArgParser.info_required_by:			# ./this_script.py --debug info --required_by ffmpeg
			info_print_required_by(objArgParser.info_required_by)	# pass the name of the package the subject of the query
		exit()

	# If commandline says LIST then do LIST stuff and exit
	if objArgParser.list:
		if objArgParser.list_products:				# ./this_script.py --debug list -d
			dictProducts.list_print(heading='PRODUCTS')
		if 	objArgParser.list_dependencies:			# ./this_script.py --debug list -p
			dictDependencies.list_print(heading='DEPENDENCIES')
		# for good measure, always list Variables free,gratis after the others
		objVariables.list_print(heading='VARIABLES')
		exit()



	# prepare ... 
	#	set environment variables
	#	create folder trees
	
	
	# set environment variables
	print(f"TEMPORARY MESSAGE: Prepare: prepare for building")
	logger.debug(f"Prepare: set environment variables")



	# create folder trees
	print(f"TEMPORARY MESSAGE: Prepare: create folder trees")
	logger.debug(f"Prepare: create folder trees")


	print(f"TEMPORARY MESSAGE: Prepare: init and load products")
	logger.debug(f"Prepare: init and load products")

	print(f"TEMPORARY MESSAGE: Prepare: init and load dependencies")
	logger.debug(f"Prepare: init and load dependencies")

	print(f"TEMPORARY MESSAGE: Prepare: init and load variables.py")
	logger.debug(f"Prepare: init and load variables.py")

	# if help or list etc, do that and exit

	print(f"TEMPORARY MESSAGE: if help or list etc, do that and exit")
	logger.debug(f"Prepare: if help or list etc, do that and exit")

	print(f"TEMPORARY MESSAGE: create folder trees")
	logger.debug(f"create folder trees")

	print(f"TEMPORARY MESSAGE: check and build the toolchain")
	logger.debug(f"check and build the toolchain")

	print(f"TEMPORARY MESSAGE: execute build etc")
	logger.debug(f"execute build etc")


	#parser_epilog = 'Copyright (C) 2023-2024 hydra3333\n\n This Source Code Form is subject to the terms of the GNU General Public License version 3 or any later version. If a copy of the GPLv3 was not distributed with this file, You may obtain one at https://www.gnu.org/licenses/gpl-3.0.html'
	#parser = argparse.ArgumentParser(formatter_class=epiFormatter, epilog=parser_epilog)
	
	exit()

##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################

'''
plans

a setlevel function per other, has global SETTINGS declared so as to reset it

global vars for packages,deps,variables

missing settings ??? 


		THEN prepareBuilding(self, bitness) DOES THIS
		---------------------------------------------
		self.logger.info('Starting build script')
		if not self.fullWorkDir.exists():
			self.logger.info("Creating workdir: %s" % (self.fullWorkDir))
			self.fullWorkDir.mkdir()
		self.cchdir(self.fullWorkDir)

		self.currentBitness = bitness
		self.bitnessStr = "x86_64" if bitness == 64 else "i686"  # e.g x86_64
		self.bitnessPath = self.fullWorkDir.joinpath("x86_64" if bitness == 64 else "i686")  # e.g x86_64
		GLOBAL_bitnessPath = self.bitnessPath
		#self.logger.info(F"DEBUG set GLOBAL_bitnessPath='{GLOBAL_bitnessPath}'")
		self.bitnessStr2 = "x86_64" if bitness == 64 else "x86"  # just for vpx...
		self.bitnessStr3 = "mingw64" if bitness == 64 else "mingw"  # just for openssl...
		self.targetOSStr = "mingw64" if bitness == 64 else "mingw32" # 2019.12.13 just for "--target-os=" 
		self.bitnessStrWin = "win64" if bitness == 64 else "win32"  # e.g win64
		self.targetHostStr = F"{self.bitnessStr}-w64-mingw32"  # e.g x86_64-w64-mingw32
		self.targetPrefix = self.fullWorkDir.joinpath(self.mingwDir, self.bitnessStr + "-w64-mingw32", self.targetHostStr)  # workdir/xcompilers/mingw-w64-x86_64/x86_64-w64-mingw32
		self.inTreePrefix = self.fullWorkDir.joinpath(self.bitnessStr)  # workdir/x86_64
		self.offtreePrefix = self.fullWorkDir.joinpath(self.bitnessStr + "_offtree")  # workdir/x86_64_offtree
		self.targetSubPrefix = self.fullWorkDir.joinpath(self.mingwDir, self.bitnessStr + "-w64-mingw32")  # e.g workdir/xcompilers/mingw-w64-x86_64
		self.mingwBinpath = self.fullWorkDir.joinpath(self.mingwDir, self.bitnessStr + "-w64-mingw32", "bin")  # e.g workdir/xcompilers/mingw-w64-x86_64/bin
		self.mingwBinpath2 = self.fullWorkDir.joinpath(self.mingwDir, self.bitnessStr + "-w64-mingw32", self.bitnessStr + "-w64-mingw32", "bin")  # e.g workdir/xcompilers/x86_64-w64-mingw32/x86_64-w64-mingw32/bin
		self.fullCrossPrefixStr = F"{self.mingwBinpath}/{self.bitnessStr}-w64-mingw32-"  # e.g workdir/xcompilers/mingw-w64-x86_64/bin/x86_64-w64-mingw32-
		self.shortCrossPrefixStr = F"{self.bitnessStr}-w64-mingw32-"  # e.g x86_64-w64-mingw32-
		self.autoConfPrefixOptions = F'--with-sysroot="{self.targetSubPrefix}" --host={self.targetHostStr} --prefix={self.targetPrefix} --disable-shared --enable-static'
		self.makePrefixOptions = F'CC={self.shortCrossPrefixStr}gcc ' \
			F"AR={self.shortCrossPrefixStr}ar " \
			F"PREFIX={self.targetPrefix} " \
			F"RANLIB={self.shortCrossPrefixStr}ranlib " \
			F"LD={self.shortCrossPrefixStr}ld " \
			F"STRIP={self.shortCrossPrefixStr}strip " \
			F'CXX={self.shortCrossPrefixStr}g++'  # --sysroot="{self.targetSubPrefix}"'
		self.pkgConfigPath = "{0}/lib/pkgconfig".format(self.targetPrefix)  # e.g workdir/xcompilers/mingw-w64-x86_64/x86_64-w64-mingw32/lib/pkgconfig
		self.localPkgConfigPath = self.aquireLocalPkgConfigPath()
		self.mesonEnvFile = self.fullWorkDir.joinpath("meson_environment.txt")
		self.cmakeToolchainFile = self.fullWorkDir.joinpath("mingw_toolchain.cmake")
		self.cmakePrefixOptions = F'-DCMAKE_TOOLCHAIN_FILE="{self.cmakeToolchainFile}" -G\"Ninja\"'
		self.cmakePrefixOptionsOld = "-G\"Unix Makefiles\" -DCMAKE_SYSTEM_PROCESSOR=\"{bitness}\" -DCMAKE_SYSTEM_NAME=Windows -DCMAKE_RANLIB={cross_prefix_full}ranlib -DCMAKE_C_COMPILER={cross_prefix_full}gcc -DCMAKE_CXX_COMPILER={cross_prefix_full}g++ -DCMAKE_RC_COMPILER={cross_prefix_full}windres -DCMAKE_FIND_ROOT_PATH={target_prefix}".format(cross_prefix_full=self.fullCrossPrefixStr, target_prefix=self.targetPrefix, bitness=self.bitnessStr)
		self.cpuCount = self.config["toolchain"]["cpu_count"]
		self.original_stack_protector = self.config["toolchain"]["original_stack_protector"]  # 2019.12.13
		self.original_stack_protector_trim = self.config["toolchain"]["original_stack_protector"].strip() # 2020.05.13
		self.original_fortify_source  = self.config["toolchain"]["original_fortify_source"] # 2019.12.13
		self.original_fortify_source_trim  = self.config["toolchain"]["original_fortify_source"].strip() # 2020.05.13
		self.originalCflag = self.config["toolchain"]["original_cflags"] # 2020.05.13 singular
		self.originalCflag_trim = self.config["toolchain"]["original_cflags"].strip() # 2020.05.13 singular
		self.originalCflags = "  " + self.config["toolchain"]["original_cflags"] + "  " + self.config["toolchain"]["original_stack_protector"] + "  " + self.config["toolchain"]["original_fortify_source"] + "  " # 2019.12.13 added stack protector and fortify source
		self.originalCflags_trim = (self.config["toolchain"]["original_cflags"] + "  " + self.config["toolchain"]["original_stack_protector"] + "  " + self.config["toolchain"]["original_fortify_source"]).strip() # 2020.05.13
		self.originbalLdLibPath = os.environ["LD_LIBRARY_PATH"] if "LD_LIBRARY_PATH" in os.environ else ""
		self.fullProductDir = self.fullWorkDir.joinpath(self.bitnessStr + "_products")
		GLOBAL_fullProductDir = self.fullProductDir
		#self.logger.info(F"DEBUG set GLOBAL_fullProductDir='{GLOBAL_fullProductDir}'")
		self.formatDict = defaultdict(lambda: "")
		self.formatDict.update(
			{
				'cmake_prefix_options': self.cmakePrefixOptions,
				'cmake_prefix_options_old': self.cmakePrefixOptionsOld,
				'make_prefix_options': self.makePrefixOptions,
				'autoconf_prefix_options': self.autoConfPrefixOptions,
				'pkg_config_path': self.pkgConfigPath,
				'local_pkg_config_path': self.localPkgConfigPath,
				'local_path': self.originalPATH,
				'mingw_binpath': self.mingwBinpath,
				'mingw_binpath2': self.mingwBinpath2,
				'cross_prefix_bare': self.shortCrossPrefixStr,
				'cross_prefix_full': self.fullCrossPrefixStr,
				'target_prefix': self.targetPrefix,
				'project_root': self.projectRoot,
				'work_dir': self.fullWorkDir,
				'inTreePrefix': self.inTreePrefix,
				'offtree_prefix': self.offtreePrefix,
				'target_host': self.targetHostStr,
				'target_sub_prefix': self.targetSubPrefix,
				'bit_name': self.bitnessStr,
				'bit_name2': self.bitnessStr2,
				'bit_name3': self.bitnessStr3,
				'bit_name_win': self.bitnessStrWin,
				'bit_num': self.currentBitness,
				'product_prefix': self.fullProductDir,
				'target_prefix_sed_escaped': str(self.targetPrefix).replace("/", "\\/"),
				'make_cpu_count': "-j {0}".format(self.cpuCount),
				'original_cflags': self.originalCflags,
				'cflag_string': self.generateCflagString('--extra-cflags='),
				'current_path': os.getcwd(),
				'current_envpath': self.getKeyOrBlankString(os.environ, "PATH"),
				'meson_env_file': self.mesonEnvFile
				# 2019.12.13 --- add own hydra3333 variables
				,'target_OS': self.targetOSStr
				,'prefix' : "{prefix}" # 2018.11.23 added a dummy variable replaced with itself, use in editing vapoursynth .pc files
				,'exec_prefix' : "{exec_prefix}" # 2018.11.23 added a dummy variable replaced with itself, use in editing vapoursynth .pc files
				,'original_cflags_trim': self.originalCflags_trim # 2020.05.13
				,'original_stack_protector' : self.original_stack_protector # 2019.11.15
				,'original_stack_protector_trim' : self.original_stack_protector_trim # 2020.05.13
				,'original_fortify_source' : self.original_fortify_source # 2019.11.15
				,'original_fortify_source_trim' : self.original_fortify_source_trim # 2020.05.13
				,'original_cflag': self.originalCflag # 2020.05.13
				,'original_cflag_trim': self.originalCflag_trim # 2020.05.13
			}
		)


		-----------------------------------------------------------------------------------------------------
		-----------------------------------------------------------------------------------------------------
		-----------------------------------------------------------------------------------------------------

		parser_epilog = 'Copyright (C) 2018-2023 DeadSix27 (https://github.com/DeadSix27/python_cross_compile_script)\n\n This Source Code Form is subject to the terms of the Mozilla Public\n License, v. 2.0. If a copy of the MPL was not distributed with this\n file, You can obtain one at https://mozilla.org/MPL/2.0/.\n '

		parser = argparse.ArgumentParser(formatter_class=epiFormatter, epilog=parser_epilog)
		parser.set_defaults(which='main')
		parser.description = Colors.CYAN + 'Pythonic Cross Compile Helper (MPL2.0)' + Colors.RESET + '\n\nExample usages:' \
			'\n "{0} list -p"             - lists all the products' \
			'\n "{0} -a"                  - builds everything' \
			'\n "{0} -f -d libx264"       - forces the rebuilding of libx264' \
			'\n "{0} -pl x265_10bit,mpv"  - builds this list of products in that order' \
			'\n "{0} -q -p ffmpeg_static" - will quietly build ffmpeg-static'.format(parser.prog)

		subparsers = parser.add_subparsers(help='Sub commands')

		list_p = subparsers.add_parser('list', help='Type: \'' + parser.prog + ' list --help\' for more help')
		list_p.set_defaults(which='list_p')

		list_p.add_argument('-md', '--markdown', help='Print list in markdown format', action='store_true')
		list_p.add_argument('-cv', '--csv', help='Print list as CSV-like string', action='store_true')
		list_p_group1 = list_p.add_mutually_exclusive_group(required=True)
		# BELOW: so, by the time this is called: self.listifyPackages(self.packages["prods"], "P")
		#	self.packages["prods"] has already been loaded WITHOUT variable processing on 'branch' (to do so requires change folder to the prod item's parent folder and back each time to allow for relative folder CMD processing)
		list_p_group1.add_argument('-p', '--products', nargs=0, help='List all products', action=self.listifyPackages(self.packages["prods"], "P"))
		# BELOW: so, by the time this is called: self.listifyPackages(self.packages["deps"], "D")
		#	self.packages["deps"]  has already been loaded WITHOUT variable processing on 'branch' (to do so requires change folder to the prod item's parent folder and back each time to allow for relative folder CMD processing)
		list_p_group1.add_argument('-d', '--dependencies', nargs=0, help='List all dependencies', action=self.listifyPackages(self.packages["deps"], "D"))

		chelps_p = subparsers.add_parser('chelps', help='Type: \'' + parser.prog + ' chelps --help\' for more help')
		list_p.set_defaults(which='chelps_p')
		chelps_p_group1 = chelps_p.add_mutually_exclusive_group(required=True)
		chelps_p_group1.add_argument('-p', '--products', nargs=0, help='Write all product config helps to confighelps.txt', action=self.assembleConfigHelps(self.packages["prods"], "P", self))
		chelps_p_group1.add_argument('-d', '--dependencies', nargs=0, help='Write all dependency config helps to confighelps.txt', action=self.assembleConfigHelps(self.packages["deps"], "D", self))

		info_p = subparsers.add_parser('info', help='Type: \'' + parser.prog + ' info --help\' for more help')
		info_p.set_defaults(which='info_p')

		info_p_group1 = info_p.add_mutually_exclusive_group(required=True)
		info_p_group1.add_argument('-r', '--required-by', help='List all packages this dependency is required by', default=None)
		info_p_group1.add_argument('-d', '--depends-on', help='List all packages this package depends on (recursively)', default=None)

		group2 = parser.add_mutually_exclusive_group(required=False)
		group2.add_argument('-p', '--build-product', dest='PRODUCT', help='Build the specificed product package(s)')
		group2.add_argument('-d', '--build-dependency', dest='DEPENDENCY', help='Build the specificed dependency package(s)')
		group2.add_argument('-a', '--build-all', help='Build all products (according to order)', action='store_true')
		
		parser.add_argument('-g', '--debug', help='Show debug information', action='store_true')
		parser.add_argument('-q', '--quiet', help='Only show info lines', action='store_true')
		parser.add_argument('-f', '--force', help='Force rebuild, deletes already files', action='store_true')
		parser.add_argument('-s', '--skip-depends', help='Skip dependencies when building', action='store_true')

		#----------------------------------------------------------------------------------------------------------
		# 2020.05.25 add -k --backup
		parser.add_argument('-k', '--backup-source-directory', action='store', type=str, required=False, help='Backup source folder(s) to this specified backup folder name (strictly no trees)')
		#----------------------------------------------------------------------------------------------------------

		if len(sys.argv) == 1:
			self.defaultEntrace()
		else:
			def errorOut(p, t, m=None):
				if m is None:
					fullStr = Colors.LIGHTRED_EX + 'Error:\n ' + Colors.CYAN + '\'{0}\'' + Colors.LIGHTRED_EX + ' is not a valid {2}\n Type: ' + Colors.CYAN + '\'{1} list --products/--dependencies\'' + Colors.LIGHTRED_EX + ' for a full list'
					print(fullStr.format(p, os.path.basename(__file__), "Product" if t == "PRODUCT" else "Dependency") + Colors.RESET)
				else:
					print(m)
				exit(1)
			args = parser.parse_args()

			if args.which == "info_p":
				if args.required_by:
					self.listRequiredBy(args.required_by)
				if args.depends_on:
					self.listDependsOn(args.depends_on)
				return

			forceRebuild = False
			if args.debug:
				self.debugMode = True
				#self.logger.info("commandLineEntrace args.debug=True, set self.debugMode=True, executing self.initDebugMode()")
				self.initDebugMode()
				#self.logger.info("commandLineEntrace args.debug=True, TEST of log statement with .info ")
				#self.logger.debug("commandLineEntrace args.debug=True, TEST of log statement with .debug ")
			if args.quiet:
				self.quietMode = True
				#self.logger.info("commandLineEntrace args.quiet=True, set self.quietMode=True, executing self.initQuietMode()")
				self.initQuietMode()
			if args.force:
				forceRebuild = True
				#self.logger.info("commandLineEntrace args.force=True, set forceRebuild=True")

			buildType = None
			
			if args.backup_source_directory:  # note, "-" relaced by "_" in the name
				self.backup_source_directory = args.backup_source_directory
			else:
				self.backup_source_directory = None

			finalPkgList = []

			if args.PRODUCT or args.DEPENDENCY:
				strPkgs = args.DEPENDENCY
				buildType = "DEPENDENCY"
				if args.PRODUCT is not None:
					strPkgs = args.PRODUCT
					buildType = "PRODUCT"
				pkgList = re.split(r'(?<!\\),', strPkgs)
				for p in pkgList:
					if buildType == "PRODUCT":
						if p not in self.packages["prods"]:
							self.errorExit("Product package '%s' does not exist." % (p))
					if buildType == "DEPENDENCY":
						if p not in self.packages["deps"]:
							self.errorExit("Dependency package '%s' does not exist." % (p))

					finalPkgList.append(p.replace("\\,", ","))

			elif args.build_all:
				self.defaultEntrace()
				return

			self.logger.info('Starting custom build process for: {0}'.format(",".join(finalPkgList)))

			skipDeps = False

			if args.skip_depends:
				skipDeps = True

			for thing in finalPkgList:
				for b in self.targetBitness:
					main.prepareBuilding(b)
					main.buildMingw(b)
					main.initBuildFolders()
					if buildType == "PRODUCT":
						self.buildThing(thing, self.packages["prods"][thing], buildType, forceRebuild, skipDeps)
					else:
						self.buildThing(thing, self.packages["deps"][thing], buildType, forceRebuild, skipDeps)
					main.finishBuilding()


'''