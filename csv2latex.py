#Program to convert CSV formatted tables into LaTeX format
#By Will Townes
import os
path = os.environ['USERPROFILE']+'\\Desktop'
ifile = 'data.csv'
ofile = 'LaTeXdata.txt'
f = open(path+ifile,'r').readlines()
g = open(path+ofile,'w')
for i in range(len(f)):
    f[i] = f[i].replace(',','&')
    f[i] = f[i].replace('\n',r'\\'+'\n')
    g.write(f[i])
g.close()

