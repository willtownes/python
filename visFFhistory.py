'''This program visualizes the data from Firefox browser history'''
import sqlite3, os
path = os.environ['USERPROFILE']+r'\Application Data\Mozilla\Firefox\Profiles\bpb5z2gu.default\\'
conn = sqlite3.connect(path+'places.sqlite')
c = conn.cursor()
#tables = c.execute("select * from SQLITE_MASTER")
#relevant tables are moz_places and moz_historyvisits

c.close()
