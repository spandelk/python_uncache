# -*- coding: utf-8 -*-
# @Author: Krystian Spandel
# @Date:   2019-02-24 23:24:21
# @Last Modified by:   Krystian Spandel
# @Last Modified time: 2019-03-01 23:22:23

import magic
import os
import shutil
import sys
import colorama
from pathlib import Path
from termcolor import colored
colorama.init(autoreset=True)


def beError(errorType, bonusArg=0):
    if errorType == 'noDictFile':
        print(
            "Dictionary file not found!\n"
            "Make sure you have the right file with the name '" +
            colored('mimeTypes.py', 'yellow', 'on_red') + "'!"
        )
    if errorType == 'noArg':
        print("No directory specified!")
    if errorType == 'noMIME':
        print(
            "Uh oh! The given MIME type '" +
            colored(bonusArg, 'yellow', 'on_red') +
            "'was not found in the dictionary!\n"
            "Contact the developer on GitHub or add the type yourself!"
        )
    sys.exit(1)


try:
    from mimeTypes import mimeTypes
except ImportError:
    beError('noDictFile')
    sys.exit(1)

if len(sys.argv) == 1:
    beError('noArg')
else:
    workDir = sys.argv[1]

outDir = workDir + "_unCached"
workDir = Path(workDir)
outDir = Path(outDir)
files = []
m = magic.Magic(mime=True, uncompress=True)

if not os.path.exists(outDir):
    os.makedirs(outDir)

for key, value in mimeTypes.items():
    # if not os.path.exists(outDir + '\\' + value):
    #     os.makedirs(outDir + '\\' + value)
    if not os.path.exists(outDir / value):
        os.makedirs(outDir / value)

for file in os.listdir(workDir):
    if not os.path.isdir(file):
        files.append(file)
    else:
        pass

for f in files:
    df = str(workDir / f)
    mime = m.from_file(df)
    if mime in mimeTypes:
        mimeType = mimeTypes[mime]
    else:
        beError('noMIME', mime)
    print(f + ":" + mime)
    print(mimeType)
    print("")
    shutil.copy2(df, str(outDir / mimeType / f) + '.' + mimeType)

for key, value in mimeTypes.items():
    if not os.listdir(outDir / value):
        os.rmdir(outDir / value)
