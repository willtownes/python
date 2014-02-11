#!/usr/bin/env python
'''
This is a script to print out a traceback to a file for later inspection. Inspired by: http://linux.byexamples.com/archives/365/python-convey-the-exception-traceback-into-log-file/
'''
import xlrd,traceback,sys
def main():
	#book = xlrd.open_workbook('Products_Export_Non_Lighting.xls')
    #book = xlrd.open_workbook('Products_Export_Lighting.xls')
    book = xlrd.open_workbook('excel_file.xls')

if __name__=="__main__":
	try:
		main()
	except:
		print("Exception Encountered")
		traceback.print_exc(file=open("xlrd_err.txt","w"))
		sys.exit(1)
