#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os


def get_type():
	return "LIBRARY"

def get_desc():
	return "JPEG 2000 reade writer"

def get_licence():
	return "BSD-2"

def get_compagny_type():
	return "org"

def get_compagny_name():
	return "openjpeg"

def get_maintainer():
	return [
	    "David Janssens",
	    "Kaori Hagihara",
	    "Jerome Fimes",
	    "Giuseppe Baruffa",
	    "Mickael Savinaud",
	    "Mathieu Malaterre"
	    ]

def get_version():
	return [2,1,2]

def configure(target, my_module):
	if "MacOs" in target.get_type():
		return False
	my_module.add_src_file([
	    'openjpeg/src/lib/openjp2/thread.c',
	    'openjpeg/src/lib/openjp2/bio.c',
	    'openjpeg/src/lib/openjp2/cio.c',
	    'openjpeg/src/lib/openjp2/dwt.c',
	    'openjpeg/src/lib/openjp2/pi.c',
	    'openjpeg/src/lib/openjp2/event.c',
	    'openjpeg/src/lib/openjp2/image.c',
	    'openjpeg/src/lib/openjp2/invert.c',
	    'openjpeg/src/lib/openjp2/j2k.c',
	    'openjpeg/src/lib/openjp2/jp2.c',
	    'openjpeg/src/lib/openjp2/mct.c',
	    'openjpeg/src/lib/openjp2/mqc.c',
	    'openjpeg/src/lib/openjp2/openjpeg.c',
	    'openjpeg/src/lib/openjp2/opj_clock.c',
	    'openjpeg/src/lib/openjp2/pi.c',
	    'openjpeg/src/lib/openjp2/raw.c',
	    'openjpeg/src/lib/openjp2/t1.c',
	    'openjpeg/src/lib/openjp2/t2.c',
	    'openjpeg/src/lib/openjp2/tcd.c',
	    'openjpeg/src/lib/openjp2/tgt.c',
	    'openjpeg/src/lib/openjp2/function_list.c',
	    'openjpeg/src/lib/openjp2/opj_malloc.c',
	    ])
	my_module.add_flag('c', [
	    '-DMUTEX_pthread',
	    '-Dopenjp2_EXPORTS'
	    ])
	my_module.compile_version("c", 1999)
	my_module.add_depend([
	    'z',
	    'm',
	    'pthread',
	    ])
	my_module.add_path("openjpeg/src/lib/openjp2/")
	my_module.add_path("generated")
	my_module.add_header_file([
	    'openjpeg/src/lib/openjp2/openjpeg.h',
	    'openjpeg/src/lib/openjp2/function_list.h',
	    'openjpeg/src/lib/openjp2/bio.h',
	    'openjpeg/src/lib/openjp2/dwt.h',
	    'openjpeg/src/lib/openjp2/mct.h',
	    'openjpeg/src/lib/openjp2/opj_stdint.h',
	    'openjpeg/src/lib/openjp2/opj_malloc.h',
	    'openjpeg/src/lib/openjp2/jp2.h',
	    'openjpeg/src/lib/openjp2/raw.h',
	    'openjpeg/src/lib/openjp2/cio.h',
	    'openjpeg/src/lib/openjp2/thread.h',
	    'openjpeg/src/lib/openjp2/indexbox_manager.h',
	    'openjpeg/src/lib/openjp2/event.h',
	    'openjpeg/src/lib/openjp2/invert.h',
	    'openjpeg/src/lib/openjp2/mqc.h',
	    'openjpeg/src/lib/openjp2/tls_keys.h',
	    'openjpeg/src/lib/openjp2/opj_inttypes.h',
	    'openjpeg/src/lib/openjp2/t1_luts.h',
	    'openjpeg/src/lib/openjp2/pi.h',
	    'openjpeg/src/lib/openjp2/cidx_manager.h',
	    'openjpeg/src/lib/openjp2/image.h',
	    'openjpeg/src/lib/openjp2/opj_intmath.h',
	    'openjpeg/src/lib/openjp2/t1.h',
	    'openjpeg/src/lib/openjp2/mqc_inl.h',
	    'openjpeg/src/lib/openjp2/opj_includes.h',
	    'openjpeg/src/lib/openjp2/tcd.h',
	    'openjpeg/src/lib/openjp2/t2.h',
	    'openjpeg/src/lib/openjp2/j2k.h',
	    'openjpeg/src/lib/openjp2/tgt.h',
	    'openjpeg/src/lib/openjp2/opj_codec.h',
	    'openjpeg/src/lib/openjp2/opj_clock.h',
	    'generated/opj_config_private.h',
	    'generated/opj_config.h',
	    ],
	    destination_path="")
	return True
