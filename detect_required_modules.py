'''
Script to detect all the modules required by the python scripts in the specified directory
Will Townes
'''

import os, re
#path = raw_input('Please paste in the directory you want to inspect')
path = r"C:\Documents and Settings\townesw\My Documents\work\scripts"
q = os.walk(path)
files = []
for root,directory,fil in os.walk(path):
    #if fil[-3:] == '.py':
    files.append((root,directory,fil))
pys = []
for j in files:
    pys.extend([os.path.join(j[0],i) for i in j[2] if i[-3:] == '.py'])
#pys is not a list of the path names to all python files in the directory and all subdirectories.
modules = []
for i in pys:
    f = open(i,'r').readlines()
    modules.extend([line for line in f if 'import' in line])
