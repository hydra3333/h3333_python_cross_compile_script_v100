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

global logging_handler 	# the handler for the logger, only used for initialization
global logger 			# the logger object used everywhere
global SETTINGS			# the SETTINGS object used everywhere

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

###################################################################################################
class settings:
	# https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables
	# Variables set at the top here are Class Variables and apparently shared across all instances
	
	def errorExit(self, msg): # logger is not up and running yer, so use our own self.errorExit instead
		#logger.error(msg)
		print("Settings Error: " + msg)
		sys.exit(1)
	
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

	def dump_vars(self, heading='VARIABLES DUMP:'):
		global_dump_object_variables(self, heading)


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
def initLogger():
	global SETTINGS
	global logging_handler
	global logger
	#print(f"TEMPORARY MESSAGE: initialize logging")
	logging_handler = logging.StreamHandler(sys.stdout)		# a handler for the logger
	fmt = MyLogFormatter(SETTINGS.log_format, SETTINGS.log_date_format)	# this is a class, it returns an object
	logging_handler.setFormatter(fmt)						# set the format into the handler for the logger
	logger = logging.getLogger(__name__)					# get an instance of the logger ?
	logger.addHandler(logging_handler)						# add our handler into the instance
	if SETTINGS.debugMode:									# if SETTINGS.debugMode is true, set loglevel to logging.DEBUG regardless of initial_logging_mode
		setLogLevel(logging.DEBUG)
	else:
		setLogLevel(SETTINGS.initial_logging_mode)
	return

###################################################################################################
def setLogLevel(new_mode):
	# set the loglevel and track its current state in SETTINGS.current_logging_mode
	# call with new_mode = (in order) one of logging.DEBUG logging.INFO logging.WARNING logging.ERROR 
	# when logging, any level LESS than the prevailing set loglevel is not logged by the logger
	global SETTINGS
	global logging_handler
	global logger
	if new_mode not in [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR]:
		logger.setLevel(logging.DEBUG)
		logger.debug(f"INVALID setLogLevel specified '{new_mode}' ... note: logging.DEBUG={logging.DEBUG} logging.INFO={logging.INFO} logging.WARNING={logging.WARNING} logging.ERROR={logging.ERROR}")
		logger.setLevel(SETTINGS.current_logging_mode)
	else:
		SETTINGS.current_logging_mode = new_mode
		logger.setLevel(SETTINGS.current_logging_mode)
		logger.debug(f"logger.setLevel to '{SETTINGS.initial_logging_mode}'")
	return

###################################################################################################
def setDebugMode(new_debugMode):
	global SETTINGS
	global logging_handler
	global logger
	if SETTINGS.debugMode:
		SETTINGS.debugMode = True
		setLogLevel(logging.DEBUG)
	else:
		SETTINGS.debugMode = False
		setLogLevel(SETTINGS.current_logging_mode)
		logger.debug(f"")
	logger.warning(f"DebugMode explicitly set to '{SETTINGS.debugMode}'")
	return

