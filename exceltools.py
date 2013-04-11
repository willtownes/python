'''
Handy functions for reading in excel files (XLS or XLSX)
Currently does not support ragged arrays or multiple sheets
By Will Townes
'''
import xlrd

class ExcelSheet(object):
    '''class for working with excel work sheets'''
    def __init__(self,filename,sheet=0,headerRow=0):
        '''creates excel sheet object based on XLS or XLSX file at specified location'''
        self.book = xlrd.open_workbook(filename)
        self.sh = self.book.sheet_by_index(sheet)
        self.sheetID = sheet
        self.header = self._maprow(self.sh.row(headerRow))
        self.headerID = headerRow
        self.array = [self._maprow(self.sh.row(i)) for i in range(headerRow+1,self.sh.nrows)]
        self.dictArray = self.dictArray = [dict(zip(self.header,self._maprow(self.sh.row(i)))) for i in range(headerRow+1,self.sh.nrows)]
        
    def __str__(self):
        return "ExcelSheet Object '%s' has %d rows and %d cols"%(self.sh.name,self.sh.nrows,self.sh.ncols)  
        
    @staticmethod
    def _maprow(row): #private method
        '''takes a list of cell objects and returns a list of values in those objects'''
        rowVals = [None for i in range(len(row))]
        for i in range(len(row)):
            rowVals[i] = row[i].value
        return tuple(rowVals) #don't allow column sorting
        
    def getSheet(self):
        '''returns the index of the current sheet in focus'''
        return self.sheetID
    
    def getHeader(self):
        '''returns the column headers'''
        return self.header
        
    def getArray(self):
        '''List of each row of conversion of specified sheet of an xls or xlsx file'''
        return self.array
        
    def getDictArray(self):
        '''List of row-dictionaries based on converting the specified sheet of an xls or xlsx file. By default, the first row is assumed to contain the header'''
        return self.dictArray
    
    def getDimension(self):
        '''returns a tuple showing the number of rows below the header and the number of columns in the sheet'''
        return (len(self.array),len(self.header))
    
    def summarize(self):
        '''practice function based on the library's documentation'''
        print "The number of worksheets is: ", self.book.nsheets
        print "Worksheet name(s):", self.book.sheet_names()
        print self.sh.name, self.sh.nrows, self.sh.ncols
        print "Cell B2 is", sh.cell_value(rowx=1, colx=1)
        for rx in range(sh.nrows):
            print sh.row(rx)
  
    def sort(self,indexColumn=0,descending=False):
        '''sorts all of the internal representations of the sheet based on the indexColumn'''
        self.array.sort(key=lambda x: x[indexColumn],reverse=descending)
        self.dictArray.sort(key=lambda x: x[self.header[indexColumn]], reverse=descending)
    
    def isDimEqual(self,that):
        '''compare the dimensions against another ExcelSheet object'''
        return self.getDimension()==that.getDimension()
        
    def compareArray(self,that):
        '''compare to another ExcelSheet object of same dimension and same sort by checking each entry in the corresponding arrays.
        The return value is an empty list for a perfect match. Otherwise, it is a list of tuples:
        (row,column,self.value,that.value)'''
        assert(self.isDimEqual(that))
        badCells = []
        other = that.getArray()
        nrow,ncol = self.getDimension()
        for i in range(nrow):
            for j in range(ncol):
                if self.array[i][j] != other[i][j]: badCells.append((i,j,self.array[i][j],other[i][j]))
        return badCells
        
        
if __name__== "__main__":
    t1 = ExcelSheet("test1.xls")
    t2 = ExcelSheet("test2.xlsx")
    t1.sort()
    t2.sort()
    badCells = t1.compareArray(t2)