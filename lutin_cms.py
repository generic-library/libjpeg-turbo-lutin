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
	my_module.add_src_file([
	    'openjpeg/thirdparty/liblcms2/src/cmsalpha.c',
	    'openjpeg/thirdparty/liblcms2/src/cmscam02.c',
	    'openjpeg/thirdparty/liblcms2/src/cmscgats.c',
	    'openjpeg/thirdparty/liblcms2/src/cmscnvrt.c',
	    'openjpeg/thirdparty/liblcms2/src/cmserr.c',
	    'openjpeg/thirdparty/liblcms2/src/cmsgamma.c',
	    'openjpeg/thirdparty/liblcms2/src/cmsgmt.c',
	    'openjpeg/thirdparty/liblcms2/src/cmshalf.c',
	    'openjpeg/thirdparty/liblcms2/src/cmsintrp.c',
	    'openjpeg/thirdparty/liblcms2/src/cmsio0.c',
	    'openjpeg/thirdparty/liblcms2/src/cmsio1.c',
	    'openjpeg/thirdparty/liblcms2/src/cmslut.c',
	    'openjpeg/thirdparty/liblcms2/src/cmsmd5.c',
	    'openjpeg/thirdparty/liblcms2/src/cmsmtrx.c',
	    'openjpeg/thirdparty/liblcms2/src/cmsnamed.c',
	    'openjpeg/thirdparty/liblcms2/src/cmsopt.c',
	    'openjpeg/thirdparty/liblcms2/src/cmspack.c',
	    'openjpeg/thirdparty/liblcms2/src/cmspcs.c',
	    'openjpeg/thirdparty/liblcms2/src/cmsplugin.c',
	    'openjpeg/thirdparty/liblcms2/src/cmsps2.c',
	    'openjpeg/thirdparty/liblcms2/src/cmssamp.c',
	    'openjpeg/thirdparty/liblcms2/src/cmssm.c',
	    'openjpeg/thirdparty/liblcms2/src/cmstypes.c',
	    'openjpeg/thirdparty/liblcms2/src/cmsvirt.c',
	    'openjpeg/thirdparty/liblcms2/src/cmswtpnt.c',
	    'openjpeg/thirdparty/liblcms2/src/cmsxform.c',
	    ])
	my_module.add_flag('c', [
	    '-DMUTEX_pthread',
	    '-Dopenjp2_EXPORTS'
	    ])
	my_module.compile_version("c", 1999)
	my_module.add_depend([
	    'z',
	    'm',
	    ])
	my_module.add_path("openjpeg/thirdparty/liblcms2/src/")
	my_module.add_header_file([
	    'openjpeg/thirdparty/liblcms2/include/lcms2.h',
	    'openjpeg/thirdparty/liblcms2/include/lcms2_plugin.h',
	    ],
	    destination_path="")
	return True



