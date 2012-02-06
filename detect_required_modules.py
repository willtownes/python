'''
Script to detect all the modules required by the python scripts in the specified directory
Will Townes
'''

import os, re
#path = raw_input('Please paste in the directory you want to inspect')
path = os.path.join(os.environ['USERPROFILE'],r'My Documents\work\scripts')
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
    #include all "import" statements except those that are commented out.
    modules.extend([line.rstrip() for line in f if 'import' in line and line[0] != '\#'])
modules.sort()
modules = list(set(modules)) #remove duplicates
for i in range(len(modules)):
    if '#' not in modules[i]:
        pass
    else:
        modules[i] = modules[i].split('#')[0] #get rid of everything to the right of the comment marker
modules = [i for i in modules if 'import' in i] #get rid of lines without import statements
pkg = set()
for i in modules:
    if 'from' in i:
        pkg.add(i.split(' ')[1])
    elif 'as' in i:
        pkg.add(i.split('as')[0].split(' ')[1])
    else:
        j = i.split('import')[1].split(',')
        j = set([k.strip() for k in j])
        pkg = pkg|j #set union operation adds the additional packages to the list
print('The following modules are needed to run the scripts:')
for i in sorted(list(pkg)):
    print(i)
