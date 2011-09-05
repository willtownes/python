#Program to convert CSV formatted tables into LaTeX format
#By Will Townes, will.townes@gmail.com
#July 2011

'''
If you ever have the need to convert a CSV file into LaTeX format, feel free to use the attached script. It's written in python 2.6, which you can download for free here:
http://www.python.org/getit/releases/2.6.7/
However, Mac computers always have Python 2.5 installed ab initio, so you might not even need to install the more recent version. The way it works is, you save a file called "data.csv" to your desktop. Then run the script using the python launcher app. The output is a text file called "LaTeXdata.txt" also saved on your desktop. If you want to execute the script from the terminal, you would do something like the following (where $ represents the command prompt):
$cd desktop
$python csv2latex.py
If I make any updates I will keep the latest version of the script posted on github here:
https://github.com/willtownes/python/blob/master/csv2latex.py
'''
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
    

