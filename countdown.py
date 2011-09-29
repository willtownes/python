'''
Runs a countdown timer for 2 minutes, then makes a beep.
Will Townes
Sept. 2011
'''

import time, winsound
minutes = input('Enter number of minutes')
seconds = input('Enter number of seconds')
raw_input('Press enter to start timer...')
total = 60.0*minutes+seconds
while total > 0:
    print(str(total)+' seconds remaining')
    time.sleep(1)
    total -= 1
winsound.Beep(180,500) #beep at typical human voice freq for .5 sec
#the beep is not working! Need to figure out why... 
    
