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

###################################################################################################
class settings:
	# https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables
	# Variables set here are Class Variables and are shared across all instances

	def __init__(self):

		
		Then init() DOES THIS
		---------------------
		self.originalPATH = os.environ["PATH"]


		if self.debugMode:
			self.initDebugMode()
			#self.logger.info('init: self.debugMode=True so initDebugMode executed')
		if self.quietMode:
			self.initQuietMode()


		THEN commandLineEntrace DOES THIS
		---------------------------------
		
					main.prepareBuilding(b)

		COMMANDLKINE ENTRANCE CALLS defaultEntrace
		------------------------------------------
		
		defaultEntrace CALLS prepareBuilding
		------------------------------------

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

		self.config = self.formatConfig(self.config)
		self.fullOutputDir = self.projectRoot.joinpath(self.replaceToolChainVars(self.config["toolchain"]["output_path"]))
		self.formatDict['output_prefix'] = str(self.fullOutputDir)

		os.environ["PATH"] = "{0}:{1}".format(self.mingwBinpath, self.originalPATH)
		# os.environ["PATH"] = "{0}:{1}:{2}".format (self.mingwBinpath, os.path.join(self.targetPrefix, 'bin'), self.originalPATH)  # TODO: properly test this..
		os.environ["PKG_CONFIG_PATH"] = self.pkgConfigPath
		os.environ["PKG_CONFIG_LIBDIR"] = ""
		os.environ["COLOR"] = "ON"  # Force coloring on (for CMake primarily)
		os.environ["CLICOLOR_FORCE"] = "ON"  # Force coloring on (for CMake primarily)

		-----------------------------------------------------------------------------------------------------
		-----------------------------------------------------------------------------------------------------
		-----------------------------------------------------------------------------------------------------

		OUR VERSION OF SETTTINGS
		------------------------

		self.DEBUG_MODE = False											# True or False
		if self.DEBUG_MODE:
			self.initial_logging_mode = logging.DEBUG					# at what level to start logging initially. logging.INFO logging.DEBUG
		else:
			self.initial_logging_mode = logging.INFO					# at what level to start logging initially. logging.INFO logging.DEBUG

		# fixed variables first, calculated variables next
		self.bitness = 64												# bits to build ffmpeg etc
		self.toolchain_bitness = self.bitness							# bits to build the toolchain
		self.targetBitness = self.bitness
		self.cpu_count = cpu_count()									# number of CPUs on this machine
		self.projectRoot = Path(os.getcwd())							# root folder for this script eg /home/u/Desktop/working
		self.originalPATH = os.environ["PATH"] 							# the original environment path, used for resets

		self.packages_subfolder = 'packages'							# 'packages' is the subfolder where the .py files reside
		self.patches_subfolder = 'patches'								# 'packages' is the subfolder where the patch files reside
		self.workdir_subfolder ='workdir'								# 'workdir'  is the subfolder where actual build stuff happens
		self.bitnessStr = "x86_64"										# eg x86_64 underneath workdir_subfolder
		self.bitnessStr2 = "x86_64"										# just for vpx... underneath workdir_subfolder
		self.bitnessStr3 = "mingw64"									# just for openssl... underneath workdir_subfolder
		self.targetOSStr = "mingw64"									# 2019.12.13 just for "--target-os=" 
		self.bitnessStrWin = "win64"									# eg 'win64'

		self.original_cflags': '-O3',
		self.original_stack_protector' : '-fstack-protector-all'
		self.original_fortify_source'  : '-D_FORTIFY_SOURCE=2'
		
		self.toolchain_mingw_subfolder = 'toolchain'					# eg 'toolchain' underneath workdir_subfolder
		self.toolchain_mingw_toolchain_script_subfolder = "mingw_toolchain_script"
		self.toolchain_mingw_toolchain_script_name = 'mingw_toolchain_script_v100_002_like_zeranoe.py'
		self.toolchain_mingw_commit = None				# specify a commit, or None which leaves that up to the toolchain builder
		self.toolchain_mingw_debug_build = False
		self.toolchain_mingw_custom_cflags = None
		
		self.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
		self.log_date_format = '%H:%M:%S'
		self.log_format = '[%(asctime)s][%(levelname)s]%(type)s %(message)s'


???

		self.fullPatchDir = self.projectRoot.joinpath("patches")
		self.originalPATH = os.environ["PATH"]
