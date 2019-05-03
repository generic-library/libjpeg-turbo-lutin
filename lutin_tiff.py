#!/usr/bin/python
import realog.debug as debug
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
	    'openjpeg/thirdparty/libtiff/tif_aux.c',
	    'openjpeg/thirdparty/libtiff/tif_close.c',
	    'openjpeg/thirdparty/libtiff/tif_codec.c',
	    'openjpeg/thirdparty/libtiff/tif_color.c',
	    'openjpeg/thirdparty/libtiff/tif_compress.c',
	    'openjpeg/thirdparty/libtiff/tif_dir.c',
	    'openjpeg/thirdparty/libtiff/tif_dirinfo.c',
	    'openjpeg/thirdparty/libtiff/tif_dirread.c',
	    'openjpeg/thirdparty/libtiff/tif_dirwrite.c',
	    'openjpeg/thirdparty/libtiff/tif_dumpmode.c',
	    'openjpeg/thirdparty/libtiff/tif_error.c',
	    'openjpeg/thirdparty/libtiff/tif_extension.c',
	    'openjpeg/thirdparty/libtiff/tif_fax3.c',
	    'openjpeg/thirdparty/libtiff/tif_fax3sm.c',
	    'openjpeg/thirdparty/libtiff/tif_flush.c',
	    'openjpeg/thirdparty/libtiff/tif_getimage.c',
	    'openjpeg/thirdparty/libtiff/tif_jbig.c',
	    'openjpeg/thirdparty/libtiff/tif_jpeg.c',
	    'openjpeg/thirdparty/libtiff/tif_luv.c',
	    'openjpeg/thirdparty/libtiff/tif_lzw.c',
	    'openjpeg/thirdparty/libtiff/tif_next.c',
	    'openjpeg/thirdparty/libtiff/tif_ojpeg.c',
	    'openjpeg/thirdparty/libtiff/tif_open.c',
	    'openjpeg/thirdparty/libtiff/tif_packbits.c',
	    'openjpeg/thirdparty/libtiff/tif_pixarlog.c',
	    'openjpeg/thirdparty/libtiff/tif_predict.c',
	    'openjpeg/thirdparty/libtiff/tif_print.c',
	    'openjpeg/thirdparty/libtiff/tif_read.c',
	    'openjpeg/thirdparty/libtiff/tif_strip.c',
	    'openjpeg/thirdparty/libtiff/tif_swab.c',
	    'openjpeg/thirdparty/libtiff/tif_thunder.c',
	    'openjpeg/thirdparty/libtiff/tif_tile.c',
	    'openjpeg/thirdparty/libtiff/tif_version.c',
	    'openjpeg/thirdparty/libtiff/tif_warning.c',
	    'openjpeg/thirdparty/libtiff/tif_write.c',
	    'openjpeg/thirdparty/libtiff/tif_zip.c',
	    'openjpeg/thirdparty/libtiff/tif_jpeg_12.c',
	    'openjpeg/thirdparty/libtiff/tif_lzma.c',
	    'openjpeg/thirdparty/libtiff/tif_unix.c',
	    ])
	"""
	my_module.add_flag('c', [
	    '-DMUTEX_pthread',
	    '-Dopenjp2_EXPORTS'
	    ])
	"""
	my_module.compile_version("c", 1999)
	my_module.add_depend([
	    'z',
	    'm',
	    ])
	my_module.add_path("openjpeg/src/lib/openjp2/")
	my_module.add_path("generated")
	my_module.add_header_file([
	    'openjpeg/thirdparty/libtiff/libport.h',
	    'openjpeg/thirdparty/libtiff/t4.h',
	    'generated/tif_config.h',
	    'openjpeg/thirdparty/libtiff/tif_dir.h',
	    'openjpeg/thirdparty/libtiff/tif_fax3.h',
	    'generated/tiffconf.h',
	    'openjpeg/thirdparty/libtiff/tiff.h',
	    'openjpeg/thirdparty/libtiff/tiffio.h',
	    'openjpeg/thirdparty/libtiff/tiffio.hxx',
	    'openjpeg/thirdparty/libtiff/tiffiop.h',
	    'openjpeg/thirdparty/libtiff/tiffvers.h',
	    'openjpeg/thirdparty/libtiff/tif_predict.h',
	    'openjpeg/thirdparty/libtiff/uvcode.h',
	    ],
	    destination_path="")
	return True

