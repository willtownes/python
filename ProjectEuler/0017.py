'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
342 = three hundred and forty two
'''
ones = ['one','two','three','four','five','six','seven','eight','nine']
teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

def lcount(stringlist):
    '''returns the number of letters in a list of strings'''
    return len(reduce(lambda x,y: x+y,stringlist)) #the lambda function here is string addition not numeric addition

#the "ones" letters are used 9 times for each range of 100 (10 such ranges total), a total of 90 times each.
#also, the letters are each used 100 times each above the 99 mark.
counter = 190*lcount(ones)
counter += 10*lcount(teens) #the words in teens are used 10 times each
counter += 100*lcount(tens) #each of the 'tens' is used 100 times (10 times per 100 range)
counter += 900*len('hundred') #number of times the word 'hundred' is used
counter += 891*len('and') #'and' is used everywhere 'hundred' is used, except for exactly on the 100,200,300, etc marks.
counter += len('onethousand')
print(counter)

    