???

		# calculated variables next
		

		self.packagesFolder = self.projectRoot.join(self.packages_subfolder)	# for input, eg /home/u/Desktop/working/packages
		self.prodFolder     = self.packagesFolder.join("products")				# for input, eg /home/u/Desktop/working/packages/products
		self.depsFolder     = self.packagesFolder.join("dependencies")			# for input, eg /home/u/Desktop/working/packages/dependencies
		self.varsPath       = self.packagesFolder.join("variables.py")			# for input, eg /home/u/Desktop/working/packages/variables.py
		self.patchesFolder	= self.projectRoot.join(self.patches_subfolder)		# for input, eg /home/u/Desktop/working/packages
		self.fullWorkDir    = self.projectRoot.join(self.workdir_subfolder)		# for output, eg /home/u/Desktop/working/workdir
		
		self.targetHostStr = F"{self.bitnessStr}-w64-mingw32"  			# e.g x86_64-w64-mingw32
		self.bitnessPath = self.fullWorkDir.joinpath(self.bitnessStr)	# for output, eg /home/u/Desktop/working/workdir/x86_64
		self.fullProductDir = self.bitnessPath.joinpath('_products')	# for output, eg /home/u/Desktop/working/workdir/x86_64_products
		self.fullDependencyDir = self.bitnessPath.joinpath('')			# to be compatible with deadsix27, rather than use a new 'x86_64_dependencies'

		self.mingw_toolchain_script_folder = self.projectRoot.join(self.toolchain_mingw_toolchain_script_subfolder)
		self.mingw_toolchain_script_path = self.mingw_toolchain_script_folder.join(self.toolchain_mingw_toolchain_script_name)

		self.toolchain_output_path = self.fullWorkDir.join(self.bitnessStrWin + "_output")

		if not os.path.isdir(self.packagesFolder):	# for input, eg /home/u/Desktop/working/packages
			errorExit(f"Packages folder '{self.packagesFolder}' does not exist.")
		if not os.path.isdir(self.prodFolder):	# for input, eg /home/u/Desktop/working/packages/products
			errorExit(f"Packages Products folder '{self.prodFolder}' does not exist.")
		if not os.path.isdir(delf.depsFolder):	# for input, eg /home/u/Desktop/working/packages/dependencies
			errorExit(f"Packages Dependencies folder '{self.depsFolder}' does not exist.")
		if not os.path.isfile(self.varsPath):	# for input, eg /home/u/Desktop/working/packages/variables.py
			errorExit(f"Variables file '{self.varsPath}' does not exist." )
		if not os.path.isdir(self.patchesFolder):	# for input, eg /home/u/Desktop/working/packages
			errorExit(f"Patches folder '{self.patchesFolder}' does not exist." )
		# ??? hmm, this next subfolder may need to be created during setup for building, not here at settings
		if not os.path.isdir(self.fullWorkDir):	# for output, eg /home/u/Desktop/working/workdir
			errorExit(f"Working folder '{self.fullWorkDir}' does not exist.")
		# ??? hmm, this next subfolder may need to be created during setup for building, not here at settings
		if not os.path.isdir(self.bitnessPath):	# for output, eg /home/u/Desktop/working/workdir/x86_64
			errorExit(f"Working folder '{self.bitnessPath}' does not exist.")
		# ??? hmm, this next subfolder may need to be created during setup for building, not here at settings
		if not os.path.isdir(self.fullProductDir):	# for output, eg /home/u/Desktop/working/workdir/x86_64_products
			errorExit(f"Working folder '{self.fullProductDir}' does not exist.")
		# ??? hmm, this next subfolder may need to be created during setup for building, not here at settings
		if not os.path.isdir(self.fullDependencyDir):	# to be compatible with deadsix27, rather than use a new 'x86_64_dependencies'
			errorExit(f"Working folder '{self.fullDependencyDir}' does not exist.")
		if not os.path.isdir(self.mingw_toolchain_script_folder):	# the subfolder where the toolchain build script resides
			errorExit(f"mingw build script folder '{self.mingw_toolchain_script_folder}' does not exist.")
		if not os.path.isfile(self.mingw_toolchain_script_path):	# the full path to the toolchain build script
			errorExit(f"mingw build script file '{self.mingw_toolchain_script_path}' does not exist." )
		# ??? hmm, this subfolder may need to be created during setup for building, not here at settings
		if not os.path.isdir(self.toolchain_output_path):			# the subfolder where the toolchain building happens
			errorExit(f"mingw build folder '{self.toolchain_output_path}' does not exist.")

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
# settings
# initialize logging (with default loglevel)
# process CMDLINE arguments
# reset logging after settings and arguments
# init and load products
# init and load dependencies
# init and load variables (the .py)
# ... etc


	# initialize system stuff
	PY_REQUIRE = (3, 8)
	if sys.version_info < PY_REQUIRE:
		sys.exit("You need at least Python %s.%s or later to run this script.\n" % PY_REQUIRE)
	sys.dont_write_bytecode = True  # Avoid __pycache__ folder, never liked that solution

	# initial settings, they can be overridden later by commandline options
	global_settings = settings()





	# initialize Logging
	logging_handler = logging.StreamHandler(sys.stdout)
	fmt = MyLogFormatter("[%(asctime)s][%(levelname)s]%(type)s %(message)s", "%H:%M:%S")
	logging_handler.setFormatter(fmt)
	logger = logging.getLogger(__name__)
	logger.addHandler(logging_handler)
	logger.setLevel(global_settings.initial_logging_mode)
	logger.debug(f'__main__: logger.setLevel is {global_settings.initial_logging_mode} ... (logging.INFO={logging.INFO} logging.DEBUG={logging.DEBUG})')
	?????????? self.config["script"]["log_format"]
	?????????? self.config["script"]["log_format"]
	?????????? fmt = MyLogFormatter(self.config["script"]["log_format"], self.config["script"]["log_date_format"])
	logging_handler.setFormatter(fmt)
	?????????? self.config["script"]["log_date_format"]
	


	#_epilog = 'Copyright (C) 2023-2024 hydra3333\n\n This Source Code Form is subject to the terms of the GNU General Public License version 3 or any later version. If a copy of the GPLv3 was not distributed with this file, You may obtain one at https://www.gnu.org/licenses/gpl-3.0.html'
	#parser = argparse.ArgumentParser(formatter_class=epiFormatter, epilog=_epilog)
