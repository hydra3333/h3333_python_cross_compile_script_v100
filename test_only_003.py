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
		global_dump_object_variables(self, heading)	# dump variables thr ordinary way
		#members = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
		#print(members)
		# we need to convert  vars(self).items() to a LIST, since dict does not allow duplicate keys
		#objPrettyPrint.pprint(vars(self))
		print(f"\nDEBUG: {heading} VARIABLES DUMPING IN ALPHABETIC NAME ORDER")
		c = sorted(vars(self).items(), key=lambda yvar: str(yvar[0]).lower() )
		choppy = 35
		for d,e in c:
			sd = str(d)
			L = min(choppy,len(sd))
			sd = sd[0:L]
			s = ' ' * (choppy-len(sd)+1)
			print(f"'{sd}'{s} = '{e}'")
		print(f"\n{len(c)} items IN ALPHABETIC NAME ORDER\n")
		del c
		print(f"\nDEBUG: {heading} VARIABLES DUMPING IN ALPHABETIC VALUE ORDER")
		f = sorted(vars(self).items(), key=lambda yvar: str(yvar[1]).lower() )
		choppy = 48
		for g,h in f:
			sh = str(h)
			m = max(0,choppy-len(sh)+1)
			s = ' '*m
			print(f"'{sh}'{s} = '{g}'")
		print(f"\n{len(f)} items ALPHABETIC VALUE ORDER\n")
		del f
		return

	def aquireLocalPkgConfigPath(self):	 	# this only works on linux
		possiblePathsStr = subprocess.check_output('pkg-config --variable pc_path pkg-config', shell=True, stderr=subprocess.STDOUT).decode("utf-8").strip()
		if possiblePathsStr == "":
			msg = f"Unable to determine local pkg-config path(s), pkg-config output is empty"
			logger.error(msg)
			raise Exception(msg)
		possiblePaths = [Path(x.strip()) for x in possiblePathsStr.split(":")]
		for p in possiblePaths:
			if not p.exists():
				possiblePaths.remove(p)
		if not len(possiblePaths):
			msg = F"Unable to determine local pkg-config path(s), pkg-config output is: {possiblePathsStr}"
			logger.error(msg)
			raise Exception(msg)
		return ":".join(str(x) for x in possiblePaths)

	def __init__(self):
		# NOTE:	here we fully flesh out all variables
		#		nothing is left with !CMDxxxCMD! or !VARxxxVAR! type stuff in it
		#		so, we do not rely on functions like replaceVariables or replaceVariables

		print(f"Processing initial settings")
		# _working and STATUS stuff first
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
		self.projectRoot = Path(os.getcwd())							# root folder for this script eg /home/u/Desktop/_working
		self.originalPATH = os.getenv("PATH") 							# the original environment search path before we add to it

		self.packages_subfolder = 'packages'							# 'packages' is the subfolder where the .py files reside
		self.patches_subfolder = 'patches'								# 'patches' is the subfolder where the patch files reside
		self.additionalheaders_subfolder = 'additional_headers'			# 'additional_headers' is where additional headers reside
		self.sources_subfolder = 'sources'								# 'sources' is where some sources reside
		self.tools_subfolder = 'tools'									# 'tools' is where some tools reside
		
		self.workdir_subfolder ='workdir'											# 'workdir'  is the subfolder where actual build stuff happens
		self.fullWorkDir    = self.projectRoot.joinpath(self.workdir_subfolder)		# for output, eg workdir

		self.bitnessStr = "x86_64"										# eg x86_64 underneath workdir_subfolder
		self.bitnessStr2 = "x86_64"										# just for vpx... underneath workdir_subfolder
		self.bitnessStr3 = "mingw64"									# just for openssl... underneath workdir_subfolder
		self.targetOSStr = "mingw64"									# 2019.12.13 just for "--target-os=" 
		self.bitnessStrWin = "win64"									# eg 'win64'

		self.targetHostStr       = F"{self.bitnessStr}-w64-mingw32"  	# eg x86_64-w64-mingw32

		self.original_cflag					= '-O3'
		self.original_stack_protector		= '-fstack-protector-all'
		self.original_fortify_source		= '-D_FORTIFY_SOURCE=2'

		self.original_cflag_trim			= self.original_cflag.strip()
		self.original_stack_protector_trim	= self.original_stack_protector.strip()
		self.original_fortify_source_trim	= self.original_fortify_source.strip()

		self.original_Cflags				= f'  {self.original_cflag_trim}  {self.original_stack_protector_trim}  {self.original_fortify_source_trim}  '	# was originalCflags, let's see what breaks
		self.original_Cflags_trim			= self.original_Cflags.strip()

		self.originalCflag					= self.original_cflag				# duplicates which are referenced, cull later
		self.originalCflag_trim				= self.originalCflag.strip()		# duplicates which are referenced, cull later
		self.originalCflags					= self.original_Cflags				# duplicates which are referenced, cull later
		self.originalCflags_trim			= self.originalCflags.strip()		# duplicates which are referenced, cull later

		self.toolchain_mingw_subfolder = 'toolchain'					# for output, eg 'toolchain' underneath self.workdir_subfolder, is the same as deadsix27 'mingwDir'
		self.toolchain_mingwDir = self.fullWorkDir.joinpath(self.toolchain_mingw_subfolder)	# fully qualified path to where it gets built into
		self.mingwDir = self.toolchain_mingwDir	# where ming64 gets built into
		self.toolchain_mingw_toolchain_script_subfolder = "mingw_toolchain_script"
		self.toolchain_mingw_toolchain_script_name = 'mingw_toolchain_script_v100_002_like_zeranoe.py'
		self.mingw_toolchain_script_folder = self.projectRoot.joinpath(self.toolchain_mingw_toolchain_script_subfolder)
		self.mingw_toolchain_script_path = self.mingw_toolchain_script_folder.joinpath(self.toolchain_mingw_toolchain_script_name)
		self.toolchain_mingw_script_relative_path = f"{self.toolchain_mingw_toolchain_script_subfolder}/{self.toolchain_mingw_toolchain_script_name}"
		#self.toolchain_mingw_debug_build = False		#
		#self.toolchain_mingw_commit = None				# specify a custom mingW64 commit, or None which leaves that up to the toolchain builder
		#self.toolchain_mingw_custom_cflags = None		#
		
		#self.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'		# old
		self.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'		# LTS as at 2023.02.07
		#self.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'	# as at 2023.02.07
		
		self.log_format = '[%(asctime)s][%(levelname)s]%(type)s %(message)s'
		self.log_date_format = '%H:%M:%S'

		# mainly calculated variables next

		self.mesonEnvFile = self.fullWorkDir.joinpath("meson_environment.txt")			# used when building packages
		self.cmakeToolchainFile = self.fullWorkDir.joinpath("mingw_toolchain.cmake")	# used when building packages

		self.packagesFolder = self.projectRoot.joinpath(self.packages_subfolder)	# for input, eg packages
		self.prodFolder     = self.packagesFolder.joinpath("products")					# for input, eg packages/products
		self.depsFolder     = self.packagesFolder.joinpath("dependencies")				# for input, eg packages/dependencies
		self.varsPath       = self.packagesFolder.joinpath("variables.py")				# for input, eg packages/variables.py
		self.patchesFolder	= self.projectRoot.joinpath(self.patches_subfolder)			# for input, eg packages
		self.additionalheadersFolder	= self.projectRoot.joinpath(self.additionalheaders_subfolder)			# for input, eg packages
		self.sourcesFolder	= self.projectRoot.joinpath(self.sources_subfolder)			# for input, eg packages
		self.toolsFolder	= self.projectRoot.joinpath(self.tools_subfolder)			# for input, eg packages

		self.bitnessPath = self.fullWorkDir.joinpath(self.bitnessStr)					# for output, eg workdir/x86_64
		self.fullProductDir = self.bitnessPath.joinpath('_products')					# for output, eg workdir/x86_64_products
		self.fullOfftreeDir = self.bitnessPath.joinpath('_offtree')						# for output, eg workdir/x86_64_offtree
		self.fullDependencyDir = self.bitnessPath.joinpath('')							# to be compatible with deadsix27, rather than use a new 'x86_64_dependencies'

		# toolchain_output_path is the same as deadsix27 fullOutputDir
		self.toolchain_output_path = self.fullWorkDir.joinpath(self.bitnessStrWin + "_output")	# eg workdir/win64_output
		# toolchain_output_path is the same as deadsix27 fullOutputDir
		self.fullOutputDir = self.toolchain_output_path									# duplicated, cull later

		self.mingwpath     = self.fullWorkDir.joinpath(self.toolchain_mingw_subfolder, self.bitnessStr + "-w64-mingw32") 	# eg workdir/toolchain/x86_64-w64-mingw32
		self.targetPrefix  = self.mingwpath.joinpath(self.bitnessStr + "-w64-mingw32") 										# eg workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32
		self.inTreePrefix  = self.bitnessPath													 							# eg workdir/x86_64
		self.targetSubPrefix = self.mingwpath																				# eg workdir/toolchain/x86_64-w64-mingw32
		self.offtreePrefix = self.fullOfftreeDir																			# eg workdir/x86_64_offtree
		self.mingwBinpath  = self.mingwpath.joinpath("bin")  																# eg workdir/toolchain/x86_64-w64-mingw32/bin
		self.mingwBinpath2 = self.mingwpath.joinpath(self.bitnessStr + "-w64-mingw32", "bin")								# eg workdir/toolchain/x86_64-w64-mingw32/x86_64-w64-mingw32/bin

		self.shortCrossPrefixStr = F"{self.bitnessStr}-w64-mingw32-"														# eg x86_64-w64-mingw32-
		self.fullCrossPrefixStr = self.mingwBinpath.joinpath(self.shortCrossPrefixStr)										# eg workdir/toolchain/x86_64-w64-mingw32/bin/x86_64-w64-mingw32-
		self.autoConfPrefixOptions = F'--with-sysroot="{self.targetSubPrefix}" --host={self.targetHostStr} --prefix={self.targetPrefix} --disable-shared --enable-static'
		self.makePrefixOptions = F'CC={self.shortCrossPrefixStr}gcc ' \
			F"AR={self.shortCrossPrefixStr}ar " \
			F"PREFIX={self.targetPrefix} " \
			F"RANLIB={self.shortCrossPrefixStr}ranlib " \
			F"LD={self.shortCrossPrefixStr}ld " \
			F"STRIP={self.shortCrossPrefixStr}strip " \
			F'CXX={self.shortCrossPrefixStr}g++'  # --sysroot="{self.targetSubPrefix}"'
		self.pkgConfigPath = f"{self.targetPrefix}/lib/pkgconfig"
		self.localPkgConfigPath = self.aquireLocalPkgConfigPath()	# this only works on linux								# eg /usr/local/lib/pkgconfig:/usr/lib/x86_64-linux-gnu/pkgconfig:/usr/lib/pkgconfig:/usr/share/pkgconfig
		self.cmakePrefixOptions = F'-DCMAKE_TOOLCHAIN_FILE="{self.cmakeToolchainFile}" -G\"Ninja\"'
		self.cmakePrefixOptionsOld = "-G\"Unix Makefiles\" -DCMAKE_SYSTEM_PROCESSOR=\"{bitness}\" -DCMAKE_SYSTEM_NAME=Windows -DCMAKE_RANLIB={cross_prefix_full}ranlib -DCMAKE_C_COMPILER={cross_prefix_full}gcc -DCMAKE_CXX_COMPILER={cross_prefix_full}g++ -DCMAKE_RC_COMPILER={cross_prefix_full}windres -DCMAKE_FIND_ROOT_PATH={target_prefix}".format(cross_prefix_full=self.fullCrossPrefixStr, target_prefix=self.targetPrefix, bitness=self.bitnessStr)
		self.cpuCount = self.cpu_count		# ??? WHY HAVE 2 VARIABLES FOR THE SAME THING ???
		self.originalLdLibPath = os.environ["LD_LIBRARY_PATH"] if "LD_LIBRARY_PATH" in os.environ else ""

		# define the name of tghe gcc compiler
		self.gcc_bin = os.path.join(self.mingwBinpath, self.bitnessStr + "-w64-mingw32-gcc")

		self.formatDict = defaultdict(lambda: "")
		self.formatDict.update(
			{
				'output_prefix': str(self.fullOutputDir),
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
				'bit_num': self.bitness,
				'product_prefix': self.fullProductDir,
				'target_prefix_sed_escaped': str(self.targetPrefix).replace("/", "\\/"),
				'make_cpu_count': "-j {0}".format(self.cpuCount),
				'original_cflags': self.originalCflags,
				'cflag_string': generateCflagString('--extra-cflags='),
				'current_path': os.getcwd(),
				'current_envpath': getKeyOrBlankString(os.environ, "PATH"),
				'meson_env_file': self.mesonEnvFile,
				#
				'target_OS': self.targetOSStr,
				'prefix' : "{prefix}", # 2018.11.23 added a dummy variable replaced with itself, use in editing vapoursynth .pc files
				'exec_prefix' : "{exec_prefix}", # 2018.11.23 added a dummy variable replaced with itself, use in editing vapoursynth .pc files
				'original_cflags': self.originalCflags_trim,
				'original_cflags_trim': self.originalCflags_trim,
				'original_stack_protector' : self.original_stack_protector,
				'original_stack_protector_trim' : self.original_stack_protector_trim,
				'original_fortify_source' : self.original_fortify_source,
				'original_fortify_source_trim' : self.original_fortify_source_trim,
				'original_cflag': self.originalCflag,				# a duplicate, cull later
				'original_cflag_trim': self.originalCflag_trim,		# a duplicate, cull later
			}
		)
		self.string_replacements_Dict = self.formatDict	# migrate to using this

		#
		# The next bit is formatting self.config into itself using 'self.formatDict' as the source of key/value replacements
		#
		#self.config = self.formatConfig(self.config) 
		#def formatConfig(self, c: dict):
		#	def fmt(d):
		#		if isinstance(d, dict):
		#			return {self.replaceToolChainVars(k): fmt(v) for k, v in d.items()}
		#		elif isinstance(d, list):
		#			return [fmt(o) for o in d]
		#		else:
		#			if isinstance(d, str):
		#				return self.replaceToolChainVars(d)
		#			else:
		#				return d
		#	try:
		#		return fmt(c)
		#	except KeyError as e:
		#self.errorExit(F"Failed to parse config file, the variable {e} does not exist.")
		#
		# HOWEVER ...
		# we do not used saved configs any more
		# since they interfered when making changes to this script and the changes appearing not to work
		# SO ... we ignore and no longer do saved config stuff
		#
		
		os.environ["PATH"] = f"{self.mingwBinpath}:{self.originalPATH}"
		os.environ["PKG_CONFIG_PATH"] = self.pkgConfigPath
		os.environ["PKG_CONFIG_LIBDIR"] = ""
		os.environ["COLOR"] = "ON"  # Force coloring on (for CMake primarily)
		os.environ["CLICOLOR_FORCE"] = "ON"  # Force coloring on (for CMake primarily)

		print(f"Processing finished Processing initial settings")
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
		
	def __init__(self, name=None):
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
		logger.info(f"Processing 'load_py_file' for {heading}")
		if not os.path.isfile(file):
			self.errorExit(f"dot_py_object({self.name}): load_py_file: variables File '{file}' does not exist.")
		with open(file, "r", encoding="utf-8") as f:
			p = Path(file)
			packageName = p.stem.lower()	# this will become the "name" field in the object
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
						self.set_data_py(name=self.name, Val=objJSON)	##### SEE THIS #####
						logger.debug(f"load_py_file: dot_py_object({self.name}): {heading} variables File '{packageName}.py' loaded")
			except SyntaxError:
				self.errorExit(f"load_py_file: dot_py_object({self.name}): Loading {heading} variables File '{packageName}' failed:\n\n{traceback.format_exc()}")
		
		logger.info(f"Finished Processing 'load_py_file' for variables from {packageName} into {heading} object named {self.name}")
		logger.info(f"Loaded {len(self.Val)} variables into {heading} object named {self.name}")
		return
		
	def list_print(self, heading=''):
		logger.info(f"Processing 'list' commandline actions for object {heading}")
		print(f"")
		print(f"LIST: {heading}: {len(self.Val.items())} items.\n")
		for key, val in self.Val.items():
			pkey = key.ljust(32,' ')
			print(f" {Colors.GREEN}{pkey}{Colors.RESET} ... '{val}'")
		logger.info(f"Finished Processing 'list' commandline actions for object {heading}")
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
		logger.info(f"Processing 'load_py_files' for dictionary {heading}")
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
		logger.info(f"Finished Processing 'load_py_files' for dictionary {heading}")
		logger.info(f"Loaded {len(self.BO)} {heading} files into dictionary {self.name}")
		return

	def list_print(self, heading=''):
		logger.info(f"Processing 'list' commandline actions for dictionary {heading}")
		print(f"")
		print(f"LIST: {heading}: {len(self.BO.items())} items.\n")
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
		logger.info(f"Finished Processing 'list' commandline actions for dictionary {heading}")
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
		logger.info(f"Processing CommandLine arguments")
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

		logger.info(f"Finished Processing CommandLine arguments")
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

	logger.info(f"Processing 'info' 'required_by' ... what packages tree is required_by package {packageName}")
	logger.debug(f"info_print_required_by: Entered with packageName='{packageName}'")
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
	logger.info(f"Finished Processing 'info' 'required_by' ... what packages tree is required_by package {packageName}")
	logger.debug(f"info_print_required_by: exiting with packageName='{packageName}'")

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

	logger.info(f"Processing 'info' 'depends_on' ... what package tree depends_on package {packageName}")
	logger.debug(f"info_print_depends_on: Entered with packageName='{packageName}'")
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
	logger.info(f"Finished Processing 'info' 'depends_on' ... what package tree depends_on package {packageName}")
	logger.debug(f"info_print_depends_on: exiting with packageName='{packageName}'")

