#!/usr/bin/python
import realog.debug as debug
import lutin.tools as tools


def get_type():
	return "BINARY"

def get_name():
	return "jpeg-2000-compressor"

def get_sub_type():
	return "TEST"

def get_desc():
	return "jpeg 2000 compressor"

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
	    "Micka Savinaud",
	    "Mathieu Malaterre"
	    ]

def get_version():
	return [2,1,2]

def configure(target, my_module):
	my_module.add_src_file([
	    'openjpeg/src/bin/jp2/opj_dump.c',
	    'openjpeg/src/bin/jp2/convert.c',
	    'openjpeg/src/bin/jp2/convertbmp.c',
	    'openjpeg/src/bin/jp2/index.c',
	    'openjpeg/src/bin/jp2/converttif.c',
	    'openjpeg/src/bin/jp2/convertpng.c',
	    'openjpeg/src/bin/common/color.c',
	    'openjpeg/src/bin/common/opj_getopt.c',
	    ])
	my_module.add_path("generated")
	my_module.add_path("openjpeg/src/bin/common/")
	my_module.add_depend([
	    'openjpeg',
	    'png',
	    'cms',
	    'tiff'
	    ])
	return True