###################################################################################################
def processCmdLineArguments():
	# Process arguments on CommandLine and change global settings accordingly
	global SETTINGS
	global logging_handler
	global logger
	class epiFormatter(argparse.RawDescriptionHelpFormatter):
		w = shutil.get_terminal_size((120, 10))[0]
		def __init__(self, max_help_position=w, width=w, *args, **kwargs):
			kwargs['max_help_position'] = max_help_position
			kwargs['width'] = width
			super(epiFormatter, self).__init__(*args, **kwargs)
		def _split_lines(self, text, width):
			return text.splitlines()

	logger.debug(f"Entered processCmdLineArguments")
	
	# Create a neew main parser
	logger.debug(f"Creating the ArgumentParser with parser = argparse.ArgumentParser")
	parser_programname = 'h3333_python_cross_compile_script'
	parser_program_description = Colors.RESET + Colors.CYAN + parser_programname + Colors.RESET + "\n" \
									'\nExample usages:' \
									'\n "{0} list -p"             - lists all the products' \
									'\n "{0} -a"                  - builds everything' \
									'\n "{0} -f -d libx264"       - forces the rebuilding of libx264' \
									'\n "{0} -pl x265_10bit,mpv"  - builds this list of products in that order' \
									'\n "{0} -q -p ffmpeg_static" - will quietly build ffmpeg-static'.format(parser_programname)
	parser_epilog = 'Copyright (C) 2023-2024 hydra3333 (https://github.com/hydra3333/h3333_python_cross_compile_script_v100)\n' \
					'This Source Code Form is subject to the terms of the Mozilla Public\n License v. 2.0 (MPLv2).\n' \
					'If a copy of the MPLv2 was not distributed with this file,\n' \
					'You can obtain one at https://mozilla.org/MPL/2.0/ \n '
	parser = argparse.ArgumentParser(	formatter_class=epiFormatter, \
										prog=parser_programname, \
										description=parser_program_description, \
										epilog=parser_epilog )
	logger.debug(f"Created the ArgumentParser with argparse.ArgumentParser")

	# set a name in the top level main ArgumentParser
	logger.debug(f"Setting a name in the top level ArgumentParser")
	parser.set_defaults(which='main') # set a default argument "which" with a default value "main" in the main parser
	logger.debug(f"Set a name in the top level ArgumentParser")

	# add sub-parsers object to the main ArgumentParser object
	logger.debug(f"Add sub-parsers object to the top level ArgumentParser")
	subparsers = parser.add_subparsers(help='Sub commands')
	logger.debug(f"Added sub-parsers object to the top level ArgumentParser")

	# create and add the (sub)parser for the "list" command to the sub-parsers object 
	# and name it with which='list_p' ... parser.prog is the programname we set
	logger.debug(f"Create and add arguments to the (sub)parser for the 'list' command")
	list_p = subparsers.add_parser('list', help='Type: \'' + parser.prog + ' list')
	list_p.set_defaults(which='list_p')
	# add arguments to the 'list' command parser which='list_p'
	# Note: the second argument contains the variable-name to check later eg 'if args.dependencies'
	list_p_group1 = list_p.add_mutually_exclusive_group(required=True)
	#list_p_group1.add_argument('-p', '--products',     nargs=0, help='List all products',     action='store_true', default=False)
	#list_p_group1.add_argument('-d', '--dependencies', nargs=0, help='List all dependencies', action='store_true', default=False)
	list_p_group1.add_argument('-p', '--products',     help='List all products',     action='store_true', default=False)
	list_p_group1.add_argument('-d', '--dependencies', help='List all dependencies', action='store_true', default=False)
	# called like:	program.py list -d
	# 				program.py list -p
	logger.debug(f"Created and added arguments to the (sub)parser for the 'list' command")

	# create and add the (sub)parser for the "info" command to the sub-parsers object 
	# and name it with which='list_p' ... parser.prog is the programname we set
	logger.debug(f"Create and add arguments to the (sub)parser for the 'info' command")
	info_p = subparsers.add_parser('info_p', help='Type: \'' + parser.prog + ' info')
	info_p.set_defaults(which='info_p')
	# add arguments to the 'info' command parser which='info_p'
	# Note: the second argument contains the variable-name to check later eg 'args.required_by'
	info_p_group1 = info_p.add_mutually_exclusive_group(required=True)
	info_p_group1.add_argument('-r', '--required_by', help='List all packages this dependency is required by',        default=None)
	info_p_group1.add_argument('-d', '--depends_on',  help='List all packages this package depends on (recursively)', default=None)
	# called like:	program.py info -r avisynth_plus_headers
	# 				program.py info -d ffmpeg
	logger.debug(f"Created and added arguments to the (sub)parser for the 'info' command")

	# *** Now it is time for arguments to initiate the build process
	# create and add a mutually exclusive group to the main ArgumentParser object
	logger.debug(f"Create and add arguments to the top level ArgumentParser for building stuff")
	group2 = parser.add_mutually_exclusive_group(required=False)
	# add arguments to the mutially exclusive group, to build a dependency or a product
	# Note: the second argument contains the variable-name to check later eg 'if args.build_product'
	group2.add_argument('-p', '--build_product',    help='Build the specificed product package(s)',		default=None)	# dest='PRODUCT', 
	group2.add_argument('-d', '--build_dependency', help='Build the specificed dependency package(s)',	default=None)	# dest='DEPENDENCY',
	group2.add_argument('-c', '--cmd_help',            help='Do nothing but show help', action='store_true', default=False) # use '-c' since -h and --help CONFLICT with system stuff
	# called like:	program.py -d avisynth_plus_headers
	# 				program.py -p ffmpeg
	logger.debug(f"Created and added arguments to the top level ArgumentParser for building stuff")

	# *** Now it is time for generic arguments
	# add generic arguments to the main ArgumentParser object. 
	# Note the '-g' for debug, since "-d" is already taken for dependency processing
	# Note: the second argument contains the variable-name to check later eg 'if args.debug'
	logger.debug(f"Create and add arguments to the top level ArgumentParser for generic use")
	parser.add_argument('-g', '--debug',        help='Show debug information',										action='store_true', default=False)
	parser.add_argument('-f', '--force',        help='Force rebuild, deletes already existing files (recommended)',	action='store_true', default=False)
	parser.add_argument('-s', '--skip-depends', help='Skip dependencies when building',								action='store_true', default=False)
	# called like:	program.py --force --debug -d avisynth_plus_headers
	# 				program.py --force --debug -p ffmpeg
	# 				program.py --force --debug --skip-depends -p ffmpeg
	logger.debug(f"Created and added arguments to the top level ArgumentParser for generic use")


	logger.debug(f"Returning from processCmdLineArguments")
	return








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
#SETTINGS = settings()
#SETTINGS.dump_vars("VARIABLES DUMP:")