###################################################################################################

def prepareForBuilding():
	logger.info(f"Processing prepareForBuilding. This script and .py files SHOULD be in projectRoot='{objSETTINGS.projectRoot}'")

	# The projectRoot is the current folder (where this script SHOULD reside)
	# Create the "workdir" subfolder under the projectRoot  if it doesn't already exist and then CD into it
	if objSETTINGS.fullWorkDir.exists():
		logger.info(f"Existing workdir: '{objSETTINGS.fullWorkDir}' found, no need to create it")
	else:
		logger.info(f"Creating workdir: '{objSETTINGS.fullWorkDir}'")
		objSETTINGS.fullWorkDir.mkdir()
	# cd into the "workdir" subfolder underneath fullWorkDir, where all the build action happens eg workdir
	cchdir(objSETTINGS.fullWorkDir)

	# Don't create these folders here as they are instead created during the mingW build process
	#	objSETTINGS.mingwBinpath		# eg workdir/xcompilers/x86_64-w64-mingw32/bin
	#	objSETTINGS.mingwBinpath2		# eg workdir/xcompilers/x86_64-w64-mingw32/x86_64-w64-mingw32/bin
	#	objSETTINGS.targetPrefix		# eg workdir/xcompilers/mingW64-x86_64/x86_64-w64-mingw32

	if not objSETTINGS.bitnessPath.exists():										# where dependenciess etc get built eg workdir/x86_64
		logger.info(f"Creating bitnessPath: '{objSETTINGS.bitnessPath}' # where dependenciess etc get built eg workdir/x86_64")
		objSETTINGS.bitnessPath.mkdir(exist_ok=True)
	if not os.path.isdir(objSETTINGS.fullDependencyDir):	# = bitnessPath, supersedes bitnessPath
		logger.info(f"Creating fullDependencyDir: '{objSETTINGS.fullDependencyDir}' # where dependenciess etc get built eg workdir/x86_64")
		objSETTINGS.fullDependencyDir.mkdir(exist_ok=True)
	if not objSETTINGS.fullProductDir.exists():										# where products etc get built eg workdir/x86_64_products
		logger.info(f"Creating fullProductDir: '{objSETTINGS.fullProductDir}' # where products etc get built eg workdir/x86_64_products")
		objSETTINGS.fullProductDir.mkdir(exist_ok=True)
	if not objSETTINGS.offtreePrefix.exists():										# where off-tree dependencies get built eg workdir/x86_64_offtree
		logger.info(f"Creating offtreePrefix: '{objSETTINGS.offtreePrefix}' # where offtree stuff etc get built eg # eg workdir/x86_64_offtree")
		objSETTINGS.offtreePrefix.mkdir(exist_ok=True)
	# objSETTINGS.fullOutputDir superseded by objSETTINGS.toolchain_output_path
	if not objSETTINGS.toolchain_output_path.exists():								# not sure what the heck goes here, possibly ming64 buildsin stuff ??? eg workdir/win64_output
		logger.info(f"Creating toolchain_output_path: '{objSETTINGS.toolchain_output_path}' # possibly ?? where mingw64 toolchain build stuff temporarily goes")
		objSETTINGS.toolchain_output_path.mkdir(exist_ok=True)

	# check some folders exist
	if not os.path.isdir(objSETTINGS.mingw_toolchain_script_folder):						# the subfolder where the toolchain build script resides
		objSETTINGS.errorExit(f"mingw build script folder '{objSETTINGS.mingw_toolchain_script_folder}' does not exist.")
	if not os.path.isfile(objSETTINGS.mingw_toolchain_script_path):						# the full path to the toolchain build script
		objSETTINGS.errorExit(f"mingw build script file '{objSETTINGS.mingw_toolchain_script_path}' does not exist." )

	# Always RE-create the toolchain build file for meson every time, in case  we have changed something
	#if not os.path.isfile(objSETTINGS.mesonEnvFile):
	if True:
		logger.debug(f"Creating Meson Environment file: '{objSETTINGS.mesonEnvFile}'")
		meFile = (
			"[binaries]\n",
			F"c = '{objSETTINGS.shortCrossPrefixStr}gcc'",
			F"cpp = '{objSETTINGS.shortCrossPrefixStr}g++'",
			F"ld = 'bfd'", # 2020.03.19 See: https://github.com/mesonbuild/meson/issues/6431#issuecomment-572544268, no clue either why we can't just define full "ld" path
			#F"ld = '{objSETTINGS.shortCrossPrefixStr}ld'", # 2020.03.19 re-commented-out
			F"ar = '{objSETTINGS.shortCrossPrefixStr}ar'",
			F"strip = '{objSETTINGS.shortCrossPrefixStr}strip'",
			F"windres = '{objSETTINGS.shortCrossPrefixStr}windres'",
			F"ranlib = '{objSETTINGS.shortCrossPrefixStr}ranlib'",
			"pkgconfig = 'pkg-config'",
			F"dlltool = '{objSETTINGS.shortCrossPrefixStr}dlltool'",
			F"gendef = '{objSETTINGS.mingwBinpath}/gendef'",
			"cmake = 'cmake'",
			"#needs_exe_wrapper = false",
			"#exe_wrapper = 'wine' # A command used to run generated executables.",
			"",
			"[host_machine]",
			"system = 'windows'",
			F"cpu_family = '{objSETTINGS.bitnessStr}'",
			F"cpu = '{objSETTINGS.bitnessStr}'",
			"endian = 'little'",
			"",
			"[target_machine]",
			"system = 'windows'",
			F"cpu_family = '{objSETTINGS.bitnessStr}'",
			F"cpu = '{objSETTINGS.bitnessStr}'",
			"endian = 'little'",
			"",
			"[properties]",
			"# sys_root = Directory that contains 'bin', 'lib', etc for the toolchain and system libraries",
			#F"sys_root = '{objSETTINGS.targetSubPrefix}'" # 2022.12.18 per DEADSIX27
			"",
			"[built-in options]",
			"# 2022.09.26 meson warning says to move the below into here when using a later version of meson",
			"c_link_args = ['-static', '-static-libgcc']"
		)
		with open(objSETTINGS.mesonEnvFile, 'w') as f:
			f.write("\n".join(meFile))
			f.write("\n")
	else:
		logger.debug(f"Using existing Meson Environment file: '{objSETTINGS.mesonEnvFile}'")
	logger.debug(f"'{objSETTINGS.mesonEnvFile}' contains:")
	cmd = f"cat {objSETTINGS.mesonEnvFile}"
	ret, result = runProcess(cmd, ignoreErrors=True, yield_return_code=True)
	if ret == 0:
		logger.debug(f"command: '{cmd}' return_code: '{ret}'")	# RESULT:\n{result}
	else:
		logger.info(f"command failed: '{cmd}' return_code: '{ret}' RESULT:\n{result}")
		#print(f"?????????? temporarily continue, for initial debugging on windows ??????????")
		exit(ret) # comment-out temporarily continue ?????????? temporarily continue, for initial debugging on windows ??????????

	# Always RE-create the toolchain build file for cmake every time, in case  we have changed something
	#if not os.path.isfile(objSETTINGS.cmakeToolchainFile):
	if True:
		logger.info(f"Creating CMake Toolchain file: '{objSETTINGS.cmakeToolchainFile}'")
		cmFile = [
			F'set(CMAKE_SYSTEM_NAME Windows)',
			F'set(CMAKE_SYSTEM_PROCESSOR {objSETTINGS.bitnessStr})',
			#F'set(CMAKE_SYSROOT {objSETTINGS.targetSubPrefix})', # 2022.12.18 per DEADSIX27
			#F'set(CMAKE_STAGING_PREFIX /home/devel/stage)',
			F'set(CMAKE_RANLIB {objSETTINGS.shortCrossPrefixStr}ranlib)',
			F'set(CMAKE_C_COMPILER {objSETTINGS.shortCrossPrefixStr}gcc)',
			F'set(CMAKE_CXX_COMPILER {objSETTINGS.shortCrossPrefixStr}g++)',
			F'set(CMAKE_RC_COMPILER {objSETTINGS.shortCrossPrefixStr}windres)',
			F'set(CMAKE_ASM_COMPILER {objSETTINGS.mingwBinpath}/{objSETTINGS.shortCrossPrefixStr}as)',
			#F'set(CMAKE_FIND_ROOT_PATH {objSETTINGS.targetPrefix})', # 2022.12.18 per DEADSIX27
			F'set(CMAKE_FIND_ROOT_PATH {objSETTINGS.targetPrefix}/)', # 2022.12.18 per DEADSIX27
			F'set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)',
			F'set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)',
			F'set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)',
			F'set(CMAKE_FIND_ROOT_PATH_MODE_PACKAGE ONLY)',
			# for shaderc
			F'set(MINGW_COMPILER_PREFIX {objSETTINGS.shortCrossPrefixStr})',
			#F'set(MINGW_SYSROOT {objSETTINGS.targetSubPrefix})'  # 2022.12.18 per DEADSIX27
		]
		with open(objSETTINGS.cmakeToolchainFile, 'w') as f:
			f.write("\n".join(cmFile))
			f.write("\n")
	else:
		logger.debug(f"Using existing CMake Toolchain file: '{objSETTINGS.cmakeToolchainFile}'")
	logger.debug(f"'{objSETTINGS.cmakeToolchainFile}' contains:")
	cmd = f"cat {objSETTINGS.cmakeToolchainFile}"
	ret, result = runProcess(cmd, ignoreErrors=True, yield_return_code=True)
	if ret == 0:
		logger.debug(f"command: '{cmd}' return_code: '{ret}'")	# RESULT:\n{result}
	else:
		logger.info(f"command failed: '{cmd}' return_code: '{ret}' RESULT:\n{result}")
		#print(f"?????????? temporarily continue, for initial debugging on windows ??????????")
		exit(ret) # comment-out temporarily continue ?????????? temporarily continue, for initial debugging on windows ??????????

	logger.info(f"Finished Processing prepareForBuilding.")

