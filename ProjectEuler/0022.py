'''
Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.
What is the total of all the name scores in the file?
'''

def namescore(text,uppercase=True):
    '''returns the sum of all the ordinal value equivalents to the letters in text, ignoring double quotes.
    for example, A gets the value of 1, and "abc" has value 1+2+3 = 6.'''
    text = text.strip('"') #strip out quotation marks.
    #if not uppercase:
    #    text = text.upper()
    baseline = ord('A')-1
    return sum([ord(s)-baseline for s in text])

if __name__ == "__main__":
    #test code
    print("COLIN should have namescore of 53, we found him to have %d"%namescore('COLIN'))
    names = sorted(open('names.txt').read().split(','))
    print("COLIN should be in the position 938, we found him to be in position %d"%(names.index('"COLIN"')+1)) 
    total = 0
    for i in xrange(len(names)):
        total += (i+1)*namescore(names[i])
    print("Total of all names scores in file was: %d"%total)
    
