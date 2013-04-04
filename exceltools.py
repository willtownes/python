'''
Handy functions for reading in excel files (XLS or XLSX)
Currently does not support ragged arrays or multiple sheets
By Will Townes
'''

import xlrd

def summarize(myfile):
    '''practice function based on the library's documentation'''
    book = xlrd.open_workbook(myfile)
    print "The number of worksheets is", book.nsheets
    print "Worksheet name(s):", book.sheet_names()
    sh = book.sheet_by_index(0)
    print sh.name, sh.nrows, sh.ncols
    print "Cell B2 is", sh.cell_value(rowx=1, colx=1)
    for rx in range(sh.nrows):
        print sh.row(rx)
    return book

def maprow(row):
    '''takes a list of cell objects and returns a list of values in those objects'''
    rowVals = [None for i in range(len(row))]
    for i in range(len(row)):
        rowVals[i] = row[i].value
    return rowVals
    
def excel2array(myfile,sheet=0):
    '''Generator iterating over each row of conversion of specified sheet of an xls or xlsx file'''
    book = xlrd.open_workbook(myfile)
    sh = book.sheet_by_index(sheet)
    #res = [None for i in range(sh.nrows)] #initialize array container
    for rx in range(sh.nrows):
        #row = sh.row(rx)
        #for cx in range(sh.ncols):
        #    res[rx][cx] = row[cx].value #extract value from cell object and insert into array.
        yield maprow(sh.row(rx))
    
def excel2dict(myfile,sheet=0,headerRow=0):
    '''Generator of row-dictionaries based on converting the specified sheet of an xls or xlsx file. By default, the first row is assumed to contain the header'''
    book = xlrd.open_workbook(myfile)
    sh = book.sheet_by_index(sheet)
    header = maprow(sh.row(headerRow)) #typically this is a list of strings representing column names
    for rx in range(headerRow+1,sh.nrows):
        yield dict(zip(header,maprow(sh.row(rx))))
        
if __name__== "__main__":
    #myfile = "fakeQPL.xls"
    myfile = "fakeQPL.xlsx"
    #book = summarize(myfile)
    res1 = list(excel2array(myfile))
    res2 = list(excel2dict(myfile))