###################################################################################################
def buildMingw64():
	# build mingw64 and the compilers etc.
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

	logger.info(f"Processing buildMingw64")
	cchdir(objSETTINGS.fullWorkDir)	
	gcc_bin = objSETTINGS.gcc_bin
	if os.path.isfile(gcc_bin):
		gccOutput = subprocess.check_output(gcc_bin + " -v", shell=True, stderr=subprocess.STDOUT).decode("utf-8")
		workingGcc = re.compile("^Target: .*-w64-mingw32$", re.MULTILINE).findall(gccOutput)
		if len(workingGcc) > 0:
			logger.info(f"NEW mingW64 GCC install is working ! (target: {objSETTINGS.targetOSStr})")
			logger.info(f"Exiting buildMingw64 since mingW64 GCC already exists and appears to be working")
			return
		else:
			logger.error(f"mingW64 GCC already exists HOWEVER appears to be NOT WORKING (target: {objSETTINGS.targetOSStr}) ({gcc_bin})")
			raise Exception(f"Existing mingW64 GCC is not working properly (target: {objSETTINGS.targetOSStr}) ({gcc_bin})")
			sys.exit(1)
	elif not os.path.isdir(objSETTINGS.mingwDir):
		logger.info(f"Building mingW64 in folder '{objSETTINGS.mingwDir}'")
		os.unsetenv("CFLAGS")								# unset any existing CFLAGS environment variable
		os.makedirs(objSETTINGS.mingwDir, exist_ok=True)	# make the target build folder
		# import may not work with full path, try relative path instead
		#module_path = str(objSETTINGS.mingw_toolchain_script_path).replace("/", ".")
		#module_path = module_path.rstrip(".py")
		module_path = str(objSETTINGS.toolchain_mingw_script_relative_path).replace("/", ".")
		module_path = module_path.rstrip(".py")
		if not os.path.isfile(objSETTINGS.mingw_toolchain_script_path):
			errorExit(f"Specified MinGW64 build script path does not exist: '{module_path}'")
			sys.exit(1)
		logger.debug(f"                       current working directory = '{os.getcwd()}'")
		logger.debug(f"         objSETTINGS.mingw_toolchain_script_path = '{objSETTINGS.mingw_toolchain_script_path}'")
		logger.debug(f"objSETTINGS.toolchain_mingw_script_relative_path = '{objSETTINGS.toolchain_mingw_script_relative_path}'")
		logger.debug(f"                          calculated module path = '{module_path}'")
		logger.debug(f"About to try-except 'importlib.import_module(module_path)'")
		try:
			mod = importlib.import_module(module_path)
			logger.debug(f"Successfully imported module '{module_path}' from '{objSETTINGS.toolchain_mingw_script_relative_path}'")
		except:
			errorExit(f"Could not import module MinGW64 build script path does not exist: '{module_path}'")
			sys.exit(1)
		# instantiate class MinGW64ToolChainBuilder from the newly imported module
		toolchainBuilder = mod.MinGW64ToolChainBuilder()
		toolchainBuilder.workDir = objSETTINGS.mingwDir
		# we no longer specify a mingW64 commit here - do it in the module instead to eliminate ambiguity
		#	toolchainBuilder.setMinGWcheckout(some_commit)
		# we no longer specify mingw_custom_cflags here - do it in the module instead to eliminate ambiguity
		#	toolchainBuilder.setCustomCflags(some_mingw_custom_cflags)
		# we no longer specify mingW64 debug build here - do it in the module instead to eliminate ambiguity
		#	toolchainBuilder.setDebugBuild(False)
		def toolchainBuildStatus(logMessage):	# define a function to add to the onStatusUpdate event
			logger.info(logMessage)
		toolchainBuilder.onStatusUpdate += toolchainBuildStatus	# display things the toolchain writes

		# Invoke the newly imported module class method to build mingW64
		logger.debug(f"Invoking newly imported module toolchainBuilder.build() to build mingW64")
		toolchainBuilder.build()
		logger.debug(f"Returned from newly imported module toolchainBuilder.build()")
		# test our shiny new mingW64 build
		logger.debug(f"Testing NEW  mingW64 GCC :")
		if os.path.isfile(gcc_bin):
			gccOutput = subprocess.check_output(gcc_bin + " -v", shell=True, stderr=subprocess.STDOUT).decode("utf-8")
			workingGcc = re.compile("^Target: .*-w64-mingw32$", re.MULTILINE).findall(gccOutput)
			if len(workingGcc) > 0:
				logger.info(f"NEW  mingW64 GCC install is working ! (target: {objSETTINGS.targetOSStr})")
			else:
				logger.error(f"NEW mingW64 GCC exists HOWEVER appears to be NOT WORKING (target: {objSETTINGS.targetOSStr}) ({gcc_bin})")
				raise Exception(f"NEW mingW64 GCC is not working properly (target: {objSETTINGS.targetOSStr}) ({gcc_bin})")
				sys.exit(1)
		else: 
			logger.error(f"NEW mingW64 GCC  exists HOWEVER appears to be NOT WORKING (target: {objSETTINGS.targetOSStr}) ({gcc_bin})")
			raise Exception(f"NEW mingW64 GCC is not working properly (target: {objSETTINGS.targetOSStr}) ({gcc_bin})")
			sys.exit(1)
		logger.info(f"Finished Processing buildMingw64")
		cchdir(objSETTINGS.fullWorkDir)
		return
	else:
		errorExit(f"It looks like the MinGW64 build failed, please delete the folder '{objSETTINGS.mingwDir}' and re-run this script")
		sys.exit(1)
	
	errorExit(f"buildMingw64 shouod never get to here. MinGW64 build failed, please delete the folder '{objSETTINGS.mingwDir}' and re-run this script")
	sys.exit(1)

