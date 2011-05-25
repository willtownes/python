print 'this program will convert a temperature from fahrenheit to celsius or vice versa'
iscale = raw_input('Is your original temperature in fahrenheit(F) or celsius(C)? Type F or C ').upper()
initialtemp = input('Enter your original temperature in degrees ' + iscale + ': ')
F = (9.0/5.0)*initialtemp + 32
C = (5.0/9.0)* (initialtemp - 32)
if iscale == 'C':
    finaltemp = F
    fscale = 'F'
elif iscale == 'F':
    finaltemp = C
    fscale = 'C'
else:
    print('error, try again')
print('your temperature is ', finaltemp, 'degrees ', fscale)
