#this is a program to convert a decimal longitude value into degrees minutes seconds format

def long2dms(ilong):

#this conditional defines whether the long. is East or West
    if ilong>=0:
        direction = 'East'
    else:
        direction = 'West'

    ilong = abs(ilong)
    
#here we parse the initial, decimal value into degrees minutes and seconds.
    degrees = int(ilong)
    rawminutes = 60*(ilong-degrees)
    minutes = int(rawminutes)
    seconds = int(60*(rawminutes-minutes))

    if ilong >180:
        print "ERROR- invalid longitude value. Please enter a value between -180 and 180."
    else:
        print "(degrees, minutes, seconds, direction)"
        return degrees, minutes, seconds, direction