def generateCflagString(prefix=""):
	if "CFLAGS" not in os.environ:
		return ""
	cfs = os.environ["CFLAGS"]
	cfs = cfs.split(' ')
	if (len(cfs) == 1 and cfs[0] != "") or not len(cfs):
		return ""
	out = ''
	if len(cfs) >= 1:
		for c in cfs:
			out += prefix + c + ' '
		out.rstrip(' ')
		return out
	return ''

def getKeyOrBlankString(db, k):
	if k in db:
		if db[k] is None:
			return ""
		else:
			return db[k]
	else:
		return ""

def zzz_downloadHeader(self, url):
	destination = self.targetPrefix.joinpath("include")
	fileName = os.path.basename(urlparse(url).path)
	if not os.path.isfile(os.path.join(destination, fileName)):
		fname = self.downloadFile(url)
		self.logger.debug("Moving Header File: '{0}' to '{1}'".format(fname, destination))
		shutil.move(fname, destination)
	else:
		self.logger.debug("Header File: '{0}' already downloaded".format(fileName))

def zzz_downloadFile(self, url=None, outputFileName=None, outputPath=None, bytesMode=False):
	def fmt_size(num, suffix="B"):
			for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
				if abs(num) < 1024.0:
					return "%3.1f%s%s" % (num, unit, suffix)
				num /= 1024.0
			return "%.1f%s%s" % (num, "Yi", suffix)
	
	if not url:
		raise Exception("No URL specified.")

	if outputPath is None:  # Default to current dir.
		outputPath = os.getcwd()
	else:
		if not os.path.isdir(outputPath):
			raise Exception('Specified path "{0}" does not exist'.format(outputPath))

	fileName = os.path.basename(url)  # Get URL filename
	userAgent = self.userAgent

	if 'sourceforge.net' in url.lower():
		userAgent = 'wget/1.18'  # sourceforce <3 wget

	if url.lower().startswith("ftp://"):
		self.logger.info("Requesting : {0}".format(url))
		if outputFileName is not None:
			fileName = outputFileName
		fullOutputPath = os.path.join(outputPath, fileName)
		urllib.request.urlretrieve(url, fullOutputPath)
		return fullOutputPath

	if url.lower().startswith("file://"):
		url = url.replace("file://", "")
		self.logger.info("Copying : {0}".format(url))
		if outputFileName is not None:
			fileName = outputFileName
		fullOutputPath = os.path.join(outputPath, fileName)
		try:
			self.logger.debug('cp -f "{0}" "{1}" # copy file '.format(url, fullOutputPath))
			shutil.copyfile(url, fullOutputPath)
		except Exception as e:
			print(e)
			exit(1)
		return fullOutputPath

	req = requests.get(url, stream=True, headers={"User-Agent": userAgent}) # , verify=False to turn off certificate validation

	if req.status_code != 200:
		req.raise_for_status()

	if "content-disposition" in req.headers:
		reSponse = re.findall("filename=(.+)", req.headers["content-disposition"])
		if reSponse is None:
			fileName = os.path.basename(url)
		else:
			fileName = reSponse[0]

	size = None
	compressed = False
	if "Content-Length" in req.headers:
		size = int(req.headers["Content-Length"])

	if "Content-Encoding" in req.headers:
		if req.headers["Content-Encoding"] == "gzip":
			compressed = True

	self.logger.info("Requesting : {0} - {1}".format(url, fmt_size(size) if size is not None else "?"))

	# terms = shutil.get_terminal_size((100,100))
	# filler = 0
	# if terms[0] > 100:
	# 	filler = int(terms[0]/4)

	widgetsNoSize = [
		progressbar.FormatCustomText("Downloading: {:25.25}".format(os.path.basename(fileName))), " ",
		progressbar.AnimatedMarker(markers='|/-\\'), " ",
		progressbar.DataSize()
		# " "*filler
	]
	widgets = [
		progressbar.FormatCustomText("Downloading: {:25.25}".format(os.path.basename(fileName))), " ",
		progressbar.Percentage(), " ",
		progressbar.Bar(fill=chr(9617), marker=chr(9608), left="[", right="]"), " ",
		progressbar.DataSize(), "/", progressbar.DataSize(variable="max_value"), " |",
		progressbar.AdaptiveTransferSpeed(), " | ",
		progressbar.ETA(),
		# " "*filler
	]
	pbar = None
	if size is None:
		pbar = progressbar.ProgressBar(widgets=widgetsNoSize, maxval=progressbar.UnknownLength)
	else:
		pbar = progressbar.ProgressBar(widgets=widgets, maxval=size)

	if outputFileName is not None:
		fileName = outputFileName
	fullOutputPath = os.path.join(outputPath, fileName)

	updateSize = 0

	if isinstance(pbar.max_value, int):
		updateSize = pbar.max_value if pbar.max_value < 1024 else 1024

	if bytesMode is True:
		output = b""
		bytesrecv = 0
		pbar.start()
		for buffer in req.iter_content(chunk_size=1024):
			if buffer:
				output += buffer
			if compressed:
				pbar.update(updateSize)
			else:
				pbar.update(bytesrecv)
			bytesrecv += len(buffer)
		pbar.finish()
		return output
	else:
		with open(fullOutputPath, "wb") as file:
			bytesrecv = 0
			pbar.start()
			for buffer in req.iter_content(chunk_size=1024):
				if buffer:
					file.write(buffer)
					file.flush()
				if compressed:
					pbar.update(updateSize)
				else:
					pbar.update(bytesrecv)
				bytesrecv += len(buffer)
			pbar.finish()

			return fullOutputPath















	return

