#{
#	'repo_type' : 'git',
#	'url' : 'https://github.com/DeadSix27/python_mingw_libs.git',
#	'needs_configure' : False,
#	'needs_make_install' : False,
#	# python 3.7.5
#	'build_options' : 'PREFIX={target_prefix} GENDEF={mingw_binpath}/gendef DLLTOOL={mingw_binpath}/{cross_prefix_bare}dlltool PYTHON_VERSION=3.7.5',
#	'_info' : { 'version' : '3.7.5', 'fancy_name' : 'Python (library-only)' },
#}
{
	'repo_type' : 'git',
	'url' : 'https://github.com/DeadSix27/python_mingw_libs.git',
	'needs_configure' : False,
	'needs_make_install' : False,
	# python 3.8.2
	'run_post_patch' : [
		'sed -i.bak "s;3.7.5;3.8.2;g" "Makefile"',
		'sed -i.bak "s;_DEBUG = False;_DEBUG = True;g" "install_python_libs.py"',
		'sed -i.bak "s;\'3.7.5\';\'3.7.5\',\'3.8.2\';g" "install_python_libs.py"',
		'sed -i.bak "s; 3.7.5 ; 3.8.2 ;g" "install_python_libs.py"',
	],
	'build_options' : 'PREFIX={target_prefix} GENDEF={mingw_binpath}/gendef DLLTOOL={mingw_binpath}/{cross_prefix_bare}dlltool PYTHON_VERSION=3.8.2',
}
#
# MABS:
#
#if  { ! mpv_disabled vapoursynth || enabled vapoursynth; }; then
#    _python_ver=3.8.2
#    _python_lib=python38
#    [[ $bits = 64bit ]] && _arch=amd64 || _arch=win32
#    _check=("lib$_python_lib.a")
#    if files_exist "${_check[@]}"; then
#        do_print_status "python $_python_ver" "$green" "Up-to-date"
#    elif do_wget "https://www.python.org/ftp/python/$_python_ver/python-$_python_ver-embed-$_arch.zip"; then
#        gendef "$_python_lib.dll" >/dev/null 2>&1
#        dlltool -y "lib$_python_lib.a" -d "$_python_lib.def"
#        [[ -f "lib$_python_lib.a" ]] && do_install "lib$_python_lib.a"
#        do_checkIfExist
#    fi
#    _vsver=49
#    _check=(lib{vapoursynth,vsscript}.a vapoursynth{,-script}.pc vapoursynth/{VS{Helper,Script},VapourSynth}.h)
#    if pc_exists "vapoursynth = $_vsver" && files_exist "${_check[@]}"; then
#        do_print_status "vapoursynth R$_vsver" "$green" "Up-to-date"
#    elif do_wget "https://github.com/vapoursynth/vapoursynth/releases/download/R$_vsver/VapourSynth${bits%bit}-Portable-R$_vsver.7z"; then
#        do_uninstall {vapoursynth,vsscript}.lib include/vapoursynth "${_check[@]}"
#        do_install sdk/include/*.h include/vapoursynth/
#        create_build_dir
#        declare -A _pc_vars=(
#            [vapoursynth-name]=vapoursynth
#            [vapoursynth-description]='A frameserver for the 21st century'
#            [vapoursynth-cflags]="-DVS_CORE_EXPORTS"
#            [vsscript-name]=vapoursynth-script
#            [vsscript-description]='Library for interfacing VapourSynth with Python'
#            [vsscript-private]="-l$_python_lib -lstdc++"
#        )
#        for _file in vapoursynth vsscript; do
#            gendef - "../$_file.dll" 2>/dev/null |
#                sed -E 's|^_||;s|@[1-9]+$||' > "${_file}.def"
#            # shellcheck disable=SC2046
#            dlltool -y "lib${_file}.a" -d "${_file}.def" \
#                $([[ $bits = 32bit ]] && echo "-U") 2>/dev/null
#            [[ -f lib${_file}.a ]] && do_install "lib${_file}.a"
#            # shellcheck disable=SC2016
#            printf '%s\n' \
#               "prefix=$LOCALDESTDIR" \
#               'exec_prefix=${prefix}' \
#               'libdir=${exec_prefix}/lib' \
#               'includedir=${prefix}/include/vapoursynth' \
#               "Name: ${_pc_vars[${_file}-name]}" \
#               "Description: ${_pc_vars[${_file}-description]}" \
#               "Version: $_vsver" \
#               "Libs: -L\${libdir} -l${_file}" \
#               "Libs.private: ${_pc_vars[${_file}-private]}" \
#               "Cflags: -I\${includedir} ${_pc_vars[${_file}-cflags]}" \
#               > "${_pc_vars[${_file}-name]}.pc"
#        done
#        do_install vapoursynth{,-script}.pc lib/pkgconfig/
#        do_checkIfExist
#    fi
#    unset _arch _file _python_lib _python_ver _vsver _pc_vars
#else
#    mpv_disable vapoursynth
#    do_removeOption --enable-vapoursynth
#fi
