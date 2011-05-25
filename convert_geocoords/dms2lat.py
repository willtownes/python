#this is a program to convert latitude in degrees minutes seconds format to decimal degree

def dms2lat(deg,mnt,sec,sign):

#need error condition for when inputs are in the wrong format (eg deg must be integer)

    if sign == 'N' or 'n':
        sign = 1
    elif sign == 'S' or 's':
        sign = -1
    else:
        print("error, not a valid sign or direction for latitude. Please reenter as N/S")

#need to figure out how to make this error end the program
#also need error conditions for invalid deg, min,sec values (eg min>60)

    mnt = mnt + sec/60
    degrees = sign * (deg + mnt/60)

    return degrees
    
