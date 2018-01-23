#!/usr/bin/env python

from os import listdir
from os.path import isfile, join
import io

def _load_txt(filename, encoding='utf-8'):
    return io.open(filename, 'r', encoding=encoding)

def read_txts():
    files = [join("../../resources", f) for f in listdir("../../resources") if isfile(join("../../resources", f))]
    txts = [_load_txt(file).read() for file in files if file.endswith('txt')]
    return txts

