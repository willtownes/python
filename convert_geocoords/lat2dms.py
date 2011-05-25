#this is a program to convert a decimal latitude value into degrees minutes seconds format
#by Will Townes 25 AUG. 2009
#http://willtownes.wordpress.com

def lat2dms(ilat):

#this conditional defines whether the lat. is north or south  
    if ilat>=0:
        direction = 'North'
    else:
        direction = 'South'

    ilat = abs(ilat)
    
#here we parse the initial, decimal value into degrees minutes and seconds.
    degrees = int(ilat)
    rawminutes = 60*(ilat-degrees)
    minutes = int(rawminutes)
    seconds = int(60*(rawminutes-minutes))

    if ilat > 90:
        print "ERROR- invalid latitude value. Please enter a value between -90 and 90."
    else:
        print "(degrees, minutes, seconds, direction)"
        return degrees, minutes, seconds, direction
