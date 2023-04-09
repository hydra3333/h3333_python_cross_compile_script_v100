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
global biggusDictus		# combined dictProducts | dictDependencies
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
impoert os.path
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
#------------------------------------------------------------------------------------------------------------
# imports for LIST --versions
##from telnetlib import EC # 2022.12.18 per DEADSIX27 ?????????? why
import ftplib
#from distutils.version import LooseVersion replaced by packaging version
from packaging.version import Version
from bs4 import BeautifulSoup
##from colorama import Fore, Style, init
import tools.libs.htmllistparse as htmllistparse  # https://github.com/gumblex/htmllisting-parser
#------------------------------------------------------------------------------------------------------------

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
	global biggusDictus		# combined dictProducts | dictDependencies
	global objPrettyPrint	# facilitates formatting and printing of text and dicts etc
	global TERMINAL_WIDTH	# for Console setup and PrettyPrint setup

	def errorExit(self, msg): # logger is not up and running yet, so use our own self.errorExit instead and use PRINT not logger to display the msg
		#logger.error(msg)
		print(f"Settings Error: {msg}")
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
		possiblePathsStr = subprocess.check_output(f"pkg-config --variable pc_path pkg-config", shell=True, stderr=subprocess.STDOUT).decode("utf-8").strip()
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

		print(f"Processing initial settings")
		# _working and STATUS stuff first
		self.debugMode = False											# True or False
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
		
		self.patches_top_url = 'https://github.com/hydra3333/h3333_python_cross_compile_script_v100/master/patches/' # if trunk moves to "main" then use "main" instead of "master"
		
		self.workdir_subfolder ='workdir'											# 'workdir'  is the subfolder where actual build stuff happens
		self.fullWorkDir    = self.projectRoot.joinpath(self.workdir_subfolder)		# for output, eg workdir
		
		self.bitnessStr = "x86_64"										# eg x86_64 underneath workdir_subfolder
		self.bitnessStr2 = "x86_64"										# just for vpx... underneath workdir_subfolder
		self.bitnessStr3 = "mingw64"									# just for openssl... underneath workdir_subfolder
		self.targetOSStr = "mingw64"									# 2019.12.13 just for "--target-os=" 
		self.bitnessStrWin = "win64"									# eg 'win64'

		self.targetHostStr       = F"{self.bitnessStr}-w64-mingw32"  	# eg x86_64-w64-mingw32

		self.original_cflag					= ' -O3 '
		self.original_stack_protector		= ' -fstack-protector-all '
		self.original_fortify_source		= ' -D_FORTIFY_SOURCE=2 '

		self.original_cflag_trim			= self.original_cflag.strip()
		self.original_stack_protector_trim	= self.original_stack_protector.strip()
		self.original_fortify_source_trim	= self.original_fortify_source.strip()

		self.original_Cflags				= f' {self.original_cflag_trim} {self.original_stack_protector_trim} {self.original_fortify_source_trim} '	# was originalCflags, let's see what breaks
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
		
		self.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'		# LTS as at 2023.02.07
		self.HEADERS =	{	'User-Agent': self.userAgent,
							'Accept-Language': 'en,en-US;',
							'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
						}
		self.SOURCEFORGE_APIKEY = None
		# if not os.path.isfile("sourceforge.apikey"):
		# 	errorExit(f"Missing sourceforge.apikey file, create it and write your api key inside of it")
		# else:
		# 	self.SOURCEFORGE_APIKEY = open("sourceforge.apikey","r").read()
		# 	print(f"Loaded sourceforge api key: " + self.SOURCEFORGE_APIKEY)
		
		self.log_format = '[%(asctime)s][%(levelname)s]%(type)s %(message)s'
		self.log_date_format = '%H:%M:%S'

		# mainly calculated variables next

		self.mesonEnvFile = self.fullWorkDir.joinpath("meson_environment.txt")			# used when building packages
		self.cmakeToolchainFile = self.fullWorkDir.joinpath("mingw_toolchain.cmake")	# used when building packages
		self.cargoHomePath = self.fullWorkDir.joinpath("cargohome")						# per deadsix27, used for rust

		self.packagesFolder = self.projectRoot.joinpath(self.packages_subfolder)	# for input, eg packages
		self.prodFolder     = self.packagesFolder.joinpath("products")					# for input, eg packages/products
		self.depsFolder     = self.packagesFolder.joinpath("dependencies")				# for input, eg packages/dependencies
		self.varsPath       = self.packagesFolder.joinpath("variables.py")				# for input, eg packages/variables.py
		self.patchesFolder	= self.projectRoot.joinpath(self.patches_subfolder)			# for input, eg packages
		self.fullPatchDir   = self.patchesFolder										# duplicated, cull later
		self.additionalheadersFolder	= self.projectRoot.joinpath(self.additionalheaders_subfolder)			# for input, eg packages
		self.sourcesFolder	= self.projectRoot.joinpath(self.sources_subfolder)			# for input, eg packages
		self.toolsFolder	= self.projectRoot.joinpath(self.tools_subfolder)			# for input, eg tools

		self.bitnessPath = self.fullWorkDir.joinpath(self.bitnessStr)					# for output, eg workdir/x86_64
	
		self.fullProductDir = self.fullWorkDir.joinpath(self.bitnessStr + "_products")	# for output, eg workdir/x86_64_products
		self.fullOfftreeDir = self.fullWorkDir.joinpath(self.bitnessStr + "_offtree")	# for output, eg workdir/x86_64_offtree

		self.fullDependencyDir = self.bitnessPath.joinpath("")							# to be compatible with deadsix27, rather than use a new 'x86_64_dependencies'

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
		#self.autoConfPrefixOptions = F'--with-sysroot="{self.targetSubPrefix}" --host={self.targetHostStr} --prefix={self.targetPrefix} --disable-shared --enable-static'
		self.autoConfPrefixOptions = F'--host={self.targetHostStr} --prefix={self.targetPrefix} --disable-shared --enable-static'
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
		#
		self.rustTargetStr = "x86_64-pc-windows-gnu" # hardcoded, only 64bit supported.
		#
		# define the name of the gcc compiler
		self.gcc_bin = os.path.join(self.mingwBinpath, self.bitnessStr + "-w64-mingw32-gcc")

		self.substitutionDict = defaultdict(lambda: "")
		self.substitutionDict.update(
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
				'rust_target': self.rustTargetStr,
				'product_prefix': self.fullProductDir,
				'target_prefix_sed_escaped': str(self.targetPrefix).replace("/", "\\/"),
				'make_cpu_count': "-j {0}".format(self.cpuCount),
				#'original_cflags': self.originalCflags,
				'cflag_string': generateCflagString(f"--extra-cflags="),
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
	
		#os.environ['PATH'] = f"{self.mingwBinpath}:{self.originalPATH}"
		#os.environ['PKG_CONFIG_PATH'] = self.pkgConfigPath
		#os.environ['PKG_CONFIG_LIBDIR'] = ''
		#os.environ['COLOR'] = "ON"  # Force coloring on (for CMake primarily)
		#os.environ['CLICOLOR_FORCE'] = "ON"  # Force coloring on (for CMake primarily)

		print(f"Processing finished Processing initial settings")
		return

###################################################################################################
def resetDefaultEnvVars():
	os.environ['PATH']              = f"{objSETTINGS.mingwBinpath}:{objSETTINGS.originalPATH}"
	os.environ['CFLAGS']            = objSETTINGS.originalCflags
	os.environ['CXXFLAGS']          = objSETTINGS.originalCflags
	os.environ['CPPFLAGS']          = objSETTINGS.originalCflags
	os.environ['LDFLAGS']           = objSETTINGS.originalCflags
	os.environ['CARGO_HOME']		= objSETTINGS.cargoHomePath
	os.environ['PKG_CONFIG_PATH']   = objSETTINGS.pkgConfigPath
	os.environ['PKG_CONFIG_LIBDIR'] = ''
	os.environ['COLOR']				= "ON" 	# Force coloring on (for CMake primarily)
	os.environ['CLICOLOR_FORCE']	= "ON"  # Force coloring on (for CMake primarily)
	logger.info(f"Reset CFLAGS/CXXFLAGS/CPPFLAGS/LDFLAGS to: '{objSETTINGS.originalCflags}', PKG_CONFIG_PATH to '{objSETTINGS.pkgConfigPath}', PKG_CONFIG_LIBDIR to ''")
	if objSETTINGS.debugMode:
		dump_environment_variables(override=True)
		pass

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
	global biggusDictus		# combined dictProducts | dictDependencies
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
def dump_environment_variables(override=None):
	override = objSETTINGS.debugMode
	if not objSETTINGS.debugMode:
		if override is not None:
			if override:	# ok, we haev been told to override a debugMode=false
				logger.info(f"##############################################################")
				logger.info(f"### Environment variables: ###")
				for osv in os.environ:
					logger.info(f"\t'{osv}' : '{os.environ[osv]}'")
				logger.info(f"##############################################################")

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
	global biggusDictus		# combined dictProducts | dictDependencies
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
	global biggusDictus		# combined dictProducts | dictDependencies
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

	def get_dot_py_obj(self, packageName):	
		# return a key/value pair as an object of class dot_py_object
		#logger.debug(f"DEBUG: Entered get_dot_py_obj")
		tmp = dot_py_object()					# create a new instance of class dot_py_object
		if packageName in self.BO:				# check whether a single key is in the dictionary
			tmp.name = packageName				# yes, insert the package name into the tmp object
			tmp.Val = self.BO[packageName]		# yes, insert the dict of json info into the tmp object
			#logger.debug(f"get_dot_py_obj packageName '{packageName}' found tmp.name='{tmp.name}'")
		else:
			tmp.name = None						# this should be the object's default for class dot_py_object anyway
			tmp.Val = {}						# this should be the object's default for class dot_py_object anyway
			#logger.debug(f"get_dot_py_obj packageName '{packageName}' NOT found tmp.name='{tmp.name}'")
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
					self.errorExit(f"SyntaxError: load_py_files: dot_py_object_dict({self.name}): Loading {heading} File '{packageName}' failed:\n\n{traceback.format_exc()}")
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
	global biggusDictus		# combined dictProducts | dictDependencies
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
	global biggusDictus		# combined dictProducts | dictDependencies
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
	global biggusDictus		# combined dictProducts | dictDependencies
	global objPrettyPrint	# facilitates formatting and printing of text and dicts etc
	global TERMINAL_WIDTH	# for Console setup and PrettyPrint setup

	if new_debugMode:
		objSETTINGS.debugMode = True
		setLogLevel(logging.DEBUG)
	else:
		objSETTINGS.debugMode = False
		setLogLevel(logging.INFO)
		#logger.debug(f"")
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
	global biggusDictus		# combined dictProducts | dictDependencies
	global objPrettyPrint	# facilitates formatting and printing of text and dicts etc
	global TERMINAL_WIDTH	# for Console setup and PrettyPrint setup

	def dump_vars(self, heading='VARIABLES DUMP:'):
		global_dump_object_variables(self, heading)
		return
		
	def __init__(self):
		logger.info(f"processCmdLineArguments: Processing CommandLine arguments")
		logger.debug(f"processCmdLineArguments: Entered processCmdLineArguments")

		# Create a neew main parser
		logger.debug(f"processCmdLineArguments: Creating the ArgumentParser with parser = argparse.ArgumentParser")
		self.parser_programname = 'h3333_python_cross_compile_script'
		self.parser_program_description = Colors.RESET + Colors.CYAN + self.parser_programname + Colors.RESET + "" \
										"\nExample usages:" \
										"\n '{0} list -p'                                   - lists all products" \
										"\n '{0} list -d'                                   - lists all dependencies" \
										"\n '{0} list --versions'                           - Check/List versions of all products/dependencies" \
										"\n '{0} info --required_by avisynth_plus_headers'  - List all packages this dependency is required by" \
										"\n '{0} info --depends_on ffmpeg'                  - List all packages this package depends on (recursively)" \
										"\n '{0} --force --debug -d avisynth_plus_headers'  - forces rebuilding of dependency avisynth_plus_headers" \
										"\n '{0} --force -debug -p ffmpeg'                  - forces rebuilding of product ffmpeg" \
										"\n '{0} --cmd_help'                                - Do nothing but show help and exit" \
										"".format(self.parser_programname)
		self.parser_epilog = "Copyright (C) 2023-2024 hydra3333 (https://github.com/hydra3333/h3333_python_cross_compile_script_v100)\n" \
						"This Source Code Form is subject to the terms of the\n" \
						"Mozilla Public License v. 2.0 (MPLv2).\n" \
						"If a copy of the MPLv2 was not distributed with this file,\n" \
						"You can obtain one at https://mozilla.org/MPL/2.0/ \n "
		self.parser = argparse.ArgumentParser(	formatter_class=epiFormatter, \
											prog=self.parser_programname, \
											description=self.parser_program_description, \
											epilog=self.parser_epilog )
		logger.debug(f"processCmdLineArguments: Created the ArgumentParser with argparse.ArgumentParser")

		# set a name in the top level main ArgumentParser
		logger.debug(f"Setting a name in the top level ArgumentParser")
		self.parser.set_defaults(which="main") # set a default argument "which" with a default value "main" in the main parser
		logger.debug(f"processCmdLineArguments: Set a name in the top level ArgumentParser")

		# Add generic arguments
		# add generic arguments to the main ArgumentParser object. 
		# Note the "-g" for debug, since "-d" is already taken for dependency processing
		# Note: the second argument contains the variable-name to check later eg "if args.debug"
		logger.debug(f"processCmdLineArguments: Create and add arguments to the top level ArgumentParser for generic use")
		self.parser.add_argument("-g", "--debug",        help="Show debug information",											action="store_true", default=False)
		self.parser.add_argument("-f", "--force",        help="Force rebuild of nominated package, deletes already existing files (recommended)",	action="store_true", default=False)
		self.parser.add_argument("-a", "--allforce",     help="Force rebuild of nominated package and its all dependencies, deletes already existing files",	action="store_true", default=False)
		self.parser.add_argument("-s", "--skip_depends", help="Skip dependencies when building",								action="store_true", default=False)
		# called like:	program.py --force --debug -d avisynth_plus_headers
		# 				program.py --force --debug -p ffmpeg
		# 				program.py --force --debug --skip-depends -p ffmpeg
		logger.debug(f"processCmdLineArguments: Created and added arguments to the top level ArgumentParser for generic use")

		# add sub-parsers object to the main ArgumentParser object
		logger.debug(f"processCmdLineArguments: Add sub-parsers object to the top level ArgumentParser")
		self.subparsers = self.parser.add_subparsers(help="Sub commands")
		logger.debug(f"processCmdLineArguments: Added sub-parsers object to the top level ArgumentParser")

		# create and add the (sub)parser for the "list" command to the sub-parsers object 
		# and name it with which="list_p" ... parser.prog is the programname we set
		logger.debug(f"processCmdLineArguments: Create and add arguments to the (sub)parser for the 'list' command")
		self.list_p = self.subparsers.add_parser("list", help="Type: '" + self.parser.prog + " list'")
		self.list_p.set_defaults(which="list")
		# add arguments to the "list" command parser which="list_p"
		# Note: the second argument contains the variable-name to check later eg "if args.dependencies"
		list_p_group1 = self.list_p.add_mutually_exclusive_group(required=True)
		list_p_group1.add_argument("-p", "--products",     help="List all products",     action="store_true", default=False)
		list_p_group1.add_argument("-d", "--dependencies", help="List all dependencies", action="store_true", default=False)
		list_p_group1.add_argument("-v", "--versions", help="Check/List versions of all products/dependencies", action="store_true", default=False)
		# called like:	program.py list -d
		# 				program.py list -p
		logger.debug(f"processCmdLineArguments: Created and added arguments to the (sub)parser for the 'list' command")

		# create and add the (sub)parser for the "info" command to the sub-parsers object 
		# and name it with which="list_p" ... parser.prog is the programname we set
		logger.debug(f"processCmdLineArguments: Create and add arguments to the (sub)parser for the 'info' command")
		self.info_p = self.subparsers.add_parser("info", help="Type: '" + self.parser.prog + " info")
		self.info_p.set_defaults(which="info")
		# add arguments to the "info" command parser which="info_p"
		# Note: the second argument contains the variable-name to check later eg "args.required_by"
		self.info_p_group1 = self.info_p.add_mutually_exclusive_group(required=True)
		self.info_p_group1.add_argument("-r", "--required_by", help="List all packages this dependency is required by",        default=None)
		self.info_p_group1.add_argument("-d", "--depends_on",  help="List all packages this package depends on (recursively)", default=None)
		# called like:	program.py info -r avisynth_plus_headers
		# 				program.py info -d ffmpeg
		logger.debug(f"processCmdLineArguments: Created and added arguments to the (sub)parser for the 'info' command")

		# *** Now it is time for arguments to initiate the build process
		# create and add a mutually exclusive group to the main ArgumentParser object
		logger.debug(f"processCmdLineArguments: Create and add arguments to the top level ArgumentParser for building stuff")
		self.group2 = self.parser.add_mutually_exclusive_group(required=False)
		# add arguments to the mutially exclusive group, to build a dependency or a product
		# Note: the second argument contains the variable-name to check later eg "if args.build_product"
		self.group2.add_argument("-p", "--build_product",    dest="PRODUCT",    help="Build the specificed product package(s)",	default=None)	# dest="PRODUCT", 
		self.group2.add_argument("-d", "--build_dependency", dest="DEPENDENCY", help="Build the specificed dependency package(s)",	default=None)	# dest="DEPENDENCY",
		self.group2.add_argument("-c", "--cmd_help", help="Do nothing but show help", action="store_true", default=False) # use "-c" since -h and --help CONFLICT with system stuff
		# called like:	program.py -d avisynth_plus_headers
		# 				program.py -p ffmpeg
		logger.debug(f"processCmdLineArguments: Created and added arguments to the top level ArgumentParser for building stuff")

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
		logger.debug(f"processCmdLineArguments: CMDLINE Processed arg self.args.force='{self.args.force}'")

		if self.args.allforce:
			self.allforce = True
			self.force = True
		else:
			self.allforce = False
		logger.debug(f"processCmdLineArguments: CMDLINE Processed arg self.args.allforce='{self.args.allforce}'")

		if self.args.skip_depends:
			self.skip_depends = True
		else:
			self.skip_depends = False
		logger.debug(f"processCmdLineArguments: CMDLINE Processed arg self.args.skip_depends='{self.args.skip_depends}'")

		if self.args.debug:
			self.debug = True	# variable ArgParser.debug is referenced elsewhere
		else:
			self.debug = False	# variable ArgParser.debug is referenced elsewhere
		# check and possibly over-ride any debug mode 
		or_debug_modes = objSETTINGS.debugMode or self.debug
		if or_debug_modes:	# one or the other is true, so make it all true, a one-way
			self.debug = True
			setDebugMode(self.debug)
		logger.debug(f"processCmdLineArguments: CMDLINE Processed arg self.args.debug='{self.args.debug}' self.debug (ArgParser.debug)='{self.debug}' objSETTINGS.debugMode='{objSETTINGS.debugMode}' ")

		# initialize for finding specific commands and parameters
		self.list = False
		self.list_products = False
		self.list_dependencies = False
		self.list_versions = False
		self.info = False
		self.info_required_by = None
		self.info_depends_on = None
		self.build = False
		self.build_PRODUCT = None
		self.build_DEPENDENCY = None

		# Note: the 'match' statement only works in Python 3.10 and above # https://learnpython.com/blog/python-match-case-statement/
		match self.args.which.lower():
			case "list":
				logger.debug(f"processCmdLineArguments: CMDLINE Processing arg self.args.which='{self.args.which}'")
				self.list = True
				if self.args.products:
					logger.debug(f"processCmdLineArguments: CMDLINE Processing arg self.args.products='{self.args.products}' in 'list_p'")
					self.list_products = True
				elif self.args.dependencies:
					logger.debug(f"processCmdLineArguments: CMDLINE Processing arg self.args.dependencies='{self.args.dependencies}' in 'list_p'")
					self.list_dependencies = True
				elif self.args.versions:
					# the name of the thing to process with INFO is in self.args.depends_on
					logger.debug(f"processCmdLineArguments: CMDLINE Processing arg self.args.versions='{self.args.versions}' in 'list_p'")
					self.list_versions = True
				else:
					msg = f"processCmdLineArguments: CMDLINE Processing arg self.args.which='{self.args.which}' BUT THERE IS NO MATCHED CMDLINE CONDITION ... exiting"
					logger.error(msg)
					sys.exit(1)
			case "info":
				logger.debug(f"processCmdLineArguments: CMDLINE Processing arg self.args.which='{self.args.which}'='info_p'")
				self.info = True
				if self.args.required_by:
					# the name of the thing to process with INFO is in self.args.required_by
					logger.debug(f"processCmdLineArguments: CMDLINE Processed arg self.args.required_by='{self.args.required_by}' in 'info_p'")
					self.info_required_by = self.args.required_by
				elif self.args.depends_on:
					# the name of the thing to process with INFO is in self.args.depends_on
					logger.debug(f"processCmdLineArguments: CMDLINE Processing arg self.args.depends_on='{self.args.depends_on}' in 'info_p'")
					self.info_depends_on = self.args.depends_on
				else:
					msg = f"processCmdLineArguments: CMDLINE Processed arg self.args.which='{self.args.which}' BUT THERE IS NO MATCHED CMDLINE CONDITION ... exiting"
					logger.error(msg)
					sys.exit(1)
			case "main":
				logger.debug(f"processCmdLineArguments: CMDLINE Processing arg self.args.which='{self.args.which}'='main'")
				self.build = True
				if self.args.PRODUCT:
					self.build_PRODUCT = self.args.PRODUCT
					logger.debug(f"processCmdLineArguments: CMDLINE Processing arg self.args.which='{self.args.which}'='main' self.build_PRODUCT='{self.build_PRODUCT}'")
				elif self.args.DEPENDENCY:
					self.build_DEPENDENCY = self.args.DEPENDENCY
					logger.debug(f"processCmdLineArguments: CMDLINE Processing arg self.args.which='{self.args.which}'='main' self.build_PRODUCT='{self.build_DEPENDENCY}'")
				else:
					msg = f"processCmdLineArguments: CMDLINE Processed arg self.args.which='{self.args.which}' BUT THERE IS NO MATCHED CMDLINE CONDITION ... exiting"
					logger.error(msg)
					sys.exit(1)
			case _:	# the "_" means a final "else"
				msg = f"processCmdLineArguments: CMDLINE Processed arg self.args.which='{self.args.which}' BUT THERE IS NO MATCHING CMDLINE CONDITION ... exiting"
				logger.error(msg)
				sys.exit(1)
				sys.exit(1)

		# If it gets to here, relevant 'self' variables have been set to inform us what to do.
		# The relevant 'self' variables can be queried from the newly instantiated object. 
		# NOTE: the only exception is --debug which is processed straight away to change the global setting
		
		#logger.debug(f"*processCmdLineArguments self.list='{self.list}' self.list_products='{self.list_products}'")
		#logger.debug(f"*processCmdLineArguments self.list='{self.list}' self.list_dependencies='{self.list_dependencies}'")
		#logger.debug(f"*processCmdLineArguments self.info='{self.info}' self.list_versions='{self.list_versions}'")
		#logger.debug(f"*processCmdLineArguments self.info='{self.info}' self.info_required_by='{self.info_required_by}'")
		#logger.debug(f"*processCmdLineArguments self.info='{self.info}' self.info_depends_on='{self.info_depends_on}'")
		#logger.debug(f"*processCmdLineArguments self.build='{self.build}' self.build_PRODUCT='{self.build_PRODUCT}' self.build_DEPENDENCY='{self.build_DEPENDENCY}'")
		#logger.debug(f"*processCmdLineArguments self.debug='{self.debug}'")
		#logger.debug(f"*processCmdLineArguments self.force='{self.force}'")
		#logger.debug(f"*processCmdLineArguments self.allforce='{self.allforce}'")
		#logger.debug(f"*processCmdLineArguments self.skip_depends='{self.skip_depends}'")
		#if objSETTINGS.debugMode:
		#	self.dump_vars('### debugMode: processCmdLineArguments INTERNAL VARIABLES DUMP:')

		logger.info(f"processCmdLineArguments: Finished Processing CommandLine arguments")
		logger.debug(f"processCmdLineArguments: Returning from processCmdLineArguments")

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
	global biggusDictus		# combined dictProducts | dictDependencies
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

	def info_print_required_by_recursive(packageName, indent=1):
		if 'depends_on' not in biggusDictus[packageName]:
			return
		zz_depends_on = biggusDictus[packageName]['depends_on']
		if len(zz_depends_on) <= 0:
			return
		#if boolKey(biggusDictus[packageName], "is_dep_inheriter"):
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
	global biggusDictus		# combined dictProducts | dictDependencies
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

	#objPrettyPrint.pprint(biggusDictus['ffmpeg'])
	#for key, val in biggusDictus.items():
	#	print(f"key='{key}'")
	#for key, val in biggusDictus['ffmpeg'].items():
	#	print(f"ffmpeg key='{key}'")
	#print(biggusDictus['ffmpeg'])
	n = packageName
	def info_print_depends_on_recursive(y,indent=1):
		for k, v in biggusDictus.items():
			if "depends_on" in biggusDictus[k]:
				if len(biggusDictus[k]['depends_on']) > 0:
					if y in biggusDictus[k]['depends_on']:
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
	global objSETTINGS		# the SETTINGS object used everywhere
	global logging_handler 	# the handler for the logger, only used for initialization
	global logger 			# the logger object used everywhere
	global objArgParser		# the ArgParser which may be used everywhere
	global objParser		# the parser creat6ed by ArgParser which may be used everywhere
	global dictProducts		# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for PRODUCTS only, of class dot_py_object_dict
	global dictDependencies	# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for DEPENDENCIES only, of class dot_py_object_dict
	global objVariables		# an object of the variables, of class dot_py_object
	global biggusDictus		# combined dictProducts | dictDependencies
	global objPrettyPrint	# facilitates formatting and printing of text and dicts etc
	global TERMINAL_WIDTH	# for Console setup and PrettyPrint setup

	logger.info(f"Processing prepareForBuilding. This script and .py files SHOULD be in projectRoot='{objSETTINGS.projectRoot}'")

	# start with the environment variables set up.
	resetDefaultEnvVars()

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
	logger.info(f"'{objSETTINGS.mesonEnvFile}' contains:")
	cmd = f"cat {objSETTINGS.mesonEnvFile}"
	ret, result = runProcess(cmd, ignoreErrors=True, yield_return_code=True)
	if ret == 0:
		logger.debug(f"command: '{cmd}' return_code: '{ret}'")	# RESULT:\n{result}
	else:
		logger.info(f"command failed: '{cmd}' return_code: '{ret}' RESULT:\n{result}")
		exit(ret)

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
	logger.info(f"'{objSETTINGS.cmakeToolchainFile}' contains:")
	cmd = f"cat {objSETTINGS.cmakeToolchainFile}"
	ret, result = runProcess(cmd, ignoreErrors=True, yield_return_code=True)
	if ret == 0:
		logger.debug(f"command: '{cmd}' return_code: '{ret}'")	# RESULT:\n{result}
	else:
		logger.info(f"command failed: '{cmd}' return_code: '{ret}' RESULT:\n{result}")
		exit(ret)

	# Always RE-create the Rust Cargo stuff every time, in case  we have changed something
	#os.environ["CARGO_HOME"] = str(objSETTINGS.cargoHomePath)
	if True:
		logger.info(f"Creating Cargo Home stuff for Rust: '{objSETTINGS.cargoHomePath}'")
		logger.info(f"Creating environment variable 'CARGO_HOME' = '{objSETTINGS.cargoHomePath}'")
		os.environ["CARGO_HOME"] = str(objSETTINGS.cargoHomePath)
		cargoConfigPath = objSETTINGS.cargoHomePath.joinpath("config.toml")	# from deadsix27
		if not os.path.isdir(objSETTINGS.cargoHomePath):
			logger.info(f"Creating Cargo Home folder: '{objSETTINGS.cargoHomePath}'")
			objSETTINGS.cargoHomePath.mkdir(parents=True)
		tcFile = [
			F'[target.{objSETTINGS.rustTargetStr}]',
			F'linker = "{objSETTINGS.shortCrossPrefixStr}gcc"',
			F'ar = "{objSETTINGS.shortCrossPrefixStr}ar"',
		]
		with open(cargoConfigPath, 'w') as f:
			f.write("\n".join(tcFile))
		logger.info(f"Wrote Cargo Home file 'config.toml' in '{objSETTINGS.cargoHomePath}'")
		logger.info(f"Setting up cargo toolchain in '{objSETTINGS.cargoHomePath}'")
		#os.system("cargo install cargo-c")
		runProcess(f'cargo install cargo-c')
	else:
		logger.debug(f"Using existing Cargo Home stuff in '{objSETTINGS.cargoHomePath}'")
	logger.info(f"'{cargoConfigPath}' contains:")
	cmd = f"cat {cargoConfigPath}"
	ret, result = runProcess(cmd, ignoreErrors=True, yield_return_code=True)
	if ret == 0:
		logger.debug(f"command: '{cmd}' return_code: '{ret}'")	# RESULT:\n{result}
	else:
		logger.info(f"command failed: '{cmd}' return_code: '{ret}' RESULT:\n{result}")
		exit(ret)
	#
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
	global biggusDictus		# combined dictProducts | dictDependencies
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
		os.unsetenv('CFLAGS')								# unset any existing CFLAGS environment variable
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

###################################################################################################
def generateCflagString(prefix=""):
	if 'CFLAGS' not in os.environ:
		return ""
	cfs = os.environ['CFLAGS']
	cfs = cfs.split(" ")
	if (len(cfs) == 1 and cfs[0] != "") or not len(cfs):
		return ""
	out = ''
	if len(cfs) >= 1:
		for c in cfs:
			out += prefix + c + " "
		out.rstrip(" ")
		return out
	return ''

###################################################################################################
class MissingDependency(Exception):
	# raise an exception ... used like:
	#	raise MissingDependency(f"The dependency '{libraryName}' of '{packageName}' does not exist")  # sys.exc_info()[0]
	__module__ = 'exceptions'
	def __init__(self, message):
		self.message = message

###################################################################################################
def errorExit(msg):
	logger.error(msg)
	sys.exit(1)

###################################################################################################
def cchdir(dir, silent=False):
	if objSETTINGS.debugMode:
		logger.debug(f"cd {dir} # Change dir from '{os.getcwd()}' to '{dir}'")
	elif not silent:
		logger.info(f"cd {dir} # Change dir from '{os.getcwd()}' to '{dir}'")
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
def getValueOrNone(db, k):
	if k in db:
		if db[k] is None:
			return None
		else:
			return db[k]
	else:
		return None

###################################################################################################
def getValueOrZero(db, k):
	if k in db:
		if db[k] is None:
			return 0
		else:
			return db[k]
	else:
		return 0

###################################################################################################
def getValueByIntOrNone(db, key):
	if key >= 0 and key < len(db):
		return db[key]
	else:
		return None

###################################################################################################
def reReplaceInFile(infile, oldString, newString, outfile):
	with open(infile, 'rw') as f:
		for line in f:
			line = re.sub(oldString, newString, line)

###################################################################################################
def getKeyOrBlankString(db, k):
	if k in db:
		if db[k] is None:
			return ""
		else:
			return db[k]
	else:
		return ""

###################################################################################################
def anyFileStartsWith(wild):
	for file in os.listdir("."):
		if file.startswith(wild):
			return True
	return False

###################################################################################################
def removeAlreadyFiles():
	for af in glob.glob("./already_*"):
		os.remove(af)

###################################################################################################
def removeConfigPatchDoneFiles():
	for af in glob.glob("./*.diff.done_past_conf"):
		os.remove(af)
	for af in glob.glob("./*.patch.done_past_conf"):
		os.remove(af)

###################################################################################################
def handleRegexReplace(rp, packageName):
	cwd = Path(os.getcwd())
	if "in_file" not in rp:
		errorExit(f"handleRegexReplace: The regex_replace command in the package {packageName}:\n{rp}\nMisses the in_file parameter.")
	if 0 not in rp:
		errorExit(f"handleRegexReplace: A regex_replace command in the package {packageName}\nrequires at least the '0' key to be a RegExpression, if 1 is not defined matching lines will be removed.")

	in_files = rp["in_file"]
	if isinstance(in_files, (list, tuple)):
		in_files = (cwd.joinpath(replaceVarCmdSubStrings(x)) for x in in_files)
	else:
		in_files = (cwd.joinpath(replaceVarCmdSubStrings(in_files)), )
	repls = [replaceVarCmdSubStrings(rp[0]), ]
	if 1 in rp:
		repls.append(replaceVarCmdSubStrings(rp[1]))
	logger.info(f"handleRegexReplace: Running regex replace commands on package: '{packageName}' [{os.getcwd()}]")
	for _current_infile in in_files:
		if "out_file" not in rp:
			out_files = (_current_infile, )
			logger.debug(f"handleRegexReplace: cp -f '{_current_infile}' '{_current_infile.parent.joinpath(_current_infile.name + '.backup')}' # copy file ")
			shutil.copy(_current_infile, _current_infile.parent.joinpath(_current_infile.name + ".backup"))
		else:
			if isinstance(rp["out_file"], (list, tuple)):
				out_files = (cwd.joinpath(replaceVarCmdSubStrings(x)) for x in rp["out_file"])
			else:
				out_files = (cwd.joinpath(replaceVarCmdSubStrings(rp["out_file"])),)
		for _current_outfile in out_files:
			if not _current_infile.exists():
				logger.warning(F"handleRegexReplace: [Regex-Command] In-File '{_current_infile}' does not exist in '{os.getcwd()}'")
			if _current_outfile == _current_infile:
				_backup = _current_infile.parent.joinpath(_current_infile.name + ".backup")
				if not _backup.parent.exists():
					logger.warning(F"handleRegexReplace: [Regex-Command] Out-File parent '{_backup.parent}' does not exist.")
				logger.debug(f"handleRegexReplace: cp -f '{_current_infile}' '{_backup}' # copy file ")
				shutil.copy(_current_infile, _backup)
				_tmp_file = _current_infile.parent.joinpath(_current_infile.name + ".tmp")
				logger.debug(f"handleRegexReplace: mv -f '{_current_infile}' '{_tmp_file}' # move file ")
				shutil.move(_current_infile, _tmp_file)
				_current_infile = _tmp_file
			logger.info(f"handleRegexReplace: [{packageName}] Running regex command on '{_current_outfile}'")
			with open(_current_infile, "r") as f, open(_current_outfile, "w") as nf:
				for line in f:
					if re.search(repls[0], line) and len(repls) > 1:
						logger.debug(f"RegEx replacing line")
						logger.debug(f"in {_current_outfile}\n{line}\nwith:")
						line = re.sub(repls[0], repls[1], line)
						logger.debug(f"\n{line}")
						nf.write(line)
					elif re.search(repls[0], line):
						logger.debug(f"RegEx removing line\n{line}:")
					else:
						nf.write(line)

###################################################################################################
def replaceSubstitutionStrings(inStr):
	# replace the substitution strings like {abcdef} inside a string (eg one of package content strings)
	# with actual filled-in data from say settings or something from substitutionDict
	global objSETTINGS		# the SETTINGS object used everywhere
	global logging_handler 	# the handler for the logger, only used for initialization
	global logger 			# the logger object used everywhere
	global objArgParser		# the ArgParser which may be used everywhere
	global objParser		# the parser creat6ed by ArgParser which may be used everywhere
	global dictProducts		# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for PRODUCTS only, of class dot_py_object_dict
	global dictDependencies	# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for DEPENDENCIES only, of class dot_py_object_dict
	global objVariables		# an object of the variables, of class dot_py_object
	global biggusDictus		# combined dictProducts | dictDependencies
	global objPrettyPrint	# facilitates formatting and printing of text and dicts etc
	global TERMINAL_WIDTH	# for Console setup and PrettyPrint setup
	return inStr.format_map(objSETTINGS.substitutionDict)

def replaceVarCmdSubStrings(inStr):
	# replace the strings like !VAR(ffmpeg_config)VAR! and !CMD(pwd)CMD! inside a string (eg one of package content strings)
	# with actual filled-in data from the variables.py file we pre-read into objVariables.Val
	# and the results of commands
	global objSETTINGS		# the SETTINGS object used everywhere
	global logging_handler 	# the handler for the logger, only used for initialization
	global logger 			# the logger object used everywhere
	global objArgParser		# the ArgParser which may be used everywhere
	global objParser		# the parser creat6ed by ArgParser which may be used everywhere
	global dictProducts		# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for PRODUCTS only, of class dot_py_object_dict
	global dictDependencies	# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for DEPENDENCIES only, of class dot_py_object_dict
	global objVariables		# an object of the variables, of class dot_py_object
	global biggusDictus		# combined dictProducts | dictDependencies
	global objPrettyPrint	# facilitates formatting and printing of text and dicts etc
	global TERMINAL_WIDTH	# for Console setup and PrettyPrint setup
	# do it in this sequence
	if inStr is None:
		return None

	rawInStr = inStr
	
	# replace variables from variables.py
	varList = re.findall(r"!VAR\((?P<variable_name>[^\)\(]+)\)VAR!", inStr)  # TODO: assignment expression
	if varList:
		for varName in varList:
			if varName in objVariables.Val:
				variableContent = objVariables.Val[varName]
				inStr = re.sub(rf"(!VAR\({varName}\)VAR!)", r"{0}".format(variableContent), inStr, flags=re.DOTALL)	# flags=re.DOTALL means "." match any character at all, including a newline
			else:
				inStr = re.sub(rf"(!VAR\({varName}\)VAR!)", r"".format(variableContent), inStr, flags=re.DOTALL)	# flags=re.DOTALL means "." match any character at all, including a newline
				logger.error(f"Unknown variable has been used: '{varName}'\n in: '{rawInStr}', it has been stripped.")
	
	# having replaced variables, also replace any substitution strings
	inStr = replaceSubstitutionStrings(inStr)
	
	# having replaced variables and substitution strings, now also replace commands
	cmdList = re.findall(r"!CMD\((?P<full_cmd>[^\)\(]+)\)CMD!", inStr)  # TODO: assignment expression TODO: handle escaped brackets inside cmd syntax
	if cmdList:
		for cmd in cmdList:
			cmdReplacer = subprocess.check_output(cmd, shell=True).decode("utf-8").replace("\n", "").replace("\r", "").strip()
			inStr = re.sub(r"!CMD\(([^\)\(]+)\)CMD!", F"{cmdReplacer}", inStr, flags=re.DOTALL)	# flags=re.DOTALL means "." match any character at all, including a newline
	
	return inStr

###################################################################################################
def runProcess(command, ignoreErrors=False, exitOnError=True, silent=False, yield_return_code=False):
	# run a shell type command and return a bufffer contaning sanitized stdout results
	isSvn = False
	if not isinstance(command, str):
		command = " ".join(command)  # could fail I guess
	if command.lower().startswith("svn"):
		isSvn = True
	if not silent:
		logger.info(f"Running '{command}' in '{os.getcwd()}'")
	elif objSETTINGS.debugMode:
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
def reviewPackageTree(packageName=''):
	global objSETTINGS		# the SETTINGS object used everywhere
	global logging_handler 	# the handler for the logger, only used for initialization
	global logger 			# the logger object used everywhere
	global objArgParser		# the ArgParser which may be used everywhere
	global objParser		# the parser creat6ed by ArgParser which may be used everywhere
	global dictProducts		# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for PRODUCTS only, of class dot_py_object_dict
	global dictDependencies	# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for DEPENDENCIES only, of class dot_py_object_dict
	global objVariables		# an object of the variables, of class dot_py_object
	global biggusDictus		# combined dictProducts | dictDependencies
	global objPrettyPrint	# facilitates formatting and printing of text and dicts etc
	global TERMINAL_WIDTH	# for Console setup and PrettyPrint setup

	logger.info(f"Processing reviewPackageTree '{packageName}'")
	if objArgParser.build_PRODUCT in dictProducts.BO:
		obj_top_Package = dictProducts.get_dot_py_obj(packageName)
	elif objArgParser.build_DEPENDENCY in dictDependencies.BO:
		obj_top_Package = dictDependencies.get_dot_py_obj(packageName)
	else:
		logger.error(f"Build package: '{packageName}' however no matching product/dependency name found.")
		sys.exit(1)
	
	if packageName not in biggusDictus:
		logger.error(f"Build package: '{packageName}' however no matching product/dependency name found in biggusDictus.")
		sys.exit(1)
	logger.debug(f"reviewPackageTree, recognised retrieved package '{packageName}'")
	
	# recursively find and build dependencies first ... and then build the specified package
	def findDepTreeAndBuild_recursive(packageName):
		#logger.debug(f"entered findDepTreeAndBuild_recursive packageName='{packageName}'")
		if 'depends_on' not in biggusDictus[packageName]:
			return
		zz_depends_on = biggusDictus[packageName]['depends_on']
		if len(zz_depends_on) <= 0:
			return
		#if boolKey(biggusDictus[packageName], "is_dep_inheriter"):
		#	return
		for d in zz_depends_on:
			#logger.debug(f"'{d}' is a child of '{packageName}'")
			sub = findDepTreeAndBuild_recursive(d)
			#logger.debug(f"*** BUILD dependency '{d}' here.")
			reviewPackage(d)	# build dependencies left-to-right in the 'depends_on', but at the bottom of each tree upward
		return
	logger.info(f"reviewPackageTree: the following package tree Dependencies are being reviewed now, before '{packageName}' aka '{obj_top_Package.name}':'")
	findDepTreeAndBuild_recursive(packageName)	# build dependencies left-to-right in the 'depends_on', but at the bottom of each tree upward
	logger.info(f"reviewPackageTree: the package tree Dependencies have been reviewed above, now we are reviewing '{packageName}' aka '{obj_top_Package.name}':'")
	reviewPackage(packageName)	# build the actual package, now that all its dependencies have been reviewed
	logger.info(f"Finished Processing reviewPackageTree '{packageName}'")
	return

###################################################################################################
def reviewPackage(packageName=''):
	# review a single package specified by name
	# NOTE:	reviewPackageTree already recursively reviews all dependencies of 'packageName',
	#		before 'packageName' gets reviewed here
	global objSETTINGS		# the SETTINGS object used everywhere
	global logging_handler 	# the handler for the logger, only used for initialization
	global logger 			# the logger object used everywhere
	global objArgParser		# the ArgParser which may be used everywhere
	global objParser		# the parser creat6ed by ArgParser which may be used everywhere
	global dictProducts		# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for PRODUCTS only, of class dot_py_object_dict
	global dictDependencies	# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for DEPENDENCIES only, of class dot_py_object_dict
	global objVariables		# an object of the variables, of class dot_py_object
	global biggusDictus		# combined dictProducts | dictDependencies
	global objPrettyPrint	# facilitates formatting and printing of text and dicts etc
	global TERMINAL_WIDTH	# for Console setup and PrettyPrint setup

	logger.info(f"Processing reviewPackage '{packageName}'")
	def dump_package_items_recursive(txt, d):
		# function to print out each field in the package structure, whether a list, dict, tuple etc.
		if type(d) is dict:	# follow the dict tree down
			#print(f"START FOLLOW DICT DOWN:  '{txt}' '{type(d)}' d={d}")
			##print(f"START FOLLOW DICT DOWN: '{txt}' '{type(d)}' d=\n{objPrettyPrint.pformat(d)}")
			for k,v in d.items():
				##print(f"item [k] type='{type(v)}' value='{v}'")
				if   type(v) is dict:	# it'll be a sub-dictionary
					#print(f"PROCESSING DICT DICT     {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' '{k}'='{v}'")
					dump_package_items_recursive(f"[{txt}][{k}]", v)	# recurse the sub-dictionary
					#print(f"PROCESSED  DICT DICT     {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' '{k}'='{v}'")
				elif type(v) is list:
					#print(f"PROCESSING DICT LIST     {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' '{k}'='{v}'")
					dump_package_items_recursive(f"[{txt}][{k}]", v)	# recurse the sub-dictionary
					#print(f"PROCESSED  DICT LIST     {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' '{k}'='{v}'")
				elif type(v) is tuple:
					#print(f"PROCESSING DICT TUPLE    {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' '{k}'='{v}'")
					dump_package_items_recursive(f"[{txt}][{k}]", v)	# recurse the sub-tuple
					#print(f"PROCESSED  DICT TUPLE    {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' '{k}'='{v}'")
				elif type(v) is str:
					#print(f"PROCESSING DICT STRING   {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' '{Colors.LIGHTMAGENTA_EX}{k}{Colors.RESET}'='{v}'")
					# do something with a string at the end of a dict
					print(f"PROCESSED  DICT STRING   {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' '{Colors.LIGHTMAGENTA_EX}{k}{Colors.RESET}'='{v}'")
					pass
				else:
					#print(f"PROCESSING DICT TYPE     {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' '{k}'='{v}' ... probably a bool or int or float")
					# is likely a base item like int, float, bool etc ... ignore it
					print(f"PROCESSED  DICT TYPE     {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' '{Colors.LIGHTMAGENTA_EX}{k}{Colors.RESET}'='{v}' ... probably a bool or int or float")
					pass
			#print(f"END   FOLLOW DICT DOWN:  '{txt}' '{type(d)}' d={d}")
			##print(f"END   FOLLOW DICT DOWN: '{txt}' '{type(d)}' d=\n{objPrettyPrint.pformat(d)}")
		elif type(d) is list:	# follow the list tree down
			#print(f"START FOLLOW LIST DOWN:  '{txt}' '{type(d)}' d={d}")
			##print(f"START FOLLOW LIST DOWN:  '{txt}' '{type(d)}' d=\n{objPrettyPrint.pformat(d)}")
			for v in d:
				##print(f"LISTitem type='{type(v)}' value='{v}'")
				if   type(v) is dict:	# it'll be a sub-dictionary
					#print(f"PROCESSING LIST DICT     {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' 'LISTitem'='{v}'")
					dump_package_items_recursive(f"[{txt}][LISTitem]", v)	# recurse the sub-dictionary
					#print(f"PROCESSED  LIST DICT     {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' 'LISTitem'='{v}'")
				elif type(v) is list:
					#print(f"PROCESSING LIST LIST     {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' 'LISTitem'='{v}'")
					dump_package_items_recursive(f"[{txt}][LISTitem]", v)	# recurse the sub-dictionary
					#print(f"PROCESSED  LIST LIST     {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' 'LISTitem'='{v}'")
				elif type(v) is tuple:
					#print(f"PROCESSING LIST TUPLE    {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' 'LISTitem'='{v}'")
					dump_package_items_recursive(f"[{txt}][LISTitem]", v)	# recurse the sub-tuple
					#print(f"PROCESSED  LIST TUPLE    {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' 'LISTitem'='{v}'")
				elif type(v) is str:
					#print(f"PROCESSING LIST STRING   {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' '{Colors.LIGHTMAGENTA_EX}LISTitem{Colors.RESET}'='{v}'")
					# do something with a string at the end of a dict
					print(f"PROCESSED  LIST STRING   {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' '{Colors.LIGHTMAGENTA_EX}LISTitem{Colors.RESET}'='{v}'")
					pass
				else:
					#print(f"PROCESSING LIST TYPE     {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' '{k}'='{v}' ... probably a bool or int or float")
					# is likely a base item like int, float, bool etc ... ignore it
					print(f"PROCESSED  LIST TYPE     {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' '{Colors.LIGHTMAGENTA_EX}{k}{Colors.RESET}'='{v}' ... probably a bool or int or float")
					pass
			#print(f"END   FOLLOW LIST DOWN:  '{txt}' '{type(d)}' d={d}")
			##print(f"END   FOLLOW LIST DOWN: '{txt}' '{type(d)}' d=\n{objPrettyPrint.pformat(d)}")
		elif type(d) is tuple:	# follow the list tree down
			#print(f"START FOLLOW TUPLE DOWN: '{txt}' '{type(d)}' d={d}")
			##print(f"START FOLLOW TUPLE DOWN: '{txt}' '{type(d)}' d=\n{objPrettyPrint.pformat(d)}")
			for v in d:
				##print(f"TUPLEitem type='{type(v)}' value='{v}'")
				if   type(v) is dict:	# it'll be a sub-dictionary
					#print(f"PROCESSING TUPLE DICT   {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' 'TUPLEitem'='{v}'")
					dump_package_items_recursive(f"[{txt}][TUPLEitem]", v)	# recurse the sub-dictionary
					#print(f"PROCESSING TUPLE DICT   {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' 'TUPLEitem'='{v}'")
				elif type(v) is list:
					#print(f"PROCESSING TUPLE LIST   {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' 'TUPLEitem'='{v}'")
					dump_package_items_recursive(f"[{txt}][TUPLEitem]", v)	# recurse the sub-dictionary
					#print(f"PROCESSED  TUPLE LIST   {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' 'TUPLEitem'='{v}'")
				elif type(v) is tuple:
					#print(f"PROCESSING TUPLE TUPLE  {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' 'TUPLEitem'='{v}'")
					dump_package_items_recursive(f"[{txt}][TUPLEitem]", v)	# recurse the sub-tuple
					#print(f"PROCESSED  TUPLE TUPLE  {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' 'TUPLEitem'='{v}'")
				elif type(v) is str:
					#print(f"PROCESSING TUPLE STRING  {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' '{Colors.LIGHTMAGENTA_EX}TUPLEitem{Colors.RESET}'='{v}'")
					# do something with a string at the end of a dict
					print(f"PROCESSED  TUPLE STRING  {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' '{Colors.LIGHTMAGENTA_EX}TUPLEitem{Colors.RESET}'='{v}'")
					pass
				else:
					#print(f"PROCESSING TUPLE TYPE    {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' '{k}'='{v}' ... probably a bool or int or float")
					# is likely a base item like int, float, bool etc ... ignore it
					print(f"PROCESSED  TUPLE TYPE    {Colors.LIGHTGREEN_EX}{txt}{Colors.RESET} '{type(v)}' '{Colors.LIGHTMAGENTA_EX}{k}{Colors.RESET}'='{v}' ... probably a bool or int or float")
					pass
			#print(f"END  FOLLOW TUPLE DOWN:  '{txt}' '{type(d)}' d={d}")
			#print(f"END  FOLLOW TUPLE DOWN:  '{txt}' '{type(d)}' d=\n{objPrettyPrint.pformat(d)}")
		else:
			#print(f"Goodness me ! EXITING ... UNKNOWN type='{type(d)}' in item to dump: '{txt}' d={d}")
			print(f"Goodness me ! EXITING ... UNKNOWN type='{type(d)}' in item to dump: '{txt}' d=\n{objPrettyPrint.pformat(d)}")
			sys.exit(1)
		return

	# get a local copy of the object being reviewed - dictPackage will be a dict
	dictPackage =  biggusDictus[packageName]

	# if debug, dump the contents of the package ... it's a jason tree of various data types
	if objSETTINGS.debugMode:
		dump_package_items_recursive(packageName, dictPackage)
	
	logger.info(f"Finished Processing reviewPackage '{packageName}'")
	return

###################################################################################################
def checkMirrors(dlLocations):
	for loc in dlLocations:
		userAgent = objSETTINGS.userAgent
		if 'sourceforge.net' in loc["url"].lower():
			userAgent = 'wget/1.20.3'  # sourceforce allows direct downloads when using wget, so we pretend we are wget
		try:
			req = requests.request("GET", loc["url"], stream=True, allow_redirects=True, headers={"User-Agent": userAgent})
		except requests.exceptions.RequestException as e:
			logger.debug(e)
		else:
			if req.status_code == 200:
				return loc
			else:
				logger.debug(loc["url"] + " unable to reach: HTTP" + str(req.status_code))
	return dlLocations[0]  # return the first if none could be found.

###################################################################################################
def getBestMirror(pkg, packageName):  # returns the first online mirror of a package, and its hash
	if "url" in pkg:
		if pkg["repo_type"] == "archive":
			logger.warning(f"getBestMirror: Package 'archive' has the old URL format, please update it.")
		return {"url": pkg["url"], "hashes": []}
	elif "download_locations" not in pkg:
		raise Exception(f"getBestMirror: download_locations not specificed for package: " + packageName)
	else:
		if not len(pkg["download_locations"]) >= 1:
			raise Exception(f"getBestMirror: download_locations is empty for package: " + packageName)
		if "url" not in pkg["download_locations"][0]:
			raise Exception(f"getBestMirror: download_location #1 of package '{packageName}' has no url specified")
		return checkMirrors(pkg["download_locations"])

###################################################################################################
def getPrimaryPackageUrl(pkg, packageName):  # returns the URL of the first download_locations entry from a package, unlike get_best_mirror this one ignores the old url format
	if "url" in pkg:
		if pkg["repo_type"] == "archive":
			logger.debug(f"getPrimaryPackageUrl: Package archive has the old URL format, please update it.")
		return replaceVarCmdSubStrings(pkg["url"])
	elif "download_locations" not in pkg:
		raise Exception(f"getPrimaryPackageUrl: download_locations in package '{packageName}' not specificed")
	else:
		if not len(pkg["download_locations"]) >= 1:
			raise Exception(f"getPrimaryPackageUrl: download_locations is empty for package")
		if "url" not in pkg["download_locations"][0]:
			raise Exception(f"getPrimaryPackageUrl: download_location #1 of package has no url specified")
		return replaceVarCmdSubStrings(pkg["download_locations"][0]["url"])  # TODO: do not assume correct format

###################################################################################################
def downloadHeader(url):
	logger.debug(f"downloadHeader: Requested download of '{url}', current path='{os.getcwd()}'")
	destination = objSETTINGS.targetPrefix.joinpath("include")
	fileName = os.path.basename(urlparse(url).path)
	full_destination_file = os.path.join(destination, fileName)
	# 2023.04.03 FORCE a re-download of headers since they may have changed.
	#if not os.path.isfile(os.path.join(destination, fileName)):
	#	logger.debug(f"downloadHeader: Downloading '{url}', current path='{os.getcwd()}'")
	#	fname = downloadFile(url)
	#	logger.debug(f"downloadHeader: Moving Header File: '{fname}' to '{destination}', current path='{os.getcwd()}'")
	#	shutil.move(fname, destination)
	#else:
	#	logger.debug(f"downloadHeader: Header File: '{fileName}' already downloaded, current path='{os.getcwd()}'")
	#
	logger.debug(f"downloadHeader: (always) Downloading '{url}', current path='{os.getcwd()}'")
	fname = downloadFile(url)
	logger.debug(f"downloadHeader: Moving (with overwrite) Header File: '{fname}' to '{full_destination_file}', current path='{os.getcwd()}'")
	# In order for shutil.move to OVERWRITE destination file (if one already exists in destination path),
	# we need to specify FULL destination path and filename, and NOT only destination folder name, or it will raise an Exception
	# for example C:\Users\user\Downloads\python-2.7.17.msi
	# see https://geekdudes.wordpress.com/2020/01/14/python-move-and-replace-if-same-file-already-exist/
	shutil.move(fname, full_destination_file)	# move with overwrite since we specify the full path and filename

###################################################################################################
def downloadFile(url=None, outputFileName=None, outputPath=None, bytesMode=False):
	def fmt_size(num, suffix="B"):
			for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
				if abs(num) < 1024.0:
					return "%3.1f%s%s" % (num, unit, suffix)
				num /= 1024.0
			return "%.1f%s%s" % (num, "Yi", suffix)
	
	if not url:
		raise Exception(f"downloadFile: No URL specified.")

	if outputPath is None:  # Default to current dir.
		outputPath = os.getcwd()
	else:
		if not os.path.isdir(outputPath):
			raise Exception(f"downloadFile: Specified path '{outputPath}' does not exist")

	fileName = os.path.basename(url)  # Get URL filename

	if 'sourceforge.net' in url.lower():
		userAgent = 'wget/1.18'  # sourceforce <3 wget
	else:
		userAgent = objSETTINGS.userAgent

	if url.lower().startswith("ftp://"):
		logger.info(f"downloadFile: downloadFileRequesting : {url}")
		if outputFileName is not None:
			fileName = outputFileName
		fullOutputPath = os.path.join(outputPath, fileName)
		urllib.request.urlretrieve(url, fullOutputPath)
		return fullOutputPath

	if url.lower().startswith("file://"):
		url = url.replace("file://", "")
		logger.info(f"downloadFile: Copying : {url}")
		if outputFileName is not None:
			fileName = outputFileName
		fullOutputPath = os.path.join(outputPath, fileName)
		try:
			logger.debug(f"cp -f '{url}' '{fullOutputPath}' # copy file ")
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

	logger.info(f"downloadFile: Requesting : {url} - {fmt_size(size) if size is not None else '?'}")

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
def touch(f):
	Path(f).touch()

###################################################################################################
def chmodPux(file):
	st = os.stat(file)
	os.chmod(file, st.st_mode | stat.S_IXUSR)  # S_IEXEC would be just +x
		
###################################################################################################
def md5(*args):
	msg = ''.join(args).encode("utf-8")
	m = hashlib.md5()
	m.update(msg)
	return m.hexdigest()

###################################################################################################
def hashFile(fname, type="sha256"):
	hash = None
	if type == "sha256":
		hash = hashlib.sha256()
	elif type == "sha512":
		hash = hashlib.sha512()
	elif type == "md5":
		hash = hashlib.md5()
	elif type == "blake2b":
		hash = hashlib.blake2b()
	with open(fname, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash.update(chunk)
	return hash.hexdigest()

###################################################################################################
def verifyHash(file, hash):
	if hash["type"] not in ["sha256", "sha512", "md5", "blake2b"]:
		raise Exception(f"verifyHash: Unsupported hash type: " + hash["type"])
	newHash = hashFile(file, hash["type"])
	if hash["sum"] == newHash:
		return (True, hash["sum"], newHash)
	return (False, hash["sum"], newHash)

###################################################################################################
def downloadUnpackFile(pkg, packageName, folderName=None, workDir=None):
	customFolder = False
	if folderName is None:
		folderName = os.path.basename(os.path.splitext(urlparse(getPrimaryPackageUrl(pkg, packageName)).path)[0]).rstrip(".tar")
	else:
		customFolder = True
	folderToCheck = folderName

	if "rename_folder" in pkg and pkg["rename_folder"] != "" and pkg["rename_folder"] is not None:
		folderToCheck = pkg["rename_folder"]

	if workDir is not None:
		folderToCheck = workDir

	check_file = os.path.join(folderToCheck, "unpacked.successfully")
	if not os.path.isfile(check_file):
		dlLocation = getBestMirror(pkg, packageName)
		url = dlLocation["url"]
		fileName = os.path.basename(urlparse(url).path)
		logger.info(f"downloadUnpackFile: Downloading {fileName} ({url})")

		cchdir(".")
		logger.debug(f"downloadUnpackFile: Downloading {url} to ({fileName})")
		downloadFile(url, fileName)
			
		if "hashes" in dlLocation:
			if len(dlLocation["hashes"]) >= 1:
				for hash in dlLocation["hashes"]:
					logger.info(f"downloadUnpackFile: Comparing hashes..")
					hashReturn = verifyHash(fileName, hash)
					if hashReturn[0] is True:
						logger.info(f"downloadUnpackFile: Hashes matched: {hashReturn[1][0:5]}...{hashReturn[1][-5:]} (local) == {hashReturn[2][0:5]}...{hashReturn[2][-5:]} (remote)")
					else:
						logger.error(f"downloadUnpackFile: File hashes didn't match: {hashReturn[1]}(local) != {hashReturn[2]}(remote)")
						raise Exception(f"downloadUnpackFile: File download error: Hash mismatch")
						exit(1)

		logger.info(f"downloadUnpackFile: Unpacking {fileName}")

		tars = (".gz", ".bz2", ".xz", ".bz", ".tgz")  # i really need a better system for this.. but in reality, those are probably the only formats we will ever encounter.

		customFolderTarArg = ""

		if customFolder:
			logger.debug(f"downloadUnpackFile: making folder '{folderName}' ...")
			customFolderTarArg = ' -C "' + folderName + '" --strip-components 1'
			# IF FOLDER EXISTS, DELETE IT BEFORE CREATING IT
			#    rmdir(path) Remove (delete) the directory path. Only works when the directory is empty, otherwise, OSError is raised. 
			#    In order to remove whole directory trees, shutil.rmtree() can be used.
			if os.path.isdir(folderName):
				logger.debug(f"downloadUnpackFile: In customFolder, deleting old existing folder '{folderName}'")
				logger.debug(f"downloadUnpackFile: rm -f '{folderName}'")
				shutil.rmtree(folderName,ignore_errors=False)
			os.makedirs(folderName) # os.makedirs creates intermediate parent paths like "mkdir -p"

		if fileName.endswith(tars):
			logger.debug(f"downloadUnpackFile: tar -vxf '{fileName}' {customFolderTarArg}")	# 2023.04.09 added "v" to make "-vxf"
			runProcess(f"tar -vxf '{fileName}' {customFolderTarArg}")
		else:
			logger.debug(f"downloadUnpackFile: unzip '{fileName}'")
			runProcess(f"unzip '{fileName}'")

		touch(os.path.join(folderName, "unpacked.successfully"))

		os.remove(fileName)

		return folderName

	else:
		logger.debug(f"downloadUnpackFile: {folderName} already downloaded")
		return folderName

###################################################################################################
def sanitizeFilename(f):
	return re.sub(r'[/\\:*?"<>|]', '', f)

###################################################################################################
def gitClone(url, virtFolderName=None, renameTo=None, desiredBranch=None, recursive=False, doNotUpdate=False, desiredPR=None, git_depth=-1):
	logger.info(f"gitClone: Processing gitClone '{Colors.LIGHTMAGENTA_EX}{url}{Colors.RESET}' in '{os.getcwd()}'")
	if virtFolderName is None:
		virtFolderName = sanitizeFilename(os.path.basename(url))
		if not virtFolderName.endswith(".git"):
			virtFolderName += ".git"
		virtFolderName = virtFolderName.replace(".git", "_git")
	else:
		virtFolderName = sanitizeFilename(virtFolderName)

	realFolderName = virtFolderName
	if renameTo is not None:
		realFolderName = renameTo

	branchString = ""
	if desiredBranch is not None:
		desiredBranch = replaceVarCmdSubStrings(desiredBranch)
		branchString = f" {desiredBranch}"

	properBranchString = "master"  # 2020.06.22 if trunk moves to "main", use "'branch' : 'main'," in the product/dependency .py file
	if desiredBranch is not None:
		properBranchString = desiredBranch
		properBranchString = replaceVarCmdSubStrings(properBranchString)	# 2023.02.13 ADDED replaceVarCmdSubStrings

	if os.path.isdir(realFolderName):
		logger.debug(f"gitClone: folder {realFolderName} already exists, will check for updates, current path='{os.getcwd()}'")
		if desiredPR is not None:
			logger.warning(f"gitClone: ###############################################################################################")
			logger.warning(f"gitClone: Git: repositiories with set PR will not auto-update, please delete the repo and retry to do so.")
			logger.warning(f"gitClone: ###############################################################################################")
		elif doNotUpdate is True:
			logger.warning(f"gitClone: #########################")
			logger.warning(f"gitClone: do_not_git_update is True")
			logger.warning(f"gitClone: #########################")
		else:
			logger.info(f"gitClone: (desiredPR is None) and (doNotUpdate is False)" )
			cchdir(realFolderName)
			logger.info(f"gitClone: git remote update")
			runProcess(f"git remote update")
			UPSTREAM = '@{u}'  # or branchName i guess
			if desiredBranch is not None:
				UPSTREAM = properBranchString
			LOCAL = subprocess.check_output(f"git rev-parse @", shell=True).decode("utf-8")
			REMOTE = subprocess.check_output(f'git rev-parse "{UPSTREAM}"', shell=True).decode("utf-8")
			BASE = subprocess.check_output(f'git merge-base @ "{UPSTREAM}"', shell=True).decode("utf-8")
			logger.info(f"gitClone: git checkout -f")
			runProcess(f"git checkout -f")
			logger.info(f"gitClone: git checkout {properBranchString}")
			runProcess(f"git checkout {properBranchString}")
			if LOCAL == REMOTE:
				logger.debug(f"gitClone: ####################")
				logger.debug(f"gitClone: Up to date")
				logger.debug(f"gitClone: LOCAL:  " + LOCAL)
				logger.debug(f"gitClone: REMOTE: " + REMOTE)
				logger.debug(f"gitClone: BASE:   " + BASE)
				logger.debug(f"gitClone: ####################")
				#cchdir("..")
				#logger.debug(f"gitClone: WILL NOT return with return_value={os.getcwd()}, current path='{os.getcwd()}'")
				#return realFolderName	# 2023.04.02 added this here to see if we can stop rebuilding every time
				#logger.debug(f"gitClone: DID NOT return with return_value={os.getcwd()}, current path='{os.getcwd()}'")
			elif LOCAL == BASE:
				logger.debug(f"gitClone: ####################")
				logger.debug(f"gitClone: Need to pull")
				logger.debug(f"gitClone: gitClone: LOCAL:  " + LOCAL)
				logger.debug(f"REMOTE: " + REMOTE)
				logger.debug(f"gitClone: BASE:   " + BASE)
				logger.debug(f"gitClone: ####################")
				if desiredBranch is not None:
					# bsSplit = properBranchString.split("/")
					# if len(bsSplit) == 2:
					# 	run_process("git pull origin {1}'.format(bsSplit[0],bsSplit[1])) ???
					# else:
					logger.info(f"gitClone: About to 'git pull origin {properBranchString}' # with desiredBranch='{desiredBranch}' properBranchString'{properBranchString}'")
					if 'Already up to date' in runProcess(f"git pull origin {properBranchString}", silent=True):
						logger.info(f"gitClone: Already up to date with branch desiredBranch='{desiredBranch}' properBranchString'{properBranchString}'")
						#return os.getcwd()
						cchdir("..")
						return realFolderName
					else:
						logger.info(f"gitClone: was NOT up to date with desiredBranch='{desiredBranch}' properBranchString'{properBranchString}' until that pull")
				else:
					logger.info(f"gitClone: git pull ") #.format(properBranchString))	# ??? HMMM, no variable for properBranchString to go into means it is ignored ... could be a bug ?
					runProcess(f"git pull ") #.format(properBranchString))				# ??? HMMM, no variable for properBranchString to go into means it is ignored ... could be a bug ?
				logger.info(f"gitClone: git clean -ffdx")  # https://gist.github.com/nicktoumpelis/11214362
				runProcess(f"git clean -ffdx")  # https://gist.github.com/nicktoumpelis/11214362
				logger.info(f"gitClone: git submodule foreach --recursive git clean -ffdx")
				runProcess(f"git submodule foreach --recursive git clean -ffdx")
				logger.info(f"gitClone: git reset --hard")
				runProcess(f"git reset --hard")
				logger.info(f"gitClone: git submodule foreach --recursive git reset --hard")
				runProcess(f"git submodule foreach --recursive git reset --hard")
				logger.info(f"gitClone: git submodule update --init --recursive")
				runProcess(f"git submodule update --init --recursive")
			elif REMOTE == BASE:
				logger.debug(f"gitClone: ####################")
				logger.debug(f"gitClone: need to push")
				logger.debug(f"gitClone: LOCAL:  " + LOCAL)
				logger.debug(f"gitClone: REMOTE: " + REMOTE)
				logger.debug(f"gitClone: BASE:   " + BASE)
				logger.debug(f"gitClone: ####################")
			else:
				logger.debug(f"gitClone: ####################")
				logger.debug(f"gitClone: diverged?")
				logger.debug(f"gitClone: LOCAL:  " + LOCAL)
				logger.debug(f"gitClone: REMOTE: " + REMOTE)
				logger.debug(f"gitClone: BASE	" + BASE)
				logger.debug(f"gitClone: ####################")
			cchdir("..")
			logger.info(f"gitClone: where folder exists, Finished GIT cloning '(url)' to '(realFolderName)', current path='{os.getcwd()}' ")
	else:
		logger.debug(f"gitClone: folder {realFolderName} does NOT  exist, current path='{os.getcwd()}'")
		logger.debug(f"gitClone: Initial GIT cloning '{url}' to '{realFolderName}', current path='{os.getcwd()}'")
		addArgs = []
		if recursive:
			addArgs.append("--recursive")
		#
		if git_depth and git_depth >= 1:
			addArgs.append(F"--depth {git_depth}")
		elif git_depth is None or git_depth < 0:
			git_depth = 1
			addArgs.append(F"--depth 1")
		logger.info(F"Git {'Shallow C' if git_depth >= 1 else 'C'}loning '{url}' to '{os.getcwd() + '/' + realFolderName}'")
		# 2023.04.09 from deadsiz27
		tmpPath = Path(os.getcwd() + '/' + realFolderName + ".tmp")
		if tmpPath.exists():
			logger.info(F"gitClone: Deleting leftover git tmp path: {tmpPath}")
			shutil.rmtree(tmpPath)
		#
		logger.debug(f"git clone {' '.join(addArgs)} --progress '{url}' '{realFolderName + '.tmp'}'")
		runProcess(f"git clone {' '.join(addArgs)} --progress '{url}' '{realFolderName + '.tmp'}'")
		if desiredBranch is not None:
			cchdir(realFolderName + ".tmp")
			logger.debug(f"gitClone: GIT Checking out:{' master' if desiredBranch is None else branchString}")
			logger.info(f"gitClone: git checkout{' master' if desiredBranch is None else branchString}")
			runProcess(f"git checkout{' master' if desiredBranch is None else branchString}")
			cchdir("..")
		if desiredPR is not None:
			cchdir(realFolderName + ".tmp")
			logger.info(f"gitClone: GIT Fetching PR: {desiredPR}")
			logger.info(f"gitClone: git fetch origin refs/pull/{desiredPR}/head")
			runProcess(f"git fetch origin refs/pull/{desiredPR}/head")
			cchdir("..")
		logger.info(f"gitClone: before mv, current path='{os.getcwd()}'")
		logger.info(f"gitClone: mv '{realFolderName + '.tmp'}' '{realFolderName}'")
		runProcess(f"mv '{realFolderName + '.tmp'}' '{realFolderName}'")
		#logger.debug(f"gitClone: Finished GIT cloning '{url}' to '{realFolderName}'")

	logger.info(f"gitClone: At END, Finished GIT cloning '{url}' to '{realFolderName}' returning with return_value={realFolderName}, current path='{os.getcwd()}'")
	return realFolderName

###################################################################################################
def svnClone(url, dir, desiredBranch=None):
	logger.info(f"svnClone: Processing svnClone '{Colors.LIGHTMAGENTA_EX}{url}{Colors.RESET}'")
	dir = sanitizeFilename(dir)
	if not dir.endswith("_svn"):
		dir += "_svn"
	if not os.path.isdir(dir):
		logger.info(f"svnClone: SVN checking out to '{dir}'.tmp then moving to '{dir}'")
		if desiredBranch is None:
			logger.info(f"svnClone: svn co '{url}' '{dir}.tmp' --non-interactive --trust-server-cert")
			runProcess(f"svnClone: svn co '{url}' '{dir}.tmp' --non-interactive --trust-server-cert")
		else:
			desiredBranch = replaceVarCmdSubStrings(desiredBranch)
			#branchString = f" {desiredBranch}"
			logger.info(f"svnClone: svn co -r '(desiredBranch)' '{url}' '{url}.tmp' --non-interactive --trust-server-cert")
			runProcess(f"svn co -r '(desiredBranch)' '{url}' '{url}.tmp' --non-interactive --trust-server-cert")
		logger.info(f"svnClone: mv -f '{dir}.tmp' '{dir}'")
		shutil.move(f"{dir}.tmp", dir) 
	else:
		pass
	return dir

###################################################################################################
def mercurialClone(url, virtFolderName=None, renameTo=None, desiredBranch=None, forceRebuild=False):
	logger.info(f"mercurialClone: Processing mercurialClone '{Colors.LIGHTMAGENTA_EX}{url}{Colors.RESET}'")
	if objArgParser.allforce:
		forceRebuild = True
	if virtFolderName is None:
		virtFolderName = sanitizeFilename(os.path.basename(url))
		if not virtFolderName.endswith(".hg"):
			virtFolderName += ".hg"
		virtFolderName = virtFolderName.replace(".hg", "_hg")
	else:
		virtFolderName = sanitizeFilename(virtFolderName)
	realFolderName = virtFolderName
	if renameTo is not None:
		realFolderName = renameTo
	branchString = ""
	if desiredBranch is not None:
		desiredBranch = replaceVarCmdSubStrings(desiredBranch)
		#branchString = f" {desiredBranch}"
	# we have to do it the hard way because "hg purge" is an extension that is not on by default
	# and making users enable stuff like that is too much
	if os.path.isdir(realFolderName) and forceRebuild:
		logger.info(f"mercurialClone: Deleting old HG clone in folder '{realFolderName}'")
		shutil.rmtree(realFolderName,ignore_errors=False)
	if os.path.isdir(realFolderName):
		cchdir(realFolderName)
		logger.info(f"mercurialClone: hg --debug id -i")
		hgVersion = subprocess.check_output("hg --debug id -i", shell=True)
		logger.info(f"mercurialClone: hg pull -u")
		runProcess(f"hg pull -u")
		#logger.info(f"mercurialClone: hg update -C{' default' if desiredBranch is None else branchString}"   .format(' default' if desiredBranch is None else branchString))
		logger.info(f"mercurialClone: hg update -C{' default' if desiredBranch is None else branchString}")
		runProcess(f"hg update -C{' default' if desiredBranch is None else branchString}")
		hgVersionNew = subprocess.check_output(f"hg --debug id -i", shell=True)
		if hgVersion != hgVersionNew:
			logger.debug(f"mercurialClone: HG clone has code changes, updating")
			removeAlreadyFiles()
		else:
			logger.debug(f"mercurialClone: HG clone already up to date")
		cchdir("..")
	else:
		logger.info(f"mercurialClone: HG cloning '{url}' to '{realFolderName + '.tmp'}'")
		logger.debug(f"mercurialClone: hg clone {url} {realFolderName + '.tmp'}")
		runProcess(f"hg clone {url} {realFolderName + '.tmp'}")
		if desiredBranch is not None:
			cchdir(realFolderName + '.tmp')
			logger.debug(f"mercurialClone: HG updating to:{' master' if desiredBranch is None else branchString}")
			logger.debug(f"mercurialClone: hg up{' master' if desiredBranch is None else branchString} -v")
			runProcess(f"hg up{' master' if desiredBranch is None else branchString} -v'")
			cchdir("..")
		logger.debug(f"mercurialClone: mv -f '{realFolderName + '.tmp'}' '{realFolderName}'")
		runProcess(f"mv '{realFolderName + '.tmp'}' '{realFolderName}'")
	logger.info(f"mercurialClone: Finished HG cloning '{url}' to 'realFolderName'")
	return realFolderName

###################################################################################################
def cmakeSource(packageName, pkg):
	logger.info(f"cmakeSource: Processing '{packageName}'")

	if objSETTINGS.debugMode:
		print("### cmakeSource: Environment variables:  ###")
		for tk in os.environ:
			print("\t" + tk + " : " + os.environ[tk])
		print("############################################")
	touchName = f"already_ran_cmake_{md5(packageName, getKeyOrBlankString(pkg,'configure_options'))}"
	if not os.path.isfile(touchName):
		logger.debug(f"cmakeSource: already_ran_cmake '{touchName}' NOT detected, running cmake")
		removeAlreadyFiles()
		makeOpts = ''
		if 'configure_options' in pkg:
			if pkg["configure_options"] is not None:
				makeOpts = replaceVarCmdSubStrings(pkg["configure_options"])
		logger.info(f"cmakeSource:  C-Making '{packageName}' with: {makeOpts}")
		logger.info(f"cmakeSource: cmake {makeOpts}")
		runProcess(f'cmake {makeOpts}')
		logger.debug(f"cmakeSource: make clean")
		runProcess(f"make clean", True)
		if 'regex_replace' in pkg and pkg['regex_replace']:
			_pos = 'post_configure'
			if isinstance(pkg['regex_replace'], dict) and _pos in pkg['regex_replace']:
				for r in pkg['regex_replace'][_pos]:
					handleRegexReplace(r, packageName)
		touch(touchName)
	else:
		logger.debug(f"cmakeSource: already_ran_cmake '{touchName}' detected, not running cmake")

###################################################################################################
def mesonSource(packageName, pkg):
	logger.info(f"mesonSource: Processing '{packageName}'")
	touchName = f"already_ran_meson_%s" % (md5(packageName, getKeyOrBlankString(pkg, "configure_options	")))
	if not os.path.isfile(touchName):
		removeAlreadyFiles()
		makeOpts = ''
		if 'configure_options' in pkg:
			makeOpts = replaceVarCmdSubStrings(pkg["configure_options"])
		logger.info(f"mesonSource: Meson-ing '{packageName}' with: '{makeOpts}'")
		logger.info(f"mesonSource: meson setup {makeOpts}")
		runProcess(f"meson setup {makeOpts}")
		if 'regex_replace' in pkg and pkg['regex_replace']:
			_pos = 'post_configure'
			if isinstance(pkg['regex_replace'], dict) and _pos in pkg['regex_replace']:
				for r in pkg['regex_replace'][_pos]:
					handleRegexReplace(r, packageName)
		touch(touchName)
	else:
		logger.debug(f"mesonSource: already_ran_meson '{touchName}' detected, not running meson")
	# 2023.04.09 'run_post_configure' added per deadsix27 ... should we run this now or not ?  Perhaps it should not run twice ?  Run it anyway.
	if 'run_post_configure' in pkg:
		logger.debug(f"mesonSource: run_post_configure detected.")
		if pkg['run_post_configure'] is not None:
			for cmd in pkg['run_post_configure']:
				logger.debug(f"mesonSource: run_post_configure found cmd='{cmd}'")
				if cmd.startswith("!SWITCHDIRBACK"):
					logger.debug(f"mesonSource: run_post_configure '!SWITCHDIRBACK' detected to change directory" )
					cchdir(_origDir)
				elif cmd.startswith("!SWITCHDIR"):
					logger.debug(f"mesonSource: run_post_configure '!SWITCHDIR' detected to change directory" )
					_dir = replaceVarCmdSubStrings("|".join(cmd.split("|")[1:]))
					cchdir(_dir)
				else:
					cmd = replaceVarCmdSubStrings(cmd)
					logger.info(f"mesonSource: Running meson run_post_configure cmd='{cmd}'")
					runProcess(cmd)

###################################################################################################
def installSource(packageName, pkg, buildSystem):
	logger.info(f"installSource: Processing '{packageName}'")
	_origDir = os.getcwd()
	touchName = f"already_ran_install_{md5(packageName, getKeyOrBlankString(pkg, 'install_options'))}"
	if not os.path.isfile(touchName):
		logger.debug(f"installSource: already_ran_install '{touchName}' NOT detected, running installer")
		cpuCountStr = f"-j {objSETTINGS.cpuCount}"
		if 'cpu_count' in pkg:
			if isinstance(pkg['cpu_count'], int):
				if pkg['cpu_count'] > 0:
					cpuCountStr = f"-j {pkg['cpu_count']}"
				#else:
				#	cpuCountStr = ""
		makeInstallOpts = ''
		if 'install_options' in pkg:
			if pkg['install_options'] is not None:
				makeInstallOpts = replaceVarCmdSubStrings(pkg["install_options"])
		installTarget = "install"
		if 'install_target' in pkg:
			if pkg['install_target'] is not None:
				installTarget = replaceVarCmdSubStrings(pkg['install_target'])
		logger.info(f"installSource: Installing '{packageName}' with install_options: '{makeInstallOpts}'", extra={'type': buildSystem})
		mkCmd = "make"
		if buildSystem == "waf":
			mkCmd = "./waf"
		if buildSystem == "rake":
			mkCmd = "rake"
		if buildSystem == "ninja":
			mkCmd = "ninja"
		if buildSystem == "rust":
			mkCmd = "cargo"

		logger.info(f"installSource: I{mkCmd} {installTarget} {makeInstallOpts} {cpuCountStr}")
		runProcess(f"{mkCmd} {installTarget} {makeInstallOpts} {cpuCountStr}")
		if 'regex_replace' in pkg and pkg['regex_replace']:
			_pos = 'post_install'
			if isinstance(pkg['regex_replace'], dict) and _pos in pkg['regex_replace']:
				for r in pkg['regex_replace'][_pos]:
					handleRegexReplace(r, packageName)
		if 'run_post_install' in pkg:
			if pkg['run_post_install'] is not None:
				for cmd in pkg['run_post_install']:
					if cmd.startswith("!SWITCHDIRBACK"):
						cchdir(_origDir)
					elif cmd.startswith("!SWITCHDIR"):
						_dir = replaceVarCmdSubStrings("|".join(cmd.split("|")[1:]))
						cchdir(_dir)
					else:
						logger.info(f"installSource: Running post-install-command pre replaceVarCmdSubStrings (raw): '{cmd}'") # 2023.04.02
						cmd = replaceVarCmdSubStrings(cmd)
						logger.info(f"installSource: Running post-install-command: '{cmd}'") # 2023.04.02
						logger.info(cmd)
						runProcess(cmd)
		touch(touchName)
	else:
		logger.debug(f"installSource: already_ran_install '{touchName}' detected, not running installer")

###################################################################################################
def configureSource(packageName, pkg, conf_system):
	logger.info(f"configureSource: Processing '{packageName}'")
	touchName = f"already_configured_{md5(packageName, getKeyOrBlankString(pkg, 'configure_options'))}"
	if not os.path.isfile(touchName):
		logger.debug(f"configureSource: already_ran_configure '{touchName}' NOT detected, running configurer")
		cpuCountStr = f"-j {objSETTINGS.cpuCount}"
		if 'cpu_count' in pkg:
			if isinstance(pkg['cpu_count'], int):
				if pkg['cpu_count'] > 0:
					cpuCountStr = f"-j {pkg['cpu_count']}"
				#else:
				#	cpuCountStr = ""
		removeAlreadyFiles()
		removeConfigPatchDoneFiles()
		doBootStrap = True
		if 'do_not_bootstrap' in pkg:
			if pkg['do_not_bootstrap'] is True:
				doBootStrap = False
		if doBootStrap:
			if conf_system == "waf":
				if not os.path.isfile("waf"):
					if os.path.isfile("bootstrap.py"):
						logger.info(f"configureSource: ./bootstrap.py")
						runProcess(f"./bootstrap.py")
			else:
				bootstrapConfigure()
		configOpts = ''
		if 'configure_options' in pkg:
			try:
				configOpts = replaceVarCmdSubStrings(pkg["configure_options"])
			except KeyError as e:
				errorExit(f"configureSource: Failed to parse configure line: '{pkg['configure_options']}', the variable {e} is invalid.")
		logger.info(f"configureSource: Configuring '{packageName}' with: '{configOpts}'", extra={'type': conf_system})
		confCmd = './configure'
		if conf_system == "waf":
			confCmd = './waf --color=yes configure'
		elif 'configure_path' in pkg:
			if pkg['configure_path'] is not None:
				confCmd = pkg['configure_path']
		logger.info(f"configureSource: {confCmd} {configOpts}")
		runProcess(f"{confCmd} {configOpts}")
		if 'regex_replace' in pkg and pkg['regex_replace']:
			_pos = 'post_configure'
			if isinstance(pkg['regex_replace'], dict) and _pos in pkg['regex_replace']:
				for r in pkg['regex_replace'][_pos]:
					handleRegexReplace(r, packageName)
		if 'run_post_configure' in pkg:
			if pkg['run_post_configure'] is not None:
				for cmd in pkg['run_post_configure']:
					logger.debug(f"configureSource: Running post-configure-command pre replaceVarCmdSubStrings (raw): '{cmd}'")
					cmd = replaceVarCmdSubStrings(cmd)
					logger.info(f"configureSource: Running post-configure-command: '{cmd}'")
					logger.debug(cmd)
					runProcess(cmd)
		doClean = True
		if 'clean_post_configure' in pkg:
			if pkg['clean_post_configure'] is False:
				doClean = False
		if doClean:
			mCleanCmd = 'make clean'
			if conf_system == "waf":
				mCleanCmd = './waf --color=yes clean'
			logger.info(f"configureSource: {mCleanCmd} {cpuCountStr}")
			runProcess(f"{mCleanCmd} {cpuCountStr}", True)
		if 'patches_post_configure' in pkg:
			if pkg['patches_post_configure'] is not None:
				for p in pkg['patches_post_configure']:
					applyPatch(p[0], p[1], True)
		touch(touchName)
	else:
		logger.debug(f"configureSource: already_ran_configure '{touchName}' detected, not running configurer")

###################################################################################################
def buildSource(packageName, pkg, buildSystem):
	logger.info(f"buildSource: Processing '{packageName}'")
	_origDir = os.getcwd()
	touchName = f"already_ran_make_{md5(packageName, getKeyOrBlankString(pkg, 'build_options'))}"
	if not os.path.isfile(touchName):
		logger.debug(f"buildSource: already_ran_build '{touchName}' NOT detected, running make/ninja/etc")
		cpuCountStr = f"-j {objSETTINGS.cpuCount}"
		if 'cpu_count' in pkg:
			if isinstance(pkg['cpu_count'], int):
				if pkg['cpu_count'] > 0:
					cpuCountStr = f"-j {pkg['cpu_count']}"
				#else:
				#	cpuCountStr = ""
		mkCmd = 'make'
		if buildSystem == "waf":
			mkCmd = './waf --color=yes'
		if buildSystem == "rake":
			mkCmd = 'rake'
		if buildSystem == "ninja":
			mkCmd = 'ninja'
		if buildSystem == "rust":
			mkCmd = 'cargo'

		if buildSystem == "make":
			if os.path.isfile("configure"):
				logger.info(f"{mkCmd} clean {cpuCountStr}")
				runProcess(f"{mkCmd} clean {cpuCountStr}", True)
		#if buildSystem == "ninja":
		#	if os.path.isfile("meson.build"):
		#		logger.info(F'{mkCmd} clean ') # -C builddir 
		#		runProcess(F'{mkCmd} clean ', True) #-C builddir 
		makeOpts = ''
		if 'build_options' in pkg:
			makeOpts = replaceVarCmdSubStrings(pkg["build_options"])
		dump_environment_variables(override=False)
		logger.info(f"buildSource: Building '{packageName}' with build_options: '{makeOpts}' in '{os.getcwd()}'", extra={'type': buildSystem})
		if 'run_pre_build' in pkg and pkg['run_pre_build']:
			logger.debug(f"buildSource: run_pre_build detected.")
			for cmd in pkg['run_pre_build']:
				logger.debug(f"buildSource: run_post_configure found cmd='{cmd}'")
				ignoreFail = False
				if isinstance(cmd, tuple):
					cmd = cmd[0]
					ignoreFail = cmd[1]
				if cmd.startswith("!SWITCHDIRBACK"):
					logger.debug(f"buildSource: run_pre_build '!SWITCHDIRBACK' detected to change directory" )
					cchdir(currentFullDir)
				elif cmd.startswith("!SWITCHDIR"):
					logger.debug(f"buildSource: run_pre_build '!SWITCHDIR' detected to change directory" )
					_dir = replaceVarCmdSubStrings("|".join(cmd.split("|")[1:])) ?????????
					cchdir(_dir)
				else:
					cmd = replaceVarCmdSubStrings(cmd)
					logger.info(f"buildSource: Running run_pre_build cmd='{cmd}'")
					runProcess(cmd, ignoreFail)
		if 'ignore_build_fail_and_run' in pkg:
			if len(pkg['ignore_build_fail_and_run']) > 0:  # todo check if its a list too
				try:
					if buildSystem == "waf":
						mkCmd = './waf --color=yes build'
					logger.info(f"buildSource: {mkCmd} {cpuCountStr} {makeOpts}")
					runProcess(f"{mkCmd} {cpuCountStr} {makeOpts}")
				except Exception:  # todo, except specific exception
					logger.info(f"buildSource: Ignoring failed make process...")
					for cmd in pkg['ignore_build_fail_and_run']:
						cmd = replaceVarCmdSubStrings(cmd)
						logger.info(f"buildSource: Running post-failed-make-command: '{cmd}'")
						runProcess(cmd)
		else:
			elif buildSystem == "rust":
				#os.system(f'{mkCmd} {cpuCountStr} {makeOpts}')
				runProcess(f'{mkCmd} {cpuCountStr} {makeOpts}')
			else:
				elif buildSystem == "waf":
					mkCmd = './waf --color=yes build'
				logger.info(f"buildSource: {mkCmd} {cpuCountStr} {makeOpts}")
				runProcess(f"{mkCmd} {cpuCountStr} {makeOpts}")
		if 'regex_replace' in pkg and pkg['regex_replace']:
			_pos = 'post_build'
			if isinstance(pkg['regex_replace'], dict) and _pos in pkg['regex_replace']:
				for r in pkg['regex_replace'][_pos]:
					handleRegexReplace(r, packageName)
		if 'run_post_build' in pkg:
			if pkg['run_post_build'] is not None:
				for cmd in pkg['run_post_build']:
					if cmd.startswith("!SWITCHDIRBACK"):
						cchdir(_origDir)
					elif cmd.startswith("!SWITCHDIR"):
						_dir = replaceVarCmdSubStrings("|".join(cmd.split("|")[1:]))
						cchdir(_dir)
					else:
						cmd = replaceVarCmdSubStrings(cmd)
						logger.info(f"buildSource: Running post-build-command: '{cmd}'")
						logger.info(cmd)
						runProcess(cmd)
		touch(touchName)
	else:
		logger.debug(f"buildSource: already_ran_build '{touchName}' detected, not running make/ninja/etc")

###################################################################################################
def bootstrapConfigure():
	if not os.path.isfile(f"configure"):
		if os.path.isfile(f"bootstrap.sh"):
			logger.info(f"bootstrapConfigure: ./bootstrap.sh")
			runProcess(f"./bootstrap.sh")
		elif os.path.isfile(f"autogen.sh"):
			logger.info(f"bootstrapConfigure: ./autogen.sh")
			runProcess(f"./autogen.sh")
		elif os.path.isfile(f"buildconf"):
			logger.info(f"bootstrapConfigure: ./buildconf")
			runProcess(f"./buildconf")
		elif os.path.isfile(f"bootstrap"):
			logger.info(f"bootstrapConfigure: ./bootstrap")
			runProcess(f"./bootstrap")
		elif os.path.isfile(f"bootstrap"):
			logger.info(f"bootstrapConfigure: ./bootstrap")
			runProcess(f"./bootstrap")
		elif os.path.isfile(f"configure.ac"):
			logger.info(f"bootstrapConfigure: autoreconf -fiv")
			runProcess(f"autoreconf -fiv")
		else:
			logger.debug(f"bootstrapConfigure: all boostrappers not detected, not running bootstrapper")
	else:
		logger.debug(f"bootstrapConfigure: configure not detected, not running bootstrapper")

###################################################################################################
def applyPatchv2(patchData):		# the incoming patch is a dict (key/value pairs)
	url = patchData["file"]									# key is "file"
	originalFolder = os.getcwd()
	if "dir" in patchData and patchData["dir"] is not None:	# key is "dir"
		cchdir(patchData["dir"])	
		logger.debug(f"applyPatchv2: Moved into patch folder: '{os.getcwd()}'")
	logger.debug(f"applyPatchv2: Applying patch '{url}' in '{os.getcwd()}'")
	patchTouchName = f"patch_{md5(url)}.done"
	ignoreErr = False
	exitOn = True
	ignore = ""
	if os.path.isfile(patchTouchName):
		logger.debug(f"applyPatchv2: Patch '{url}' already applied")
		cchdir(originalFolder)
		return
	pUrl = urlparse(url)
	if pUrl.scheme != '':
		fileName = os.path.basename(pUrl.path)
		logger.info(f"applyPatchv2: Downloading patch '{url}' to: {fileName}")
		downloadFile(url, fileName)
	else:
		local_patch_path = os.path.join(objSETTINGS.fullPatchDir, url)
		fileName = os.path.basename(Path(local_patch_path).name)
		if os.path.isfile(local_patch_path):
			copyPath = os.path.join(os.getcwd(), fileName)
			logger.info(f"applyPatchv2: Copying patch from '{local_patch_path}' to '{copyPath}'")
			logger.debug(f"applyPatchv2: cp -f '{local_patch_path}' '{copyPath}' # copy file ")
			shutil.copyfile(local_patch_path, copyPath)
		else:
			fileName = os.path.basename(urlparse(url).path)
			#url = "https://raw.githubusercontent.com/hydra3333/python_cross_compile_script/master/patches" + url
			url = objSETTINGS.patches_top_url + url
			downloadFile(url, fileName)
	logger.info(f"applyPatchv2: Patching source using: '{fileName}'")
	logger.info(f'{patchData["cmd"]} "{fileName}"')						# key is "cmd"
	runProcess(f'{patchData["cmd"]} "{fileName}"', ignoreErr, exitOn)	# key is "cmd"
	touch(patchTouchName)
	#if "dir" in patchData and patchData["dir"] is not None:
	#	cchdir(originalFolder)
	cchdir(originalFolder)	# get back to original folder regardless of whether we changed or not.

###
def applyPatch(url, type="-p1", postConf=False, folderToPatchIn=None):
	originalFolder = os.getcwd()
	if folderToPatchIn is not None:
		cchdir(folderToPatchIn)
		logger.info(f"applyPatch: Moved into patch folder: '{os.getcwd()}'")
	logger.info(f"applyPatch: Applying patch '{url}' in '{os.getcwd()}'")
	patchTouchName = f"patch_{md5(url)}.done"
	ignoreErr = False
	exitOn = True
	ignore = ""
	if postConf:
		patchTouchName = patchTouchName + "_past_conf"
		ignore = "-N "
		ignoreErr = True
		exitOn = False
	if os.path.isfile(patchTouchName):
		logger.info(f"applyPatch: Patch '{url}' already applied")
		cchdir(originalFolder)
		return
	pUrl = urlparse(url)
	if pUrl.scheme != '':
		fileName = os.path.basename(pUrl.path)
		logger.info(f"applyPatch: Downloading patch '{url}' to: {fileName}")
		downloadFile(url, fileName)
	else:
		local_patch_path = os.path.join(objSETTINGS.fullPatchDir, url)
		fileName = os.path.basename(Path(local_patch_path).name)
		if os.path.isfile(local_patch_path):
			copyPath = os.path.join(os.getcwd(), fileName)
			logger.info(f"applyPatch: Copying patch from '{local_patch_path}' to '{copyPath}'")
			logger.debug(f"applyPatch: cp -f '{local_patch_path}' '{copyPath}' # copy file ")
			shutil.copyfile(local_patch_path, copyPath)
		else:
			fileName = os.path.basename(urlparse(url).path)
			url = objSETTINGS.patches_top_url + url # 2020.06.22 if trunk moves to "main", "main" instead
			downloadFile(url, fileName)
	logger.info(f"applyPatch: Patching source using: '{fileName}'")
	logger.debug(f"applyPatch: patch -b {ignore}{type} < '{fileName}'")
	runProcess(f"patch -b {ignore}{type} < '{fileName}'", ignoreErr, exitOn)
	if not postConf:
		removeAlreadyFiles()
	touch(patchTouchName)
	if folderToPatchIn is not None:
		cchdir(originalFolder)

###################################################################################################
def buildPackage(packageName='', forceRebuild=False):	# was buildThing
	#old: def buildThing(self, packageName, pkg, type, forceRebuild=False, skipDepends=False):
	
	# a trick for the unwary:
	# if biggusDictus['_already_built'] exists, then it must have already been built
	# during the current run so don't build it yet again.
	# this implies that '_already_built' must have been added, once built, into all 3 of
	#	biggusDictus
	#	if packageName in dictProducts.BO
	#	if packageName in dictDependencies.BO
	#
	# NOTES: these are a bit special and unlike other variable commands such as !CMDxxxCMD!
	#	!SWITCHDIR
	#	!SWITCHDIRBACK
	#
	# we are in workdir
	
	resetDefaultEnvVars()
	if objArgParser.allforce:
		forceRebuild = True
	if packageName in dictProducts.BO:
		package_type = "PRODUCT"
	elif packageName in dictDependencies.BO:
		package_type = "DEPENDENCY"
	else:
		logger.error(f"Goodness me ! The specified object '{Colors.LIGHTMAGENTA_EX}{packageName}{Colors.RESET}' is neither a known PRODUCT nor a DEPENDENCY. Exiting.")
		sys.exit(1)
	logger.info(f"buildPackage: {Colors.LIGHTMAGENTA_EX}Building '{package_type.lower()} '{packageName}': Started ...{Colors.RESET}")

	# we want to be in workdir
	cchdir(objSETTINGS.fullWorkDir)  # cd to workdir
	currentFullDir = Path(os.getcwd())
	pkg = biggusDictus[packageName]
	
	#if boolKey(pkg, "is_dep_inheriter"):
	#	logger.warning(f"buildPackage: '{packageName}' contains 'is_dep_inheriter'='{pkg['is_dep_inheriter']}'")

	# check if the package has already been built in this run of this script
	# if so, return almost silently 
	if '_already_built' in pkg:
		if pkg['_already_built'] is True:
			logger.info(f"buildPackage: Skipping rebuild of '{Colors.LIGHTMAGENTA_EX}{packageName}{Colors.RESET}' since it has already been built")
			cchdir(objSETTINGS.fullWorkDir)  # cd to workdir
			return
	
	# peek at 'skip_deps' and set a flag
	skip_depends = False
	if objArgParser.skip_depends:
		skip_depends = True
		logger.debug(f"buildPackage: via cmdline, skip_depends={skip_depends} globally including for '{packageName}'")
	if 'skip_deps' in pkg:
		if pkg['skip_deps'] is True:
			skip_depends = True
			logger.debug(f"buildPackage: package parameter, skip_depends={skip_depends} for '{packageName}'")
		else:
			logger.debug(f"buildPackage: skip_deps in pkg  '{packageName}' but is False - ignored")
	else:
		logger.debug(f"buildPackage: skip_deps not in pkg '{packageName}'")

	#-----
	# 'run_pre_depends_on' goes here at the start ! 
	# It exists mainly for building freetype cleanly (it crashed if re-run).
	# It causes this section to run even if 'is_dep_inheriter' is set and allows for an early return
	if 'run_pre_depends_on' in pkg:
		if len(pkg['run_pre_depends_on']) > 0:
		# was this :- if pkg['run_pre_depends_on']:
			logger.debug(f"buildPackage: '{packageName}' ['run_pre_depends_on']=\n{objPrettyPrint.pformat(pkg['run_pre_depends_on'])}")
			for cmd in pkg['run_pre_depends_on']:	# for each item in 'run_pre_depends_on' (usually a line)
				logger.debug(f"buildPackage: '{packageName}' running ['run_pre_depends_on']cmd='{cmd}'")
				ignoreFail = False
				if isinstance(cmd, tuple):	# if one of the values in 'run_pre_depends_on' is a tuple itself like ('some_command', False)
					ignoreFail = cmd[1]	# whether to ignoreFail
					cmd = cmd[0]		# the command
				if cmd.startswith("!SWITCHDIRBACK"):
					cchdir(currentFullDir)
				elif cmd.startswith("!SWITCHDIR"):
					_dir = replaceVarCmdSubStrings("|".join(cmd.split("|")[1:]))
					cchdir(_dir)
				else:
					logger.debug(f"buildPackage: Running run_pre_depends_on-command pre replaceVarCmdSubStrings (raw): '{cmd}'")
					cmd = replaceVarCmdSubStrings(cmd)
					logger.debug(f"buildPackage: Running run_pre_depends_on-command: '{cmd}'")
					# run_process(cmd)	# no, see below
					logger.debug(cmd)
					runProcess(cmd, ignoreFail)		
		else:
			logger.debug(f"buildPackage: run_pre_depends_on in pkg '{packageName}' but is None - ignored")
	else:
		logger.debug(f"buildPackage: run_pre_depends_on not in pkg '{packageName}'")

	#-----

	if "depends_on" in pkg:
		if skip_depends is False:
			if len(pkg["depends_on"]) > 0:
				logger.info(f"buildPackage: Building dependencies of '{Colors.LIGHTMAGENTA_EX}{packageName}{Colors.RESET}' : {Colors.LIGHTRED_EX}{objPrettyPrint.pformat(pkg['depends_on'])}{Colors.RESET}")
				for libraryName in pkg["depends_on"]:
					if libraryName not in biggusDictus:
						logger.error(f"The specified dependency '{Colors.LIGHTMAGENTA_EX}{libraryName}{Colors.RESET}' of '{Colors.LIGHTMAGENTA_EX}{packageName}{Colors.RESET}' does not exist. Exiting.")
						raise MissingDependency(f"The specified dependency '{libraryName}' of '{packageName}' does not exist. Exiting.")  # sys.exc_info()[0]
						sys.exit(1)	# in case MissingDependency fails
					else:
						logger.debug(f"buildPackage: in '{Colors.LIGHTMAGENTA_EX}{packageName}{Colors.RESET}' about to recursive call buildPackage('{Colors.LIGHTMAGENTA_EX}{libraryName}{Colors.RESET}')")
						if objArgParser.allforce:
							all_force = True
						else:
							all_force = False
						buildPackage(libraryName, forceRebuild=all_force)	# only permit force rebuild on the nominated product/dependency rather than it's dependencies as well
		else:
			logger.debug(f"buildPackage: depends_on in pkg '{packageName}' but is True")
	else:
		logger.debug(f"buildPackage: depends_on not in pkg '{packageName}'")

	if 'is_dep_inheriter' in pkg:
		if pkg['is_dep_inheriter'] is True:
			pkg['_already_built'] = True
			biggusDictus[packageName]['_already_built'] = True
			logger.debug(f"buildPackage: in '{packageName}' with 'is_dep_inheriter'='{pkg['is_dep_inheriter']} ... Set pkg['_already_built']='{pkg['_already_built']}'")
		else: # specified but false is an error
			logger.error(f"buildPackage: '{packageName}' contains 'is_dep_inheriter'='{pkg['is_dep_inheriter']}'")
			sys.exit(1)
		logger.warning(f"buildPackage: '{packageName}' contains 'is_dep_inheriter'='{pkg['is_dep_inheriter']}', returning early")
		return

	if objSETTINGS.debugMode:
		logger.debug(f"############## Checks done, build '{package_type}' : '{Colors.LIGHTMAGENTA_EX}{packageName}{Colors.RESET}' ...")
		dump_environment_variables(override=False)
		pass

	#------------------------------------------------------------------------------------------------
	#------------------------------------------------------------------------------------------------
	logger.info(f"-----------------------------------------------------------------------------------")
	logger.info(f"Building {package_type} '{Colors.LIGHTMAGENTA_EX}{packageName}{Colors.RESET}' ...")
	logger.info(f"-----------------------------------------------------------------------------------")
	#------------------------------------------------------------------------------------------------
	#------------------------------------------------------------------------------------------------
	
	cchdir(".")
	resetDefaultEnvVars()	# deadsix27 removed this line ... leave it in for now

	if 'warnings' in pkg:
		if len(pkg['warnings']) > 0:
			for w in pkg['warnings']:
				logger.warning(w)
		else:
			logger.debug(f"buildPackage: warnings in pkg '{packageName}' but len is not > 0 - ignored")
	else:
		logger.debug(f"buildPackage: warnings not in pkg '{packageName}'")

	workDir = None
	renameFolder = None
	if 'rename_folder' in pkg:
		if pkg['rename_folder'] is not None:
			renameFolder = replaceVarCmdSubStrings(pkg['rename_folder'])
		else:
			logger.debug(f"buildPackage: rename_folder in pkg '{packageName}' but is None - ignored")
	else:
		logger.debug(f"buildPackage: rename_folder not in pkg '{packageName}'")

	if package_type == "PRODUCT":
		cchdir(objSETTINGS.fullProductDir)	# descend into x86_64_products
	elif package_type == "DEPENDENCY":
		cchdir(objSETTINGS.bitnessPath)		# descend into x86_64
	else:
		logger.error(f"Goodness me ! The specified object '{Colors.LIGHTMAGENTA_EX}{packageName}{Colors.RESET}' has been pre-checked, and yet it still is neither a known PRODUCT nor a DEPENDENCY. Exiting.")
		sys.exit(1)

	if pkg["repo_type"] == "git":		# GIT GIT GIT GIT GIT GIT GIT GIT GIT GIT GIT GIT GIT GIT GIT GIT 
		branch = getValueOrNone(pkg, 'branch')
		if branch is not None:
			branch = replaceVarCmdSubStrings(branch)
		recursive = getValueOrNone(pkg, 'recursive_git')
		git_depth = pkg.get(f"depth_git", -1)	# Use Dict .get method, with a default of -1 which meanss the last commit
		folderName = replaceVarCmdSubStrings(getValueOrNone(pkg, 'folder_name'))
		doNotUpdate = False
		if 'do_not_git_update' in pkg:
			if pkg['do_not_git_update'] is True:
				doNotUpdate = True
		desiredPRVal = None
		if 'desired_pr_id' in pkg:
			if pkg['desired_pr_id'] is not None:
				desiredPRVal = replaceVarCmdSubStrings(pkg['desired_pr_id'])
		ppd = getPrimaryPackageUrl(pkg, packageName)
		logger.debug(f"buildPackage: GIT: gitClone '{packageName}' ppd='{ppd}' branch='{branch}' folderName='{folderName}' renameFolder='{renameFolder}'")
		workDir = gitClone(ppd, folderName, renameFolder, branch, recursive, doNotUpdate, desiredPRVal, git_depth) # returned to the level above renameFolder
		logger.debug(f"buildPackage: GIT: gitClone '{packageName}' returned workdir='{workDir}' and current path='{os.getcwd()}'")
	elif pkg["repo_type"] == "svn":	# SVN SVN SVN SVN SVN SVN SVN SVN SVN SVN SVN SVN SVN SVN SVN SVN 
		folderName = replaceVarCmdSubStrings(getValueOrNone(pkg, 'folder_name'))
		ppd = getPrimaryPackageUrl(pkg, packageName)
		logger.debug(f"buildPackage: SVN: svnClone '{packageName}' folderName='{folderName}' renameFolder='{renameFolder}'")
		workDir = svnClone(ppd, folderName, renameFolder)
		logger.debug(f"buildPackage: SVN: svnClone '{packageName}' returned workdir='{workDir}' and current path='{os.getcwd()}'")
	elif pkg['repo_type'] == 'mercurial':	# MERCURUAL MERCURUAL MERCURUAL MERCURUAL MERCURUAL MERCURUAL 
		branch = getValueOrNone(pkg, 'branch')
		if branch is not None:
			branch = replaceVarCmdSubStrings(branch)
		folderName = replaceVarCmdSubStrings(getValueOrNone(pkg, 'folder_name'))
		ppd = getPrimaryPackageUrl(pkg, packageName)
		logger.debug(f"buildPackage: mercurial: mercurialClone '{packageName}' folderName='{folderName}' renameFolder='{renameFolder}'")
		workDir = mercurialClone(ppd, folderName, renameFolder, branch, forceRebuild)
		logger.debug(f"buildPackage: mercurial: mercurialClone '{packageName}' returned workdir='{workDir}' and current path='{os.getcwd()}'")
	elif pkg["repo_type"] == "archive":	# ARCHIVE ARCHIVE ARCHIVE ARCHIVE ARCHIVE ARCHIVE ARCHIVE ARCHIVE 
		if "folder_name" in pkg:
			folderName = replaceVarCmdSubStrings(getValueOrNone(pkg, 'folder_name'))
			logger.debug(f"buildPackage: archive: downloadUnpackFile '{packageName}' folderName='{folderName}'")
			workDir = downloadUnpackFile(pkg, packageName, folderName, workDir)
			logger.debug(f"buildPackage: archive: downloadUnpackFile '{packageName}' returned workdir='{workDir}' and current path='{os.getcwd()}'")
		else:
			logger.debug(f"buildPackage: archive: downloadUnpackFile '{packageName}' folderName='{None}'")
			workDir = downloadUnpackFile(pkg, packageName, None, workDir)
			logger.debug(f"buildPackage: archive: downloadUnpackFile '{packageName}' returned workdir='{workDir}' and current path='{os.getcwd()}'")
	elif pkg["repo_type"] == "none":		# REPO-NONE REPO-NONE REPO-NONE REPO-NONE REPO-NONE REPO-NONE 
		if "folder_name" in pkg:
			folderName = replaceVarCmdSubStrings(getValueOrNone(pkg, 'folder_name'))
			logger.debug(f"buildPackage: REPO-NONE: mkdir '{packageName}' folderName='{folderName}'")
			workDir = folderName
			logger.debug(f"mkdir -p '{workDir}'")
			os.makedirs(workDir, exist_ok=True)
			logger.debug(f"buildPackage: REPO-NONE: mkdir '{packageName}' returned workdir='{workDir}' and current path='{os.getcwd()}'")
		else:
			logger.error(f"Error: When using repo_type 'none' you have to set folder_name as well.")
			exit(1)

	if workDir is None:
		logger.error(f"buildPackage :Error: Unexpected error when building {packageName}, workdir='{workDir}' and current path='{os.getcwd()}', please report this: {sys.exc_info()[0]}")
		raise Exception(f"buildPackage: Error: Unexpected error when building {packageName}, workdir='{workDir}' and current path='{os.getcwd()}'")

	#### does this rename_folder break if there is a specified commit in gitclone ?  
	#### a specified gitclone commit immediate return value from  gitclone leaves us in the subfolder which is wrong
	#### since the other git returns leave is in the level above and rename_folder then can't find it to stop renaming itself since it's still inside it
	########## this only occurs where both a specified git commit and a rename_folder occur inside the same product/dependency
	########## fixed upstream

	if 'rename_folder' in pkg:
		if pkg['rename_folder'] is not None:
			logger.debug(f"buildPackage:rename_folder when workdir='{workDir}' and current path='{os.getcwd()}'")
			if not os.path.isdir(pkg['rename_folder']):	# the rename_folder doesn't get executed if the folder has already been renamed)
				logger.debug(f"buildPackage rename_folder in pkg '{packageName}', current path='{os.getcwd()}', workdir='{workDir}', folder {pkg['rename_folder']} does NOT EXIST, renaming '{workDir}' to '{pkg['rename_folder']}")
				logger.debug(f"mv -f '{workDir}' '{pkg['rename_folder']}' # rename folder from '{workDir}' to '{pkg['rename_folder']}'")
				shutil.move(workDir, pkg['rename_folder'])
			else:
				logger.debug(f"buildPackage rename_folder in pkg '{packageName}', current path='{os.getcwd()}', workdir='{workDir}', folder {pkg['rename_folder']} EXISTS, NOT renaming '{workDir}' to '{pkg['rename_folder']}")
			workDir = pkg['rename_folder']
		else:
			logger.debug(f"buildPackage: rename_folder in pkg '{packageName}' but is None - ignored")
	else:
		logger.debug(f"buildPackage: rename_folder not in pkg '{packageName}', current path='{os.getcwd()}'")

	if 'download_header' in pkg:
		if pkg['download_header'] is not None:
			logger.debug(f"buildPackage: detected 'download_header' is not None in pkg '{packageName}'")
			for h in pkg['download_header']:
				logger.debug(f"buildPackage: download_header in pkg '{packageName}' downloading header '{h}'")
				downloadHeader(h)
		else:
			logger.debug(f"buildPackage: download_header in pkg '{packageName}' but is None - ignored")
	else:
		logger.debug(f"buildPackage: download_header not in pkg '{packageName}', current path='{os.getcwd()}'")

	###++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	logger.debug(f"buildPackage: ABOUT TO CD INTO DEPENDENCY_OR_PRODUCT '{packageName}' FOLDER, current path='{os.getcwd()}'")
	cchdir(workDir)  # descend into x86_64/[DEPENDENCY_OR_PRODUCT_FOLDER]
	logger.debug(f"buildPackage: AFTER    CD INTO DEPENDENCY_OR_PRODUCT '{packageName}' FOLDER, current path='{os.getcwd()}'")
	###++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	
	if 'debug_downloadonly' in pkg:		# WELL, WELL, HADN'T SEEN THAT BEFORE
		cchdir("..")
		exit()

	oldPath = getKeyOrBlankString(os.environ, "PATH")
	currentFullDir = os.getcwd()

	if not anyFileStartsWith('already_configured'):
		logger.debug(f"buildPackage: detected 'not anyFileStartsWith('already_configured')' for run_pre_patch in pkg '{packageName}', current path='{os.getcwd()}'")
		if 'run_pre_patch' in pkg:
			if pkg['run_pre_patch'] is not None:
				for cmd in pkg['run_pre_patch']:
					logger.debug(f"buildPackage: Running pre-patch-command pre replaceVarCmdSubStrings (raw): '{cmd}'")
					cmd = replaceVarCmdSubStrings(cmd)
					logger.debug(f"buildPackage: Running pre-patch-command: '{cmd}'")
					logger.info(cmd)
					runProcess(cmd)
			else:
				logger.debug(f"buildPackage: run_pre_patch in pkg '{packageName}' but is None - ignored")
		else:
			logger.debug(f"buildPackage: run_pre_patch not in pkg '{packageName}'")

	if forceRebuild:
		logger.debug(f"buildPackage: detected forceRebuild={forceRebuild} in pkg '{packageName}', current path='{os.getcwd()}'")
		if os.path.isdir(".git"):
			logger.info(F'buildPackage: Force cleaning')
			logger.info(f"buildPackage: git clean -ffdx")  # https://gist.github.com/nicktoumpelis/11214362
			runProcess(f"git clean -ffdx")  # https://gist.github.com/nicktoumpelis/11214362
			logger.info(f"buildPackage: git submodule foreach --recursive git clean -ffdx")
			runProcess(f"git submodule foreach --recursive git clean -ffdx")
			logger.info(f"buildPackage: git reset --hard")
			runProcess(f"git reset --hard")
			logger.info(f"buildPackage: git submodule foreach --recursive git reset --hard")
			runProcess(f"git submodule foreach --recursive git reset --hard")
			logger.info(f"buildPackage: git submodule update --init --recursive")
			runProcess(f"git submodule update --init --recursive")

	# 2023.04.09 added rhis block per deadsix27
	if 'regex_replace' in pkg and pkg['regex_replace']:
		_pos = 'pre_patch'
		if isinstance(pkg['regex_replace'], dict) and _pos in pkg['regex_replace']:
			for r in pkg['regex_replace'][_pos]:
				try:
					handleRegexReplace(r, packageName)
				except re.error as e:
					errorExit(e)
					sys.exit(1)

	if 'source_subfolder' in pkg:
		if pkg['source_subfolder'] is not None:
			vval = pkg['source_subfolder']
			vval = replaceVarCmdSubStrings(vval)
			if not os.path.isdir(vval):
				logger.info(f"buildPackage: mkdirs '{vval}'")
				os.makedirs(vval, exist_ok=True)
			cchdir(vval)
		else:
			logger.debug(f"buildPackage: source_subfolder in pkg '{packageName}' but is None - ignored")
	else:
		logger.debug(f"buildPackage: source_subfolder not in pkg '{packageName}'")

	if forceRebuild:
		removeAlreadyFiles()
		removeConfigPatchDoneFiles()
	else:
		logger.debug(f"buildPackage: forceRebuild not specified - not removing patches and Already files")

	#?????? here assumes we are in the subfolder
	if 'debug_confighelp_and_exit' in pkg:		# WELL, WELL, HADN'T SEEN THAT BEFORE
		if pkg['debug_confighelp_and_exit'] is True:
			logger.info(f"buildPackage: ./configure --help")
			bootstrapConfigure()
			logger.info(f"buildPackage: ./configure --help")
			runProcess(f"./configure --help")
			exit()
		else:
			logger.debug(f"buildPackage: debug_confighelp_and_exit in pkg '{packageName}' but is False - ignored")
	else:
		logger.debug(f"buildPackage: debug_confighelp_and_exit not in pkg '{packageName}'")

	if 'cflag_addition' in pkg:
		if pkg['cflag_addition'] is not None:
			vval = pkg['cflag_addition']
			vval = replaceVarCmdSubStrings(vval)
			logger.debug(f"buildPackage: Adding '{vval}' to CFLAGS")
			logger.debug(f"buildPackage: os.environ CFLAGS   before cflag_addition = '{os.environ['CFLAGS']}'")
			logger.debug(f"buildPackage: os.environ CXXFLAGS before cflag_addition = '{os.environ['CXXFLAGS']}'")
			logger.debug(f"buildPackage: os.environ CPPFLAGS before cflag_addition = '{os.environ['CPPFLAGS']}'")
			logger.debug(f"buildPackage: os.environ LDFLAGS  before cflag_addition = '{os.environ['LDFLAGS']}'")
			os.environ['CFLAGS'] = os.environ['CFLAGS'] + " " + vval
			os.environ['CXXFLAGS'] = os.environ['CXXFLAGS'] + " " + vval
			os.environ['CPPFLAGS'] = os.environ['CPPFLAGS'] + " " + vval
			os.environ['LDFLAGS'] = os.environ['LDFLAGS'] + " " + vval
			logger.info(f"buildPackage: Added to CFLAGS,   now: '{os.environ['CFLAGS']}'")
			logger.info(f"buildPackage: Added to CXXFLAGS, now: '{os.environ['CXXFLAGS']}'")
			logger.info(f"buildPackage: Added to CPPFLAGS, now: '{os.environ['CPPFLAGS']}'")
			logger.info(f"buildPackage: Added to LDFLAGS,  now: '{os.environ['LDFLAGS']}'")
			dump_environment_variables(override=False)
		else:
			logger.debug(f"buildPackage: cflag_addition in pkg '{packageName}' but is None - ignored")
	else:
		logger.debug(f"buildPackage: cflag_addition not in pkg '{packageName}'")

	if 'custom_cflag' in pkg:
		if pkg['custom_cflag'] is not None:
			vval = pkg['custom_cflag']
			vval = replaceVarCmdSubStrings(vval)
			logger.debug(f"buildPackage: Setting CFLAGS to '{vval}'")
			logger.debug(f"buildPackage: os.environ CFLAGS   before custom_cflag = '{os.environ['CFLAGS']}'")
			logger.debug(f"buildPackage: os.environ CXXFLAGS before custom_cflag = '{os.environ['CXXFLAGS']}'")
			logger.debug(f"buildPackage: os.environ CPPFLAGS before custom_cflag = '{os.environ['CPPFLAGS']}'")
			logger.debug(f"buildPackage: os.environ LDFLAGS  before custom_cflag = '{os.environ['LDFLAGS']}'")
			os.environ['CFLAGS'] = vval   # 2019.12.13
			os.environ['CXXFLAGS'] = vval # 2019.12.13
			os.environ['CPPFLAGS'] = vval # 2019.12.13
			os.environ['LDFLAGS'] = vval  # 2019.12.13
			logger.info(f"buildPackage: Set custom CFLAGS,   now: '{os.environ['CFLAGS']}'")
			logger.info(f"buildPackage: Set custom CXXFLAGS, now: '{os.environ['CXXFLAGS']}'")
			logger.info(f"buildPackage: Set custom CPPFLAGS, now: '{os.environ['CPPFLAGS']}'")
			logger.info(f"buildPackage: Set custom LDFLAGS,  now: '{os.environ['LDFLAGS']}'")
			dump_environment_variables(override=False)
		else:
			logger.debug(f"buildPackage: custom_cflag in pkg '{packageName}' but is None - ignored")
	else:
		logger.debug(f"buildPackage: custom_cflag not in pkg '{packageName}'")

	if 'custom_ldflag' in pkg:
		if pkg['custom_ldflag'] is not None:
			vval = pkg['custom_ldflag']
			vval = replaceVarCmdSubStrings(vval)
			logger.debug(f"buildPackage: custom_ldflag os.environ LDFLAGS  before setting LDFLAGS = '{os.environ['LDFLAGS']}'")
			logger.debug(f"buildPackage: Setting LDFLAGS to '{vval}'")
			os.environ['LDFLAGS'] = vval  # 2019.12.13
			logger.info(f"buildPackage: Set LDFLAGS, now: '{os.environ['LDFLAGS']}'")
			dump_environment_variables(override=False)
		else:
			logger.debug(f"buildPackage: custom_ldflag in pkg '{packageName}' but is None - ignored")
	else:
		logger.debug(f"buildPackage: custom_ldflag not in pkg '{packageName}'")

	if 'strip_cflags' in pkg:
		if isinstance(pkg["strip_cflags"], (list, tuple)) and len(pkg["strip_cflags"]):
			for _pattern in pkg["strip_cflags"]:
				logger.debug(f"buildPackage: os.environ CFLAGS,   before stripping = '{os.environ['CFLAGS']}'")
				logger.debug(f"buildPackage: os.environ CXXFLAGS, before stripping = '{os.environ['CXXFLAGS']}'")
				logger.debug(f"buildPackage: os.environ CPPFLAGS, before stripping = '{os.environ['CPPFLAGS']}")
				logger.debug(f"buildPackage: os.environ LDFLAGS,  before stripping = '{os.environ['LDFLAGS']}'")
				os.environ['CFLAGS'] = reStrip(_pattern, os.environ['CFLAGS'])
				os.environ['CXXFLAGS'] = reStrip(_pattern, os.environ['CXXFLAGS'])
				os.environ['CPPFLAGS'] = reStrip(_pattern, os.environ['CPPFLAGS'])
				os.environ['LDFLAGS'] = reStrip(_pattern, os.environ['LDFLAGS'])
				logger.info(f"buildPackage: Stripped CFLAGS,   now: '{os.environ['CFLAGS']}'")
				logger.info(f"buildPackage: Stripped CXXFLAGS, now: '{os.environ['CXXFLAGS']}'")
				logger.info(f"buildPackage: Stripped CPPFLAGS, now: '{os.environ['CPPFLAGS']}'")
				logger.info(f"buildPackage: Stripped LDFLAGS,  now: '{os.environ['LDFLAGS']}'")
			dump_environment_variables(override=False)
		else:
			logger.debug(f"buildPackage: strip_cflags in pkg '{packageName}' but conditions not satisfied - ignored")
	else:
		logger.debug(f"buildPackage: strip_cflags not in pkg '{packageName}'")

	if 'custom_path' in pkg:
		if pkg['custom_path'] is not None:
			vval = pkg['custom_path']
			vval = replaceVarCmdSubStrings(vval)
			logger.debug(f"buildPackage: os.environ PATH   before custom_path = '{os.environ['PATH']}'")
			logger.debug(f"Setting PATH to '{vval}'")
			os.environ['PATH'] = vval
			logger.info(f"buildPackage: Set custom PATH, now: '{os.environ['PATH']}'")
			dump_environment_variables(override=False)
		else:
			logger.debug(f"buildPackage: custom_path in pkg '{packageName}' but is None - ignored")
	else:
		logger.debug(f"buildPackage: custom_path not in pkg '{packageName}'")

	if 'flipped_path' in pkg:
		if pkg['flipped_path'] is True:
			bef = os.environ['PATH']
			logger.debug(f"buildPackage: os.environ PATH before custom_path = '{os.environ['PATH']}'")
			os.environ['PATH']  = f"{objSETTINGS.mingwBinpath}:{os.path.join(objSETTINGS.targetPrefix,'bin')}:{objSETTINGS.originalPATH}"  # todo properly test this..
			logger.info(f"buildPackage: Flipping path from: '{bef}' to '{os.environ['PATH']}'")
			dump_environment_variables(override=False)
		else:
			logger.debug(f"buildPackage: flipped_path in pkg '{packageName}' but is False - ignored")
	else:
		logger.debug(f"buildPackage: flipped_path not in pkg '{packageName}'")

	if 'env_exports' in pkg:
		if pkg['env_exports'] is not None:
			for key, val in pkg['env_exports'].items():
				vval = replaceVarCmdSubStrings(val)
				prevEnv = ''
				if key in os.environ:
					prevEnv = os.environ[key]
				os.environ[key] = vval
				logger.info(f"buildPackage: Environment variable '{key}' Set from '{prevEnv}' to '{vval}'")
			dump_environment_variables(override=False)
		else:
			logger.debug(f"buildPackage: env_exports in pkg '{packageName}' but is None - ignored")
	else:
		logger.debug(f"buildPackage: env_exports not in pkg '{packageName}'")

	if 'copy_over' in pkg:
		if pkg['copy_over'] is not None:
			for f in pkg['copy_over']:
				f_formatted = replaceVarCmdSubStrings(f)
				f_formatted = Path(f_formatted)
				if not f_formatted.is_file():
					errorExit(f"buildPackage: Copy-over file '{f_formatted}' (Unformatted: '{f}') does not exist.")
					sys.exit(1)
				dst = os.path.join(currentFullDir, f_formatted.name)
				logger.info(f"buildPackage: Copying file over from '{dst}' to '{dst}'")
				logger.info(f"cp -f '{f_formatted}' '{dst}' # copy file ")
				shutil.copyfile(f_formatted, dst)
		else:
			logger.debug(f"buildPackage: copy_over in pkg '{packageName}' but is None - ignored")
	else:
		logger.debug(f"buildPackage: copy_over not in pkg '{packageName}'")

	if 'run_justbefore_patch' in pkg:
		if pkg['run_justbefore_patch'] is not None:
			for cmd in pkg['run_justbefore_patch']:
				ignoreFail = False
				if isinstance(cmd, tuple):
					cmd = cmd[0]
					ignoreFail = cmd[1]
				if cmd.startswith(f"!SWITCHDIRBACK"):
					cchdir(currentFullDir)
				elif cmd.startswith(f"!SWITCHDIR"):
					_dir = replaceVarCmdSubStrings("|".join(cmd.split("|")[1:]))
					cchdir(_dir)
				else:
					logger.debug(f"buildPackage: Running justbefore_patch-command pre ']: (raw): '{cmd}'")
					cmd = replaceVarCmdSubStrings(cmd)
					logger.info(f"buildPackage: Running justbefore_patch-command: '{cmd}'")
					#run_process(cmd)	# no, see below
					logger.debug(cmd)
					runProcess(cmd, ignoreFail)
		else:
			logger.debug(f"buildPackage: run_justbefore_patch in pkg '{packageName}' but is None - ignored")
	else:
		logger.debug(f"buildPackage: run_justbefore_patch not in pkg '{packageName}'")

	if 'patches' in pkg:
		if pkg['patches'] is not None:
			for p in pkg['patches']:
				if isinstance(p, dict):	# if a patch in the list is a dict (a set of key/value pairs) then use v2
					applyPatchv2(p)
				else:
					applyPatch(p[0], p[1], False, getValueByIntOrNone(p, 2))
		else:
			logger.debug(f"buildPackage: patches in pkg but is None - ignored")
	else:
		logger.debug(f"buildPackage: patches not in pkg")

	if not anyFileStartsWith('already_ran_make'):
		if 'run_post_patch' in pkg:
			if pkg['run_post_patch'] is not None:
				for cmd in pkg['run_post_patch']:
					ignoreFail = False
					if isinstance(cmd, tuple):
						cmd = cmd[0]
						ignoreFail = cmd[1]
					if cmd.startswith(f"!SWITCHDIRBACK"):
						cchdir(currentFullDir)
					elif cmd.startswith(f"!SWITCHDIR"):
						_dir = replaceVarCmdSubStrings("|".join(cmd.split("|")[1:]))
						cchdir(_dir)
					else:
						logger.debug(f"buildPackage: Running post-patch-command pre replaceVarCmdSubStrings (raw): '{cmd}'")
						cmd = replaceVarCmdSubStrings(cmd)
						logger.info(f"buildPackage: Running post-patch-command: '{cmd}'")
						#run_process(cmd)	# no, see below
						logger.debug(cmd)
						runProcess(cmd, ignoreFail)
			else:
				logger.debug(f"buildPackage: run_post_patch in pkg '{packageName}' but is None - ignored")
		if 'regex_replace' in pkg and pkg['regex_replace']:
			_pos = 'post_patch'
			if isinstance(pkg['regex_replace'], dict) and _pos in pkg['regex_replace']:
				for r in pkg['regex_replace'][_pos]:
					try:
						handleRegexReplace(r, packageName)
					except re.error as e:
						errorExit(e)
			else:
				logger.debug(f"buildPackage: regex_replace in pkg '{packageName}' but is None - ignored")
		else:
			logger.debug(f"buildPackage: regex_replace not in pkg '{packageName}'")		
		
		if 'run_post_regexreplace' in pkg and pkg['run_post_regexreplace']:
				for cmd in pkg['run_post_regexreplace']:
					ignoreFail = False
					if isinstance(cmd, tuple):
						cmd = cmd[0]
						ignoreFail = cmd[1]
					if cmd.startswith(f"!SWITCHDIRBACK"):
						cchdir(currentFullDir)
					elif cmd.startswith(f"!SWITCHDIR"):
						_dir = replaceVarCmdSubStrings("|".join(cmd.split("|")[1:]))
						cchdir(_dir)
					else:
						cmd = replaceVarCmdSubStrings(cmd)
						logger.info(f"buildPackage: Running run_post_regexreplace-command: '{cmd}'")
						# run_process(cmd)	# no, see below
						runProcess(cmd, ignoreFail)
		else:
			logger.debug(f"buildPackage: run_post_regexreplace in pkg '{packageName}' but is None - ignored")
	else:
		logger.debug(f"buildPackage: already_ran_make detected for '{packageName}', run_post_patch not run, run_post_regexreplace not run")

	#	conf_system_specifics = {	"gnumake_based_systems" : [ "cmake", "autoconf" ],
	# 								"ninja_based_systems" : [ "meson" ]
	#	}
	conf_system = None
	build_system = None
	if 'build_system' in pkg:  # Kinda redundant, but ill keep it for now, maybe add an alias system for this.
		if pkg['build_system'] == "ninja":
			build_system = "ninja"
		if pkg['build_system'] == "waf":
			build_system = "waf"
		if pkg['build_system'] == "rake":
			build_system = "rake"
		if pkg['build_system'] == "rust":
			build_system = "rust"
	else:
		logger.debug(f"buildPackage: build_system not in pkg '{packageName}'")
	if 'conf_system' in pkg:
		if pkg['conf_system'] == "cmake":
			conf_system = "cmake"
			if not build_system:
				build_system = "ninja"
		elif pkg['conf_system'] == "meson":
			conf_system = "meson"
		elif pkg['conf_system'] == "waf":
			conf_system = "waf"
		elif pkg['conf_system'] == "cinstall":
			conf_system = "cinstall"
		else:
			logger.debug(f"buildPackage: conf_system in pkg '{packageName}' but is NOT RECOGNISED - ignored")
	else:
		logger.debug(f"buildPackage: conf_system not in pkg '{packageName}'")

	conf_system = "autoconf" if not conf_system else conf_system
	build_system = "make" if not build_system else build_system

	# +++
	needs_conf = True
	if 'needs_configure' in pkg:
		if pkg['needs_configure'] is False:
			needs_conf = False
		else:
			logger.debug(f"buildPackage: needs_configure in pkg '{packageName}' but is None - ignored")
	else:
		logger.debug(f"buildPackage: needs_configure not in pkg '{packageName}'")

	if needs_conf:
		logger.debug(f"buildPackage: needs_conf is TRUE, conf_system is {conf_system} in pkg '{packageName}'")
		if conf_system == "cmake":
			cmakeSource(packageName, pkg)
		elif conf_system == "meson":
			mesonSource(packageName, pkg)
		else:
			configureSource(packageName, pkg, conf_system)
			logger.debug(f"buildPackage: needs_conf in pkg '{packageName}' is TRUE but conf_system='{conf_system}' is NOT RECOGNISED - ignored")
	else:
		logger.debug(f"buildPackage: needs_conf is FALSE in pkg '{packageName}'")

	# +++
	if 'make_subdir' in pkg:
		if pkg['make_subdir'] is not None:
			if not os.path.isdir(pkg['make_subdir']):
				os.makedirs(pkg['make_subdir'], exist_ok=True)
			cchdir(pkg['make_subdir'])
		else:
			logger.debug(f"buildPackage: make_subdir in pkg '{packageName}' but is None - ignored")
	else:
		logger.debug(f"buildPackage: make_subdir not in pkg '{packageName}'")

	if 'needs_make' in pkg:
		if pkg['needs_make'] is True:
			logger.debug(f"buildPackage: needs_make is in pkg '{packageName}'")
			buildSource(packageName, pkg, build_system)
	else:
		logger.debug(f"buildPackage: needs_make not in pkg '{packageName}'")
		buildSource(packageName, pkg, build_system)

	# +++
	if 'needs_make_install' in pkg:
		if pkg['needs_make_install'] is True:
			logger.debug(f"buildPackage: needs_make_install is in pkg '{packageName}' and is True")
			installSource(packageName, pkg, build_system)
		else:
			logger.debug(f"buildPackage: needs_make_install in pkg '{packageName}' but is False - ignored")
	else:
		logger.debug(f"buildPackage: needs_make_install not in pkg '{packageName}'")
		installSource(packageName, pkg, build_system)

	if 'env_exports' in pkg:
		if pkg['env_exports'] is not None:
			for key, val in pkg['env_exports'].items():
				del os.environ[key]
				logger.debug(f"buildPackage: Environment variable '{key}' has been UNSET from '{val}' !")
		else:
			logger.debug(f"buildPackage: env_exports in pkg '{packageName}' but is None - ignored")
	else:
		logger.debug(f"buildPackage: env_exports not in pkg '{packageName}'")

	if 'flipped_path' in pkg:
		if pkg['flipped_path'] is True:
			_path = os.environ['PATH']
			os.environ['PATH'] = "{0}:{1}".format(objSETTINGS.mingwBinpath, objSETTINGS.originalPATH)
			logger.debug(f"buildPackage: Resetting flipped path to: '{_path}' from '{os.environ['PATH']}'")
		else:
			logger.debug(f"buildPackage: flipped_path in pkg '{packageName}' but is False - ignored")
	else:
		logger.debug(f"buildPackage: flipped_path not in pkg '{packageName}'")

	if 'source_subfolder' in pkg:
		if pkg['source_subfolder'] is not None:
			if not os.path.isdir(pkg['source_subfolder']):
				os.makedirs(pkg['source_subfolder'], exist_ok=True)
			cchdir(currentFullDir)
		else:
			logger.debug(f"buildPackage: source_subfolder in pkg '{packageName}' but is None - ignored")
	else:
		logger.debug(f"buildPackage: source_subfolder not in pkg '{packageName}'")

	if 'make_subdir' in pkg:
		if pkg['make_subdir'] is not None:
			cchdir(currentFullDir)
		else:
			logger.debug(f"buildPackage: make_subdir in pkg '{packageName}' but is None - ignored")
	else:
		logger.debug(f"buildPackage: make_subdir not in pkg '{packageName}'")

	cchdir("..")  # asecond into x86_64
	
	pkg['_already_built'] = True
	biggusDictus[packageName]['_already_built'] = True

	if 'debug_exitafter' in pkg:
		logger.info(f"buildPackage: {Colors.LIGHTMAGENTA_EX}Building '{package_type.lower()} '{packageName}': Done !{Colors.RESET}")
		exit()
	else:
		logger.debug(f"buildPackage: debug_exitafter not in pkg '{packageName}'")

	if 'custom_path' in pkg:
		if pkg['custom_path'] is not None:
			logger.debug(f"buildPackage: Re-setting PATH to '{oldPath}'")
			os.environ['PATH'] = oldPath
			dump_environment_variables(override=False)
		else:
			logger.debug(f"buildPackage: custom_path in pkg '{packageName}' but is None - ignored")
	else:
		logger.debug(f"buildPackage: custom_path not in pkg '{packageName}'")

	resetDefaultEnvVars()
	cchdir("..")  # ascend into workdir

	logger.info(f"buildPackage: {Colors.LIGHTMAGENTA_EX}Building '{package_type.lower()} '{packageName}': Done !{Colors.RESET}")
	return

###################################################################################################
def listVersions():
	# uses biggusDictus for detail, getting key = package names from dictProducts.BO and dictDependencies.BO
	global objSETTINGS		# the SETTINGS object used everywhere
	global logging_handler 	# the handler for the logger, only used for initialization
	global logger 			# the logger object used everywhere
	global objArgParser		# the ArgParser which may be used everywhere
	global objParser		# the parser creat6ed by ArgParser which may be used everywhere
	global dictProducts		# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for PRODUCTS only, of class dot_py_object_dict
	global dictDependencies	# a dict of key/values pairs, in this case the filename/json-values-inside-the-.py for DEPENDENCIES only, of class dot_py_object_dict
	global objVariables		# an object of the variables, of class dot_py_object
	global biggusDictus		# combined dictProducts | dictDependencies
	global objPrettyPrint	# facilitates formatting and printing of text and dicts etc
	global TERMINAL_WIDTH	# for Console setup and PrettyPrint setup
	###=== START OF LOCAL CLASS PARSERS
	class Parsers:
		def __init__(self, url, verex):
			logger.debug(f"listVersions: Parsers: __init__: Start processing with incoming url='{url}' verex='{verex}'")
			self.url = url
			self.verex = verex
			# self.api_key = SOURCEFORGE_APIKEY
			logger.debug(f"listVersions: Parsers: __init__: Finished processing")
		#
		def sourceforge(self):
			logger.debug(f"listVersions: Parsers: sourceforge: Start processing")
			soup = BeautifulSoup(requests.get(self.url, headers=objSETTINGS.HEADERS, timeout=2).content, features="html5lib")
			allFolderTrs = soup.find_all("tr", attrs={"class": re.compile(r"folder.*"), "title": re.compile(r".*")})
			allFileTrs = soup.find_all("tr", attrs={"class": re.compile(r"file.*"), "title": re.compile(r".*")})
			newest = "0.0.0"
			for tr in allFolderTrs + allFileTrs:
				v = tr["title"]
				if self.verex is not None:
					m = re.search(self.verex, v)
					if m is not None:
						g = m.groupdict()
						if "version_num" not in g:
							errorExit(f"listVersions: Parsers: sourceforge: You have to name a regex group version_num")
						v = g["version_num"]
						if "rc_num" in g:
							v = v + "." + g["rc_num"]
					else:
						v = ""
				if v != "":
					if re.match(r"^(?P<version_num>(?:[\dx]{1,3}\.){0,3}[\dx]{1,3})$", v):
						if Version(v) > Version(newest):
							newest = v
			logger.debug(f"listVersions: Parsers: sourceforge: Finished processing, returning newest='{newest}'")
			return newest
		#
		def httpindex(self):
			logger.debug(f"listVersions: Parsers: httpindex: Start processing")
			cwd, listing = htmllistparse.fetch_listing(self.url, timeout=2) # timeout=30
			newest = "0.0.0"
			for entry in listing:
				v = entry.name
				if self.verex is not None:
					m = re.search(self.verex, v)
					if m is not None:
						g = m.groupdict()
						if "version_num" not in g:
							errorExit(f"listVersions: Parsers: httpindex: You have to name a regex group version_num")
						v = g["version_num"]
						if "rc_num" in g:
							v = v + "." + g["rc_num"]
					else:
						v = ""
				if v != "":
					if re.match(r"^(?P<version_num>(?:[\dx]{1,3}\.){0,3}[\dx]{1,3})$", v):
						if Version(v) > Version(newest):
							newest = v
			logger.debug(f"listVersions: Parsers: httpindex: Finished processing, returning newest='{newest}'")
			return newest
		#
		def githubreleases(self, githubType="name"):
			logger.debug(f"listVersions: Parsers: githubreleases: Start processing githubType='{githubType}'")
			m = re.search(r'http?s:\/\/github.com\/(.+\/.+\/releases)', self.url)
			if m is None:
				errorExit(f"listVersions: Parsers: githubreleases: Improper github release URL: '%s' (Example: https://github.com/exampleGroup/exampleProject/releases)" % (self.url))
			releaseApiUrl = 'https://api.github.com/repos/%s' % (m.groups()[0])
			jString = requests.get(releaseApiUrl, headers=objSETTINGS.HEADERS, timeout=2).content  # .decode("utf-8")
			releases = json.loads(jString)
			newest = "0.0.0"
			for r in releases:
				v = r[githubType]
				if self.verex is not None:
					m = re.search(self.verex, v)
					if m is not None:
						g = m.groupdict()
						if "version_num" not in g:
							errorExit(f"listVersions: Parsers: githubreleases: You have to name a regex group version_num")
						v = g["version_num"]
						if "rc_num" in g:
							v = v + "." + g["rc_num"]
					else:
						v = ""
				if v != "":
					if re.match(r"^(?P<version_num>(?:[\dx]{1,3}\.){0,3}[\dx]{1,3})$", v):
						if Version(v) > Version(newest):
							newest = v
			logger.debug(f"listVersions: Parsers: githubreleases: Finished processing, returning newest='{newest}'")
			return newest
		#
		def githubtags(self, githubType="tag"):
			logger.debug(f"listVersions: Parsers: githubtags: Start processing githubType='{githubType}'")
			m = re.search(r'http?s:\/\/github.com\/(.+\/.+\/tags)', self.url)
			if m is None:
				errorExit(f"listVersions: Parsers: githubtags: Improper github tag URL: '%s' (Example: https://github.com/exampleGroup/exampleProject/tags)" % (self.url))
			releaseApiUrl = 'https://api.github.com/repos/%s' % (m.groups()[0])
			jString = requests.get(releaseApiUrl, headers=objSETTINGS.HEADERS).content  # .decode("utf-8")
			releases = json.loads(jString)
			newest = "0.0.0"
			for r in releases:
				v = r[githubType]
				if self.verex is not None:
					m = re.search(self.verex, v)
					if m is not None:
						g = m.groupdict()
						if "version_num" not in g:
							errorExit(f"listVersions: Parsers: githubtags: You have to name a regex group version_num")
						v = g["version_num"]
						if "rc_num" in g:
							v = v + "." + g["rc_num"]
					else:
						v = ""
				if v != "":
					if re.match(r"^(?P<version_num>(?:[\dx]{1,3}\.){0,3}[\dx]{1,3})$", v):
						if Version(v) > Version(newest):
							newest = v
			logger.debug(f"listVersions: Parsers: githubtags: Finished processing, returning newest='{newest}'")
			return newest
		#
		def httpregex(self):
			logger.debug(f"listVersions: Parsers: httpregex: Start processing")
			r = requests.get(self.url, headers=objSETTINGS.HEADERS, timeout=2)
			html = r.content.decode("utf-8")
			m = re.findall(self.verex, html)
			newest = "0.0.0"
			for v in m:
				if v != "":
					if re.match(r"^(?P<version_num>(?:[\dx]{1,3}\.){0,3}[\dx]{1,3})$", v):
						if Version(v) > Version(newest):
							newest = v
			logger.debug(f"listVersions: Parsers: httpregex: Finished processing, returning newest='{newest}'")
			return newest
		#
		def ftp(self):
			logger.debug(f"listVersions: Parsers: ftp: Start processing")
			pUrl = urlparse(self.url)
			ftp = ftplib.FTP(pUrl.netloc, timeout=2)
			ftp.login()
			ftp.cwd(pUrl.path)
			files = []
			try:
				files = ftp.nlst()
			except ftplib.error_perm as resp:
				if str(resp) == "550 No files found":
					errorExit(f"listVersions: Parsers: ftp: FTP 550: No files in this directory")
				else:
					errorExit(f"listVersions: Parsers: ftp: Failed to parse version of " + pUrl + "\n\n" + traceback.format_exc())
			newest = "0.0.0"
			for v in files:
				if self.verex is not None:
					m = re.search(self.verex, v)
					if m is not None:
						g = m.groupdict()
						if "version_num" not in g:
							errorExit(f"listVersions: Parsers: ftp: You have to name a regex group version_num")
						v = g["version_num"]
						if "rc_num" in g:
							v = v + "." + g["rc_num"]
					else:
						v = ""
				if v != "":
					if re.match(r"^(?P<version_num>(?:[\dx]{1,3}\.){0,3}[\dx]{1,3})$", v):
						if Version(v) > Version(newest):
							newest = v
			logger.debug(f"listVersions: Parsers: ftp: Finished processing, returning newest='{newest}'")
			return newest
	###=== END OF LOCAL CLASS PARSERS
	###=== START OF LOCAL FUNCTIONS
	def getGitClonePathFromPkg(pkg):
		logger.debug(f"listVersions: getGitClonePathFromPkg: called with package:\n'{objPrettyPrint.pformat(pkg)}'")
		clonePath = None
		if "folder_name" in pkg:
			clonePath = pkg["folder_name"]
			clonePath = replaceVarCmdSubStrings(clonePath)
		if "rename_folder" in pkg:
			clonePath = pkg["rename_folder"]
			clonePath = replaceVarCmdSubStrings(clonePath)
		if "rename_folder" not in pkg and "folder_name" not in pkg:
			logger.debug(f"listVersions: getGitClonePathFromPkg: pkg['url']={objPrettyPrint.pformat(pkg['url'])}" )
			pUrl = urlparse(pkg["url"])
			clonePath = os.path.basename(replaceVarCmdSubStrings(pUrl.path)).replace(".", "_")
			if not clonePath.endswith("_git"):
				clonePath = clonePath + "_git"
		dirs = []
		for dir in BUILD_DIRS:
			mDir = os.path.join(dir, clonePath)
			dirs.append(mDir)
			if os.path.isdir(mDir):
				logger.debug(f"listVersions: getGitClonePathFromPkg: success for package '{pkg['packageName']}'. Returning folder '{mDir}'")
				return Path(mDir)
		logger.debug(f"listVersions: getGitClonePathFromPkg: failure for package '{pkg['packageName']}'. None of those folders exist: " + ", ".join(dirs))
		return None
	###
	def local_run(cmd):	# a local 'run' command, different to the global def 'runProcess'
		logger.debug(f"listVersions: local_run: '{cmd}' in '{os.getcwd()}'")
		r = subprocess.check_output(cmd, shell=True).decode("utf-8", "replace")
		logger.debug(f"listVersions: local_run: '{cmd}' returning with given return value: '{r}'")
		return r
	###
	def getCommitsDiff(pkg):
		logger.debug(f"listVersions: getCommitsDiff: Start processing")
		curCommit = None 
		master_branch_name = ""
		if "branch" in pkg:
			curCommit = replaceVarCmdSubStrings(pkg["branch"])
		logger.debug(f"listVersions: getCommitsDiff: curCommit='{curCommit}'")
		# repoUrl = replaceVarCmdSubStrings(pkg["url"])
		# latestCommit = None
		origDir = os.getcwd()
		clonePath = getGitClonePathFromPkg(pkg)
		if clonePath is None:
			return None, master_branch_name
		cchdir(clonePath,silent=True)
		#local_run("git remote update")
		dummy = runProcess("git remote update", ignoreErrors=True, silent=True, yield_return_code=False)
		if curCommit is not None:
			logger.debug(f"listVersions: getCommitsDiff: '{pkg['packageName']}': processing is not None: curCommit='{curCommit}' WHICH MEANS COMMIT SPECIFIED TO USE")
			##### 2023.02.20 attempt to try git_log in a meaningful order
			logger.debug(f"listVersions: getCommitsDiff: '{pkg['packageName']}': about to do 'git rev-parse --abbrev-ref HEAD'")
			#master_branch_name = runProcess("git branch --show-current", ignoreErrors=True, silent=True, yield_return_code=False).strip((" \n )		# returns '' if in detached state
			master_branch_name = runProcess("git rev-parse --abbrev-ref HEAD", ignoreErrors=True, silent=True, yield_return_code=False).strip(" \n ")	# returns 'HEAD' if in detached state or the BRANCH name if attached to a different branch name
			logger.debug(f"listVersions: getCommitsDiff: '{pkg['packageName']}': 'git rev-parse --abbrev-ref HEAD'  returned '{master_branch_name}'")
			if master_branch_name.lower() == "HEAD".lower() or master_branch_name.lower() not in ['master'.lower(), 'main'.lower(), 'default'.lower()]:	# maybe returned a 'detached state' name rather than the real branch name, or an attached name of a branch
				# assuming we have checked only checked out one branch, 'git branch' returns a multi-line (2 lines we hope), the line not starting with '*' is the one we want ... rely on it only being 2 lines
				# i.e. making a bold assumption.
				#	for example in any .py we use 'branch': 'main' or  'branch': 'default' if the main branch is other than 'master', or 'branch':  'commit_id'
				#	and any of these only checks out ONE branch (hopefully).
				# So ... if we have used 'branch':  'commit_id',
				#	then a "git rev-parse --abbrev-ref HEAD" will return 'HEAD' 
				#	and we assume a subsequent "git branch" will return only 2 lines
				#	where we can discard the line starting with "*"
				#	and the remaining 1 line when stripped will be the "real" name of the branch (HEAD) even with a detached HEAD.
				logger.debug(f"listVersions: getCommitsDiff: '{pkg['packageName']}': DETACHED HEAD: about to do 'git branch'")
				master_branch_name = runProcess("git branch", ignoreErrors=True, silent=True, yield_return_code=False)	# returns a string of 2 or more lines, the the commit check out and the local branches
				logger.debug(f"listVersions: getCommitsDiff: '{pkg['packageName']}': DETACHED HEAD: 'git branch (non-edited)' returned \"{objPrettyPrint.pformat(master_branch_name)}\"")
				master_branch_name = [line for line in master_branch_name.splitlines() if not line.startswith('*')]
				master_branch_name = master_branch_name[0].strip(" \n ")
				logger.debug(f"listVersions: getCommitsDiff: '{pkg['packageName']}': DETACHED HEAD: 'git branch (edited)' returned \"{objPrettyPrint.pformat(master_branch_name)}\"")
			if master_branch_name.lower() == "master".lower():
				hh = ( "master", "main", "default" )	# a tuple, Tuple items are indexed, the first item has index [0], the second item has index [1] 
			elif master_branch_name.lower() == "main".lower():
				hh = ( "main", "master", "default" )	# a tuple, Tuple items are indexed, the first item has index [0], the second item has index [1] 
			elif master_branch_name.lower() == "default".lower():
				hh = ( "default", "master", "main" )	# a tuple, Tuple items are indexed, the first item has index [0], the second item has index [1] 
			elif curCommit.lower() == "master".lower():
				hh = ( "master", "main", "default" )	# a tuple, Tuple items are indexed, the first item has index [0], the second item has index [1] 
			elif curCommit.lower() == "main".lower():
				hh = ( "main", "master", "default" )	# a tuple, Tuple items are indexed, the first item has index [0], the second item has index [1] 
			elif curCommit.lower() == "default".lower():
				hh = ( "default", "master", "main" )	# a tuple, Tuple items are indexed, the first item has index [0], the second item has index [1] 
			else:
				hh = ( "master", "main", "default" )	# a tuple, Tuple items are indexed, the first item has index [0], the second item has index [1] 
			c_0=f'git log --pretty=format:\"%H;;%an;;%s\" {curCommit}..{hh[0]}'
			c_1=f'git log --pretty=format:\"%H;;%an;;%s\" {curCommit}..{hh[1]}'
			c_2=f'git log --pretty=format:\"%H;;%an;;%s\" {curCommit}..{hh[2]}'
			try:
				logger.debug(f"listVersions: getCommitsDiff: try using '{c_0}'")
				# TODO ... figure out what this somewhat obscure ambiguous line of python actually does]
				#cmts = [c.split(";;") for c in local_run(c_0).split("\n") if c != ""]
				cmts = [c.split(";;") for c in runProcess(c_0, ignoreErrors=True, silent=True, yield_return_code=False).split("\n") if c != ""]
			except: # an error occurred ... assume it's the trunkl=change thing
				logger.warning(f"listVersions: getCommitsDiff: {pkg['packageName']}: re-try using '{c_1}'")
				try:
					# TODO ... figure out what this somewhat obscure ambiguous line of python actually does]
					#cmts = [c.split(";;") for c in local_run(c_1).split("\n") if c != ""]
					cmts = [c.split(";;") for c in runProcess(c_1, ignoreErrors=True, silent=True, yield_return_code=False).split("\n") if c != ""]
					pass
				except:
					logger.warning(f"listVersions: getCommitsDiff: {pkg['packageName']}: re-try using '{c_2}'")
					try:
						# TODO ... figure out what this somewhat obscure ambiguous line of python actually does]
						#cmts = [c.split(";;") for c in local_run(c_2).split("\n") if c != ""]
						cmts = [c.split(";;") for c in runProcess(c_2, ignoreErrors=True, silent=True, yield_return_code=False).split("\n") if c != ""]
						pass
					except:
						logger.error(f"*** Fatal Exception: 'git log --pretty' ABORTED failed for all of 'master' 'main' 'default' in: '{pkg['packageName']}' ... aborting ...")
						logger.error(f"{c_0}\n{c_1}\n{c_2}")
						logger.error(f"Unexpected error: '{sys.exc_info()[0]}'")
						raise
			#####
			#----
			# 2020.06.22 try to cater for either/or or "master" or "main"
			#c_master=("git log --pretty=format:\"%H;;%an;;%s\" {0}..master".format(curCommit))
			#c_main=("git log --pretty=format:\"%H;;%an;;%s\" {0}..main".format(curCommit))
			#c_default=("git log --pretty=format:\"%H;;%an;;%s\" {0}..default".format(curCommit))
			#try: # 2020.06.22 try using "master"
			#	logger.debug(f"listVersions: getCommitsDiff: try using '{c_master}'")
			#	# TODO ... figure out what this somewhat obscure ambiguous line of python actually does]
			#	cmts = [c.split(";;") for c in local_run(c_master).split("\n") if c != ""]
			#except: # an error occurred ... assume it's the trunkl=change thing
			#	logger.warning(f"listVersions: getCommitsDiff: {pkg['packageName']}: re-try using '{c_main}'")
			#	try: # 2020.06.22 re-try using "main" instead of "master"
			#		# TODO ... figure out what this somewhat obscure ambiguous line of python actually does]
			#		cmts = [c.split(";;") for c in local_run(c_main).split("\n") if c != ""]
			#		pass
			#	except:
			#		logger.warning(f"listVersions: getCommitsDiff: {pkg['packageName']}: re-try using '{c_default}'")
			#		try: # 2020.06.22 re-try using "default" instead of "main" instead of "master"
			#			# TODO ... figure out what this somewhat obscure ambiguous line of python actually does]
			#			cmts = [c.split(";;") for c in local_run(c_default).split("\n") if c != ""]
			#			pass
			#		except:
			#			logger.error(f"*** Fatal Exception: 'git log --pretty' ABORTED failed for all of 'master' 'main' 'default' in: '{pkg['packageName']}' ... aborting ...")
			#			logger.error(f"{c_master}\n{c_main}\n{c_default}")
			#			logger.error(f"Unexpected error: '{sys.exc_info()[0]}'")
			#			raise
			#----
		else:
			logger.debug(f"listVersions: getCommitsDiff: processing curCommit is None: WHICH MEANS NO COMMIT SPECIFIED")
			cmtsBehind = 0
			try:
				#cmtsBehind = re.search(r"## .* \[behind ([0-9]+)\]", local_run("git status -sb").split("\n")[0]).groups()[0]
				cmtsBehind = re.search(r"## .* \[behind ([0-9]+)\]", runProcess("git status -sb", ignoreErrors=True, silent=True, yield_return_code=False).split("\n")[0]).groups()[0]
			except Exception:
				# print(local_run("git status -sb").split("\n")[0])
				# print(runProcess("git status -sb", ignoreErrors=True, silent=True, yield_return_code=False).split("\n")[0])
				pass
			cmts = int(cmtsBehind)
		cchdir(origDir,silent=True)
		logger.debug(f"listVersions: getCommitsDiff: returning with cmts='{cmts}'")
		return cmts, master_branch_name

	def geLatestVersion(versionElement):
		url = versionElement["url"]
		verex = None
		ghtype = None
		logger.debug(f"listVersions: geLatestVersion: Start processing with incoming versionElement='{versionElement}' url='{url}' verex='{verex}' ghtype='{ghtype}'") # versionElement is pkg["update_check"]
		if "regex" in versionElement:
			verex = versionElement["regex"]
		if "name_or_tag" in versionElement:
			ghtype = versionElement["name_or_tag"]
		pUrl = urlparse(url)
		#pUrl = replaceVarCmdSubStrings(pUrl)
		if pUrl.scheme == '':
			errorExit(f"listVersions: geLatestVersion: Update check URL '{url}' is invalid.")
		logger.debug(f"listVersions: geLatestVersion: BEFORE TRY url='{url}' verex='{verex}' ghtype='{ghtype}' pUrl='{pUrl}'")
		try:
			pType = replaceVarCmdSubStrings(versionElement["type"])
			parser = Parsers(url, verex)	# start an instance of the parser
			if pType == "sourceforge":
				logger.debug(f"listVersions: geLatestVersion: TRY: CALLING sourceforge WITH url='{url}' verex='{verex}' ghtype='{ghtype}' pUrl='{pUrl}'")
				r = parser.sourceforge()
				logger.debug(f"listVersions: geLatestVersion: TRY: CALLED sourceforge WITH url='{url}' verex='{verex}' ghtype='{ghtype}' pUrl='{pUrl}'\nRETURNED='{r}'")
				return r
			elif pType == "httpindex":
				logger.debug(f"listVersions: geLatestVersion: TRY: CALLING httpindex WITH url='{url}' verex='{verex}' ghtype='{ghtype}' pUrl='{pUrl}'")
				r = parser.httpindex()
				logger.debug(f"listVersions: geLatestVersion: TRY: CALLED httpindex WITH url='{url}' verex='{verex}' ghtype='{ghtype}' pUrl='{pUrl}'\nRETURNED='{r}'")
				return r
			elif pType == "ftpindex":
				logger.debug(f"listVersions: geLatestVersion: TRY: CALLING ftp WITH url='{url}' verex='{verex}' ghtype='{ghtype}' pUrl='{pUrl}'")
				r = parser.ftp()
				logger.debug(f"listVersions: geLatestVersion: TRY: CALLED ftp WITH url='{url}' verex='{verex}' ghtype='{ghtype}' pUrl='{pUrl}'\nRETURNED='{r}'")
				return r
			elif pType == "httpregex":
				logger.debug(f"listVersions: geLatestVersion: TRY: CALLING httpregex WITH url='{url}' verex='{verex}' ghtype='{ghtype}' pUrl='{pUrl}'")
				r = parser.httpregex()
				logger.debug(f"listVersions: geLatestVersion: TRY: CALLED httpregex WITH url='{url}' verex='{verex}' ghtype='{ghtype}' pUrl='{pUrl}'\nRETURNED='{r}'")
				return r
			elif pType == "githubreleases":
				logger.debug(f"listVersions: geLatestVersion: TRY: CALLING githubreleases WITH url='{url}' verex='{verex}' ghtype='{ghtype}' pUrl='{pUrl}'")
				r = parser.githubreleases(ghtype)
				logger.debug(f"listVersions: geLatestVersion: TRY: CALLED githubreleases WITH url='{url}' verex='{verex}' ghtype='{ghtype}' pUrl='{pUrl}'\nRETURNED='{r}'")
				return r
			elif pType == "githubtags":
				logger.debug(f"listVersions: geLatestVersion: TRY: CALLING githubtags WITH url='{url}' verex='{verex}' ghtype='{ghtype}' pUrl='{pUrl}'")
				r = parser.githubtags(ghtype)
				logger.debug(f"listVersions: geLatestVersion: TRY: CALLED githubtags WITH url='{url}' verex='{verex}' ghtype='{ghtype}' pUrl='{pUrl}'\nRETURNED='{r}'")
				return r
			else:
				errorExit(f"listVersions: geLatestVersion: Unknown parser: '{pType}'")
			del parser	# remove the object 'parser'
		except Exception:
			errorExit(f"listVersions: geLatestVersion: Failed to parse version of '{url}'\n\n{traceback.format_exc()}")
		logger.error(f"listVersions: geLatestVersion: end of  processing ... it should NEVER get to here.")
	###=== END OF LOCAL FUNCTIONS
	#
	###=== START OF NORMAL FUNCTION PROCSSING
	logger.info(f"listVersions: Processing checking for version and possible updates")
	cchdir(objSETTINGS.fullWorkDir,silent=True)
	##logger.debug(f"listVersions: doing init() from colorama ")
	##init()	# from within: import Fore, Style, init
	BUILD_DIRS = [ objSETTINGS.bitnessPath, objSETTINGS.fullProductDir, objSETTINGS.fullOfftreeDir]	# eg {stuff}/workdir/x86_64, {stuff}/workdir/x86_64_products/, {stuff}/workdir/x86_64_offtree/
	logger.debug(f"listVersions: build folders to check: '{BUILD_DIRS}'")

	# process Products
	#for packageName in sorted(dictProducts.BO.keys()):
	#	print(f"dictProducts key='{packageName}'")
	#	pkg = biggusDictus[packageName]
	# process Dependencies
	#for packageName in sorted(dictDependencies.BO.keys()):
	#	print(f"dictDependencies key='{packageName}'")
	#	pkg = biggusDictus[packageName]
	# process Variables 
	#... nothing to do
	#pass

	ignorePkgsUpdate = []
	pkgsWithoutUpdateCheck = []

	print("\nChecking PRODUCT versions:")
	for name, pkg in sorted(dictProducts.BO.items(),key=lambda i: i[0].casefold()):
		pkg["packageName"] = name
		logger.debug(f"Checking product %s ..." % (name))
		if "repo_type" in pkg and (pkg["repo_type"] == "archive" or (pkg["repo_type"] == "git" and "branch" in pkg)):  # check for packages without update check.
			if "update_check" not in pkg:
				if name not in ignorePkgsUpdate:
					pkgsWithoutUpdateCheck.append(name)
					logger.debug(f"listVersions: PRODUCTS: pkgsWithoutUpdateCheck updated:\n{objPrettyPrint.pformat(pkgsWithoutUpdateCheck)}")
		if "update_check" in pkg :
			versionElement = pkg["update_check"]
			vType = versionElement["type"]
			logger.debug(f"listVersions: PRODUCTS: name='{name}' vType='{vType}'")
			if vType == "git":  # packages that are git clones
				di = None
				master_branch_name = None
				try:
					di, master_branch_name = getCommitsDiff(pkg)
					logger.debug(f"listVersions: PRODUCTS: GIT: name='{name}' vType='{vType}' master_branch_name='{master_branch_name}' di='{objPrettyPrint.pformat(di)}' ")
				except Exception as e:
					logger.warning(f"{e}")
					continue
				if di is not None:
					numCmts = 0
					if isinstance(di, int):
						numCmts = di
					else:
						numCmts = len(di)
					gitaffixed = ""
					if "branch" in pkg:
						gitaffixed = gitaffixed + " ... affixed at " + replaceVarCmdSubStrings(pkg["branch"])
					if "checkout" in pkg:
						gitaffixed = gitaffixed + " ... affixed at " + replaceVarCmdSubStrings(pkg["checkout"])
					if gitaffixed == "":
						gitaffixed = " ... Git Head"
					if numCmts > 0:
						print(f"{Colors.LIGHTYELLOW_EX}%s {Colors.RED}is %d commits behind {master_branch_name} ! %s{Colors.RESET}" % (name.rjust(30), numCmts, gitaffixed))
					else:
						print(f"{Colors.LIGHTYELLOW_EX}%s {Colors.LIGHTGREEN_EX}is up to date. %s{Colors.RESET}" % (name.rjust(30), gitaffixed))
			else:  # packages that are archive downloads
				ourVer = pkg["_info"]["version"]
				logger.debug(f"listVersions: PRODUCTS: non-git: name='{name}' vType='{vType}' ourVer={ourVer}")
				try:
					latestVer = geLatestVersion(versionElement)
				except Exception:
					logger.warning(f"listVersions: PRODUCTS: non-git processing: EXCEPTION: name='{name}' vType='{vType}' ourVer={ourVer}")
					continue
				if latestVer == "0.0.0":
					print(f"{Colors.LIGHTYELLOW_EX}%s {Colors.RED}may have an update! [Local: %s Remote: %s] (Error parsing remote version){Colors.RESET}" % (name.rjust(30), ourVer.center(10), latestVer.center(10)))
					#print("%s Regex pattern:" % name)
					try:
						#print("\t" + versionElement["regex"])
						pass
					except:
						#print("\nIgnored Error determining 'versionElement[\"regex\"]'")
						pass
				elif Version(ourVer) < Version(latestVer):
					print(f"{Colors.LIGHTYELLOW_EX}%s {Colors.RED}has an update! [Local: %s Remote: %s]{Colors.RESET}" % (name.rjust(30), ourVer.center(10), latestVer.center(10)))
				else:
					print(f"{Colors.LIGHTYELLOW_EX}%s {Colors.LIGHTGREEN_EX}is up to date. [Local: %s Remote: %s]{Colors.RESET}" % (name.rjust(30), ourVer.center(10), latestVer.center(10)))

	print("\nChecking DEPENDENCY versions:")
	for name, pkg in sorted(dictDependencies.BO.items(),key=lambda i: i[0].casefold()):
		pkg["packageName"] = name
		logger.debug(f"Checking dependency %s ..." % (name))
		if "repo_type" in pkg and (pkg["repo_type"] == "archive" or (pkg["repo_type"] == "git" and "branch" in pkg)):  # check for packages without update check.
			if "update_check" not in pkg:
				if name not in ignorePkgsUpdate:
					pkgsWithoutUpdateCheck.append(name)
					logger.debug(f"listVersions: DEPENDENCIES: pkgsWithoutUpdateCheck updated:\n{objPrettyPrint.pformat(pkgsWithoutUpdateCheck)}")
		if "update_check" in pkg:
			versionElement = pkg["update_check"]
			vType = versionElement["type"]
			logger.debug(f"listVersions: DEPENDENCIES: name='{name}' vType='{vType}'")
			if vType == "git":  # packages that are git clones
				di, master_branch_name = getCommitsDiff(pkg)
				logger.debug(f"listVersions: DEPENDENCIES: GIT: name='{name}' vType='{vType}' master_branch_name='{master_branch_name}' di='{objPrettyPrint.pformat(di)}' ")
				if di is not None:
					numCmts = 0
					if isinstance(di, int):
						numCmts = di
					else:
						numCmts = len(di)
					gitaffixed = ""
					if "branch" in pkg:
						gitaffixed = gitaffixed + " ... affixed at " + replaceVarCmdSubStrings(pkg["branch"])
					if "checkout" in pkg:
						gitaffixed = gitaffixed + " ... affixed at " + replaceVarCmdSubStrings(pkg["checkout"])
					if gitaffixed == "":
						gitaffixed = " ... Git Head"
					if numCmts > 0:
						print(f"{Colors.LIGHTYELLOW_EX}%s {Colors.RED}is %d commits behind {master_branch_name} ! %s{Colors.RESET}" % (name.rjust(30), numCmts, gitaffixed))
					else:
						print(f"{Colors.LIGHTYELLOW_EX}%s {Colors.LIGHTGREEN_EX}is up to date. %s{Colors.RESET}" % (name.rjust(30), gitaffixed))
			else:  # packages that are archive downloads
				ourVer = pkg["_info"]["version"]
				logger.debug(f"listVersions: DEPENDENCIES: non-git processing before TRY: name='{name}' vType='{vType}' ourVer={ourVer}")
				try:
					latestVer = geLatestVersion(versionElement)
				except Exception:
					logger.debug(f"listVersions: DEPENDENCIES: non-git: EXCEPTION: name='{name}' vType='{vType}' ourVer={ourVer}")
					continue
				if latestVer == "0.0.0":
					print(f"{Colors.LIGHTYELLOW_EX}%s {Colors.RED}may have an update! [Local: %s Remote: %s] (Error parsing remote version){Colors.RESET}" % (name.rjust(30), ourVer.center(10), latestVer.center(10)))
					#print(f"%s Regex pattern:" % name)
					try:
						#print("\t" + versionElement["regex"])
						pass
					except:
						#print("\nIgnored Error determining 'versionElement[\"regex\"]'")
						pass
				elif Version(ourVer) < Version(latestVer):
					print(f"{Colors.LIGHTYELLOW_EX}%s {Colors.RED}has an update! [Local: %s Remote: %s]{Colors.RESET}" % (name.rjust(30), ourVer.center(10), latestVer.center(10)))
				else:
					print(f"{Colors.LIGHTYELLOW_EX}%s {Colors.LIGHTGREEN_EX}is up to date. [Local: %s Remote: %s]{Colors.RESET}" % (name.rjust(30), ourVer.center(10), latestVer.center(10)))

	print("\nGit packages without update_check:")
	#for name, pkg in sorted({**pkgs["deps"], **pkgs["prods"]}.items(),key=lambda i: i[0].casefold()):
	for name, pkg in sorted(biggusDictus.items(),key=lambda i: i[0].casefold()):
		pkg["packageName"] = name
		if "repo_type" in pkg and pkg["repo_type"] == "git" and "update_check" not in pkg:
			clonePath = getGitClonePathFromPkg(pkg)
			if clonePath is None:
				continue
			repoUrl = pkg["url"]
			origDir = os.getcwd()
			cchdir(clonePath,silent=True)
			local_run("git remote update")
			cmtsBehind = re.search(r"## .* \[behind ([0-9]+)\]", local_run("git status -sb").split("\n")[0])
			if cmtsBehind:
				print(f"{Colors.LIGHTYELLOW_EX}{clonePath.name} {Colors.RED}is {cmtsBehind.groups()[0]} commits behind{Colors.RESET}")
	if len(pkgsWithoutUpdateCheck) > 0:
		print("\nPackages without update check:\n%s" % (",".join(pkgsWithoutUpdateCheck)))

	print("\nFinished package and dependency version checking.")

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
		objSETTINGS.dump_vars(f"### debugMode: DEBUG SETTINGS INTERNAL VARIABLES DUMP:")
	
	# Initialize Logging, this depends on objSETTINGS being initialized first
	initLogger()

	# Initialize DEBUG mode ... do it ONLY ONLY AFTER initLogger() since that sets the initial loglevel inside the logger
	setDebugMode(objSETTINGS.debugMode)

	# Process CMDLINE arguments into variables in the processCmdLineArguments object
	objArgParser = processCmdLineArguments()
	#if objSETTINGS.debugMode:
	#	objArgParser.dump_vars(f"### processCmdLineArguments: SETTINGS INTERNAL VARIABLES DUMP:")
	#objParser = objArgParser.parser	# the actual parser object
	# And just because we can, retrieve the parser object from our new objArgParser object
	#if objSETTINGS.debugMode:
	#	global_dump_object_variables(objParser, "### objParser retrieved from objArgParser")
	logger.debug(f"*objArgParser.list='{objArgParser.list}' objArgParser.list_products='{objArgParser.list_products}' objArgParser.list_dependencies='{ objArgParser.list_dependencies}'")
	logger.debug(f"*objArgParser.info='{objArgParser.info}' objArgParser.info_required_by='{objArgParser.info_required_by}'")
	logger.debug(f"*objArgParser.info='{objArgParser.info}' objArgParser.info_depends_on='{objArgParser.info_depends_on}'")
	logger.debug(f"*objArgParser.info='{objArgParser.info}' objArgParser.list_versions='{objArgParser.list_versions}'")
	logger.debug(f"*objArgParser.build='{objArgParser.build}' objArgParser.build_PRODUCT='{objArgParser.build_PRODUCT}' objArgParser.build_DEPENDENCY='{objArgParser.build_DEPENDENCY}'")
	logger.debug(f"*objArgParser.debug='{objArgParser.debug}'")
	logger.debug(f"*objArgParser.force='{objArgParser.force}'")
	logger.debug(f"*objArgParser.allforce='{objArgParser.allforce}'")
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
	
	# for joint searching, combine both products and dependencies into a global biggusDictus, and flag the type of package in a new string "packageType"
	biggusDictus = dictProducts.BO | dictDependencies.BO		# allow both products and dependencies to be searched as one
	for packageName in dictProducts.BO.keys():
		biggusDictus[packageName]["packageType"] = "P".upper()	# a PRODUCT package type "P"
	for packageName in dictDependencies.BO.keys():
		biggusDictus[packageName]["packageType"] = "D".upper()	# a DEPENDENCY package type "D"
	
	# FOR DEBUG:
	logger.debug(f"DEBUG: start example substitutions")
	logger.debug(f"objSETTINGS.substitutionDict=")
	logger.debug(objPrettyPrint.pformat(objSETTINGS.substitutionDict))
	logger.debug(f"objVariables.Val=")
	logger.debug(objPrettyPrint.pformat(objVariables.Val))
	logger.debug(replaceVarCmdSubStrings("Example VAR: VAR(ffmpeg_config)VAR=\n'!VAR(ffmpeg_config)VAR!'"))
	logger.debug(replaceVarCmdSubStrings("Example CMD: CMD(pwd)CMD='!CMD(pwd)CMD!'"))
	logger.debug(replaceVarCmdSubStrings("Example Sub: target_OS='{target_OS}'"))
	logger.debug(f"DEBUG: finish example substitutions")
	
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
			objVariables.list_print(heading='VARIABLES')	# for good measure, always list Variables free,gratis after the others
		elif objArgParser.list_dependencies:			# ./this_script.py --debug list -p
			dictDependencies.list_print(heading='DEPENDENCIES')
			objVariables.list_print(heading='VARIABLES')	# for good measure, always list Variables free,gratis after the others
		elif objArgParser.list_versions:				# ./this_script.py --debug list --versions
			logger.debug(f" list_versions set, calling listVersions()")
			listVersions()							# uses biggusDictus for detail, getting key = package names from dictProducts.BO and dictDependencies.BO
		logger.info(f"Finished Processing 'list' commandline actions")
		exit()

	# Setup the general environment ... if necessary change settings in objSETTINGS
	# set other variables including eg for "{cmake_prefix_options}" "!VARxxxVAR!" "!CMDyyyCMD!" etc
	# what to build is in objArgParser
	# create folders
	# init environment variables using os.environ
	#
	#resetDefaultEnvVars()	# this is done within prepareForBuilding()
	# 
	prepareForBuilding()	# also does cchdir(objSETTINGS.fullWorkDir)

	# Setup the mingw64 build environment and build the cross-compiling compilers etc
	# what to build is in objArgParser
	# settings to use are in objSETTINGS ... if necessary change settings in objSETTINGS
	buildMingw64()			# also does cchdir(objSETTINGS.fullWorkDir)
	#logger.debug(f"after buildMingw64()")

	# OK. By the time we're here, we have created folders and built mingW64.
	# So, review the specified package, could be a dependency, dependency tree, product, product tree.
	# The package name will be in objArgParser.
	if objSETTINGS.debugMode:
		#logger.debug(f"after buildMingw64() debugMode, checking for objArgParser.build checking for validity of product/dependency to build")
		if objArgParser.build:
			if objArgParser.build_PRODUCT is not None:
				if objArgParser.build_PRODUCT not in dictProducts.BO:
					logger.error(f"Specified build PRODUCT:'{objArgParser.build_PRODUCT}' however no matching product name found.")
					sys.exit(1)
				#obj_top_Package = dictProducts.get_dot_py_obj(objArgParser.build_PRODUCT)		# returns an object of class dot_py_object 
				#logger.info(f"About to Build PRODUCT='{objArgParser.build_PRODUCT}'")
				reviewPackageTree(objArgParser.build_PRODUCT)
				#logger.info(f"Finished Build of PRODUCT='{objArgParser.build_PRODUCT}'")
			elif objArgParser.build_DEPENDENCY is not None:
				if objArgParser.build_DEPENDENCY not in dictDependencies.BO:
					logger.error(f"Specified build DEPENDENCY:'{objArgParser.build_DEPENDENCY}' however no matching dependency name found.")
					sys.exit(1)
				#obj_top_Package = dictDependencies.get_dot_py_obj(objArgParser.build_DEPENDENCY)		# returns an object of class dot_py_object 
				#logger.info(f"About to Build DEPENDENCY='{objArgParser.build_DEPENDENCY}'")
				reviewPackageTree(objArgParser.build_DEPENDENCY)
				#logger.info(f"Finished Build of DEPENDENCY='{objArgParser.build_DEPENDENCY}'")
			else:
				msg = f"Hmm, BUILD specified, but no package named: PRODUCT='{objArgParser.build_PRODUCT}' DEPENDENCY='{objArgParser.build_DEPENDENCY}' ... exiting"
				logger.error(msg)
				sys.exit(1)
		else:
			msg = f"Hmm, BUILD was not specified but nothing else was either : PRODUCT='{objArgParser.build_PRODUCT}' DEPENDENCY='{objArgParser.build_DEPENDENCY}' ... that's an error condition ... exiting"
			logger.error(msg)
			sys.exit(1)

	# Well, looks like we finally have to build the specified package
	if objArgParser.force:	# only force the nominated package to be rebuilt (buildPackage will take care of it)
		forceRebuild = True
	else:
		forceRebuild = False	
	if objArgParser.allforce:	# force the nominated package to be rebuilt (buildPackage will take care of it)
		forceRebuild = True
	if objArgParser.build:
		if objArgParser.build_PRODUCT is not None:
			if objArgParser.build_PRODUCT not in dictProducts.BO:
				logger.error(f"Specified build PRODUCT:'{objArgParser.build_PRODUCT}' however no matching product name found.")
				sys.exit(1)
			buildPackage(objArgParser.build_PRODUCT, forceRebuild)
		elif objArgParser.build_DEPENDENCY is not None:
			if objArgParser.build_DEPENDENCY not in dictDependencies.BO:
				logger.error(f"Specified build DEPENDENCY:'{objArgParser.build_DEPENDENCY}' however no matching dependency name found.")
				sys.exit(1)
			buildPackage(objArgParser.build_DEPENDENCY, forceRebuild)
		else:
			msg = f"Hmm, BUILD specified, but no package named: PRODUCT='{objArgParser.build_PRODUCT}' DEPENDENCY='{objArgParser.build_DEPENDENCY}' ... exiting"
			logger.error(msg)
			sys.exit(1)
	else:
		msg = f"Hmm, BUILD was not specified but nothing else was either : PRODUCT='{objArgParser.build_PRODUCT}' DEPENDENCY='{objArgParser.build_DEPENDENCY}' ... that's an error condition ... exiting"
		logger.error(msg)
		sys.exit(1)


	# All Finished.
	exit()

##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
