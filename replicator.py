#Will Townes
import os, shutil, inspect

def replicate(n,ifile,directory):
    '''this program copies file "ifile" n times into the directory specified.
    ifile is a full path name.'''
    (name,ext) = ifile.split('\\')[-1].split('.')
    for i in range(n):
        shutil.copyfile(ifile,directory+'\\'+name+str(i)+'.'+ext)
        
if __name__ == "__main__":
    #this part 
    currentfile = inspect.getfile(inspect.currentframe())
    print(currentfile)
    replicate(5,currentfile,os.environ['USERPROFILE']+'\\Desktop')
