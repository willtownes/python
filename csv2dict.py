import csv

def csv2dictlist(csvfile):
    '''reads in csv file and converts it into a list of dictionaries
    (one dictionary per row).
    Keys to the dictionary are column names.
    Warning- this function does not preserve the order of the column names!
    '''
    reader = csv.DictReader(open(csvfile,'rb'))
    info = [i for i in reader]
    return info

def dictlist2csv(list_of_dictionaries,csvfile):
    '''takes a list of dictionaries and writes it out to a csv file (provide full path name).
    Each dictionary in the list must have the same keys, or an exception will be thrown.
    Also, it does not preserve the order of the column names!'''
    dl = list_of_dictionaries
    cols = dl[0].keys() #assuming the first item has the authoritative list of columns
    writer = csv.DictWriter(open(csvfile,'wb'),cols,extrasaction='raise')
    writer.writerow(dict((h,h) for h in cols)) #write header row.
    for i in dl:
        assert set(i.keys()) == set(cols) #check to make sure each row has the same columns. Otherwise, throw exception.
        writer.writerow(i)
    #note this function doesn't return anything, because no objects were modified.