###################################################################################################
def errorExit(msg):
	logger.error(msg)
	sys.exit(1)

###################################################################################################
def cchdir(dir):
	logger.debug(f"cd {dir} # Change dir from '{os.getcwd()}' to '{dir}'")
	os.chdir(dir)


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
def reStrip(pat, txt):
	x = re.sub(pat, '', txt)
	return re.sub(r'[ ]+', ' ', x).strip()

###################################################################################################
def runProcess(command, ignoreErrors=False, exitOnError=True, silent=False, yield_return_code=False):
	# run a shell type command and retutn a bufffer contaning sanitized stdout results
	isSvn = False
	if not isinstance(command, str):
		command = " ".join(command)  # could fail I guess
	if command.lower().startswith("svn"):
		isSvn = True
	logger.debug(f"Running '{command}' in '{os.getcwd()}'")
	process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
	buffer = ""
	while True:
		nextline = process.stdout.readline()
		if nextline == b'' and process.poll() is not None:
			break
		buffer += nextline.decode("utf-8", "ignore")
		if isSvn:
			if not nextline.decode('utf-8').startswith('A	'):
				if not silent:
					sys.stdout.write(nextline.decode('utf-8', 'replace'))
					sys.stdout.flush()
		else:
			if not silent:
				sys.stdout.write(nextline.decode('utf-8', 'replace'))
				sys.stdout.flush()
	return_code = process.returncode
	process.communicate()[0]
	process.wait()
	if (return_code == 0):
		if yield_return_code:
			return return_code, buffer
		else:
			return buffer
	else:
		if ignoreErrors:
			if yield_return_code:
				return return_code, buffer
			else:
				return buffer
		logger.error(f"Error [{return_code}] running process: '{command}' in '{os.getcwd()}'")
		logger.error(f"You can try deleting the product/dependency folder: '{os.getcwd()}' and re-run the script")
		if exitOnError:
			exit(1)

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
		objSETTINGS.dump_vars('### debugMode: DEBUG SETTINGS INTERNAL VARIABLES DUMP:')
	
	# Initialize Logging, this depends on objSETTINGS being initialized first
	initLogger()

	# Initialize DEBUG mode ... do it ONLY ONLY AFTER initLogger() since that sets the initial loglevel inside the logger
	setDebugMode(objSETTINGS.debugMode)

	# Process CMDLINE arguments into variables in the processCmdLineArguments object
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
	logger.info(f"Processing initialize and load products")
	dictProducts = dot_py_object_dict(name='PRODUCTS')	# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for PRODUCTS only, of class dot_py_object_dict
	products_folder_to_parse = objSETTINGS.prodFolder	# for input, eg packages/products
	dictProducts.load_py_files(folder=products_folder_to_parse, heading='Product')
	#dictProducts.dump_vars(heading='PRODUCT VARIABLES DUMP:')
	logger.info(f"Finished Processing initialize and load products")

	# Initialize and load dependencies - note the use of a fixed text string type="D" to identify it as a dependencies
	logger.info(f"Processing initialize and load dependencies")
	dictDependencies = dot_py_object_dict(name='DEPENDENCIES')	# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for DEPENDENCIES only, of class dot_py_object_dict
	dependencies_folder_to_parse = objSETTINGS.depsFolder	# for input, eg packages/dependencies
	dictDependencies.load_py_files(folder=dependencies_folder_to_parse, heading='Dependency')
	#dictDependencies.dump_vars(heading='DEPENDENCY VARIABLES DUMP:')
	logger.info(f"Finished Processing initialize and load dependencies")

	# Initialize and load the Variables - note the use of a fixed text string type="V" to identify it as a Variables
	logger.debug(f"Processing initialize and load variables.py")
	objVariables = dot_py_object(name='VARIABLES') # an object of the variables, of class dot_py_object
	variables_file_to_parse = objSETTINGS.varsPath	# for input, eg packages/variables.py
	objVariables.load_py_file(file=variables_file_to_parse, heading='Variables')
	#objVariables.dump_vars(heading='variables.py VARIABLES DUMP:')
	logger.info(f"Finished Processing initialize and load variables.py")
	
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
	logger.info(f"Processing initial sanity check of products and dependencies")
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
	logger.debug(f"SANITY CHECK: passed. No duplicate PRODUCT and DEPENDENCY filenames detected")
	logger.info(f"Finished Processing initial sanity check of products and dependencies. Passed.")
	
	# If commandline says INFO then do INFO stuff and exit
	if objArgParser.info:
		logger.info(f"Processing 'info' commandline actions")
		if objArgParser.info_depends_on:			# ./this_script.py --debug info --depends_on avisynth_plus_headers
			info_print_depends_on(objArgParser.info_depends_on)		# pass the name of the package the subject of the query
		if 	objArgParser.info_required_by:			# ./this_script.py --debug info --required_by ffmpeg
			info_print_required_by(objArgParser.info_required_by)	# pass the name of the package the subject of the query
		logger.info(f"Finished Processing 'info' commandline actions")
		exit()


	# If commandline says LIST then do LIST stuff and exit
	if objArgParser.list:
		logger.info(f"Processing 'list' commandline actions")
		if objArgParser.list_products:				# ./this_script.py --debug list -d
			dictProducts.list_print(heading='PRODUCTS')
		if 	objArgParser.list_dependencies:			# ./this_script.py --debug list -p
			dictDependencies.list_print(heading='DEPENDENCIES')
		# for good measure, always list Variables free,gratis after the others
		objVariables.list_print(heading='VARIABLES')
		logger.info(f"Finished Processing 'list' commandline actions")
		exit()

	# Setup the general environment ... if necessary change settings in objSETTINGS
	# set other variables including eg for "{cmake_prefix_options}" "!VARxxxVAR!" "!CMDyyyCMD!" etc
	# what to build is in objArgParser
	# create folders
	# init environment variables using os.environ
	prepareForBuilding()	# also does cchdir(objSETTINGS.fullWorkDir)

	# Setup the mingw64 build environment and build the cross-compiling compilers etc
	# what to build is in objArgParser
	# settings to use are in objSETTINGS ... if necessary change settings in objSETTINGS
	buildMingw64()			# also does cchdir(objSETTINGS.fullWorkDir)


	# build the specified package, could be a dependency, dependency tree, product, product tree.
	# 




