'''This program visualizes the data from Firefox browser history'''
import sqlite3, os, csv

if os.name.lower() == 'nt': #windows case
	path = os.environ['USERPROFILE']+r'\Application Data\Mozilla\Firefox\Profiles\bpb5z2gu.default\\'
else: #mac or unix case
	path = os.environ['HOME']+'/desktop/'

conn = sqlite3.connect(path+'places.sqlite')
c = conn.cursor()
#tables = c.execute("select * from SQLITE_MASTER") #master list of all tables in db
#relevant tables are moz_places and moz_historyvisits
#the following query was copied from a mozilla forensics wiki
info = c.execute('''
SELECT datetime(moz_historyvisits.visit_date/1000000,'unixepoch'), moz_places.url
FROM moz_places, moz_historyvisits 
WHERE moz_places.id = moz_historyvisits.place_id''').fetchall()
c.close()
conn.close()
f = open(path+'FF_history.csv','wb')
writer = csv.writer(f)
writer.writerows(info)
f.close()

