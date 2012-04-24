'''this script is to generate a CSV showing the directory structure of some folder'''
import os,csv
def contentinventory(root):
    '''writes a csv file to the current working directory containing a list of all files under the specified root directory'''
    writer = csv.writer(open('content_inventory.csv','wb'))
    writer.writerow(['Folder','filename'])
    for root,dirs,files in os.walk(root): #this is a generator which returns one tuple for each folder
        for f in files:
            #print(f)
            if f in ['.DS_Store']: pass #skip system files
            else: writer.writerow([root,f])

def parsenames(csvfile):
    '''reads the csv file (should be an object, not a string) and parses out the year, family, genus, species, file type, and other info'''
    reader = csv.DictReader(csvfile)        
    writer = csv.DictWriter(open('content_inventory2.csv','wb'),reader.fieldnames+['year','family','genus','species','info','file type'])
    writer.writeheader()
    for row in reader:
        (row['year'],row['family']) = (os.path.split(os.path.split(row['Folder'])[0])[1],os.path.split(row['Folder'])[1])
        (name,row['file type']) = os.path.splitext(row['filename'])
        name = name.split(' ')
        row['genus'] = name[0]
        if len(name) < 3:
            row['species'] = row['info'] = ''
        else:
            row['species'] = name[1]
            row['info'] = ' '.join(name[2:])
            writer.writerow(row)

if __name__=="__main__":
    root = '/Users/townesf/Pictures/iphoto_flora_malesia/Originals'
    #contentinventory(root)
    parsenames(csvfile=open('content_inventory.csv','rb'))