if __name__ == "__main__":
	# GLOBALS are already defined at the top, this is __main__ so it sees them
	# NOTE:
	#	Apparently, also specifying globals inside a function/class-instance permits these to see
	#	globals as read/write global variables rather than as read-only global variables if at all
	
	# process CMDLINE arguments and change settings
	# prepare ... 
	#	reset logging level after cmdline arguments
	#	set environment variables
	#	init and load products
	#	init and load dependencies
	#	init and load variables (the .py)
	# if help or list etc, do that and exit
	# create folder trees
	# check and build the toolchain
	# execute build etc

	# initialize system stuff
	print(f"TEMPORARY MESSAGE: initialize system stuff")
	PY_REQUIRE = (3, 8)
	if sys.version_info < PY_REQUIRE:
		sys.exit("You need at least Python %s.%s or later to run this script.\n" % PY_REQUIRE)
	sys.dont_write_bytecode = True  # Avoid __pycache__ folder, never liked that solution

	# Initialize global settings, they can be overridden later by commandline options
	print(f"TEMPORARY MESSAGE: Initialize global settings")	# logger not available yet, do not do logging.info etc
	SETTINGS = settings()
	if SETTINGS.debugMode:
		SETTINGS.dump_vars("SETTINGS in debugMode")
	
	# Initialize Logging
	initLogger()

	# Initialize DEBUG mode ... ONLY ONLY AFTER initLogger() since that sets the initial loglevel
	setDebugMode(SETTINGS.debugMode)

	# process CMDLINE arguments
	logger.debug(f"Processing CommandLine arguments")
	processCmdLineArguments()




	# prepare ... 
	#	reset logging level after cmdline arguments, create folder trees
	#	set environment variables
	#	init and load products
	#	init and load dependencies
	#	init and load variables (the .py)
	#
	print(f"TEMPORARY MESSAGE: Commencing Preparation ...")
	logger.debug(f"Commencing Preparation ...")

	print(f"TEMPORARY MESSAGE: Prepare: Reset logging level after cmdline arguments")
	logger.debug(f"Prepare: Reset logging level after cmdline arguments")
	
	# set environment variables
	print(f"TEMPORARY MESSAGE: Prepare: set environment variables")
	logger.debug(f"Prepare: set environment variables")
	#os.environ["PATH"] = "{0}:{1}".format(self.mingwBinpath, self.originalPATH)
	#os.environ["PKG_CONFIG_PATH"] = self.pkgConfigPath
	#os.environ["PKG_CONFIG_LIBDIR"] = ""
	#os.environ["COLOR"] = "ON"  # Force coloring on (for CMake primarily)
	#os.environ["CLICOLOR_FORCE"] = "ON"  # Force coloring on (for CMake primarily)

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