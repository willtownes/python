#STILL HAS UNRESOLVED BUGS#


print "This program will calculate the residual of a data value, if you provide the mean"
#zero out all variables#
mean = 0
value = 0
residual = 0
#use conditional to catch invalid data types#
while type(mean) == ('int' or 'float') and type(value) == ('int' or 'float'):
    mean = input("What is the mean?")
    value = input("What is the value?")
    residual = value - mean
else:
    print 'error- invalid data type. Please input an integer or float.'
