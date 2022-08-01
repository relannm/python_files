'''
================================================================================
Simple file operations like:
    1. search for a file in a directory
    2. reading a file
        2.1 read by lines
        2.2 read the whole content of file
    3. searching for files (with specfic extension/filetype) in a directory

(C) Copyright 2019 Lear Corporation
================================================================================
'''

__author__  = 'Relan Morales'
__version__ = '1.0.0'

'''
CHANGE LOG
==========
1.0.0 Initial version -
'''

import os

def find_file(path, filename):
    '''
    Description: search for a specific file in a directory
    Input(s):
        path = root path where the file will be searched
        filename = specific file name (in format: filename.ext), where:
            - filename is the name of file
            - ext is the file type/extension
    Output(s):
        filepath = the path of the file (in format: path/filename)
    '''
    filepath = None
    for path, subdirs, files in os.walk(path):
        for file in files:
            if file == filename:
                filepath = os.path.join(path, file)
                return filepath
                break;
    return filepath

def find_files(path, ext):
    '''
    Purpose: find all files (with specific extension) within a directory
    Input(s):
        path = root path where the file will be searched
        ext = the file type/extension
    Output(s):  list of files (with the specified type/extension) in the format:
        [path/file1, path/file2 ...]
    '''
    file_list = []
    for path, subdirs, files in os.walk(path):
        for file in files:
            if file.endswith(ext):
                file_list.append(os.path.join(path, file))
    return file_list

def read_file(filepath):
    '''
    Purpose: read the file content
    Input(s): filepath - the path of the file (in format: path/filename)
    Output(s): content - the whole content of the file in string format
    '''
    f = open(filepath, 'r')
    content = f.read()
    f.close()
    return content

def read_file_lines(filepath):
    '''
    Purpose: read the file content
    Input(s): filepath - the path of the file (in format: path/filename)
    Output(s): content - the whole content of the file in list format where:
        each line in the file is an element of list
    '''
    f = open(filepath, 'r')
    content = f.readlines()
    f.close()
    return content
