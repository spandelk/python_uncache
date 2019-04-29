# -*- coding: utf-8 -*-
# @Author: Jutju
# @Date:   2019-04-27 18:08:47
# @File:   __main__.py
# @Last Modified by:   Jutju
# @Last Modified time: 2019-04-30 00:31:23

import os
import sys
import shutil
import argparse
import magic
# import libmagic
# import colorama
from mimeTypes import mimeTypes
# from termcolor import colored

version = 'v0.0.1'

parser = argparse.ArgumentParser(description='"Uncache" files from the provided directory')
# group = parser.add_mutually_exclusive_group()
parser.add_argument('-v', '--version', version=version, action='version')
parser.add_argument('-i', '--input',  help='Input directory', required=True)
parser.add_argument('-o', '--output', help='Output directory. Will be created if does not exist. If not provided, defaults to "[INPUT]_uncache"')
args = parser.parse_args()

in_dir = args.input
out_dir = args.output

if not os.path.isdir(in_dir):
    sys.exit('"{}" is not a valid directory!'.format(in_dir))
elif os.path.isdir(in_dir):
    in_dir = os.path.abspath(in_dir)

if not out_dir:
    out_dir = '{}_uncache'.format(in_dir)
elif out_dir:
    if os.path.isfile(out_dir):
        sys.exit('"{}" is not a valid directory!'.format(out_dir))
    elif not os.path.isfile(out_dir):
        out_dir = os.path.abspath(out_dir)

print('Input: {}'.format(in_dir))
print('Output: {}'.format(out_dir))

m = magic.Magic(mime=True, uncompress=True)
files =[]

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

for key, value in mimeTypes.items():
    if not os.path.exists('{}/{}'.format(out_dir, value)):
        os.makedirs('{}/{}'.format(out_dir, value))

for file in os.listdir(in_dir):
    if not os.path.isdir(file):
        files.append(file)
    else:
        pass

for f in files:
    ff = '{}/{}'.format(in_dir, f)
    mime = m.from_file(ff)
    if mime in mimeTypes:
        mime = mimeTypes[mime]
    else:
        print('MIME type "{}" for file "{}" was not found in the dictionary!'.format(mime, ff))
        pass
    if os.path.exists('{}/{}'.format(out_dir, mime)):
        shutil.copy2(ff, '{}/{}/{}.{}'.format(out_dir, mime, f, mime))
    else:
        pass
    # print('{}/{}/{}.{}'.format(out_dir, mime, f, mime))

for key, value in mimeTypes.items():
    if not os.listdir('{}/{}'.format(out_dir, value)):
        os.rmdir('{}/{}'.format(out_dir, value))