#------------------------


#def assembleConfigHelps:
#				main.prepareBuilding(64)
#				main.build_mingw(64)
#				main.initBuildFolders()

#def commandLineEntrace:
#	# has args
#	for thing in finalPkgList:
#				for b in self.targetBitness:
#					main.prepareBuilding(b)
#					main.buildMingw(b)
#					main.initBuildFolders()
#					if buildType == "PRODUCT":
#						self.buildThing(thing, self.packages["prods"][thing], buildType, forceRebuild, skipDeps)
#					else:
#						self.buildThing(thing, self.packages["deps"][thing], buildType, forceRebuild, skipDeps)
#					main.finishBuilding()

#def defaultEntrace():
#		for b in self.targetBitness:
#			self.prepareBuilding(b)
#			self.buildMingw(b)
#			self.initBuildFolders()
#			for p in self.product_order:
#				self.buildThing(p, self.packages["prods"][p], "PRODUCT")
#			self.finishBuilding()


#def finishBuilding(self):
#	self.cchdir("..")







	#parser_epilog = 'Copyright (C) 2023-2024 hydra3333\n\n This Source Code Form is subject to the terms of the GNU General Public License version 3 or any later version. If a copy of the GPLv3 was not distributed with this file, You may obtain one at https://www.gnu.org/licenses/gpl-3.0.html'
	#parser = argparse.ArgumentParser(formatter_class=epiFormatter, epilog=parser_epilog)
	
	exit()

##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################

