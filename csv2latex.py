#Program to convert CSV formatted tables into LaTeX format
#By Will Townes, will.townes@gmail.com
#July 2011
import os, csv

if os.name.lower() == 'nt':
    #Windows version
    path = os.environ['USERPROFILE']+'\\Desktop'
    ifile = '\\data.csv'
    ofile = '\\LaTeXdata.txt'
    newline = '\n'
else:
    #Mac or Linux version
    path = os.environ['HOME']+'/desktop'
    ifile = '/data.csv'
    ofile = '/LaTeXdata.txt'
    newline = '\r'

f = csv.DictReader(open(path+ifile,'rb'))
ofile2 = open(path+ofile,'wb')
csv.register_dialect('latex',delimiter='&',quotechar='"') #define LaTeX dialect
g = csv.DictWriter(ofile2,f.fieldnames,dialect='latex',extrasaction='raise')
g.writerow(dict((h,h) for h in f.fieldnames)) #write header row
for i in f:
    g.writerow(i)
ofile2.close()

x = open(path+ofile,'r').readlines()
y = open(path+ofile,'w')
for i in x: #escape all dollar signs for currency data, add '\\' to end of lines
    y.write(i.replace(newline,'\\\\'+newline).replace('$','\\$'))
y.close()
    

