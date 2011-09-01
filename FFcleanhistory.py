'''This removes all records of visits to
youtube, okcupid, facebook, twitter,
hulu, and amazon from Firefox browser history'''

import sqlite3, os
path = r'C:\Documents and Settings\townesw\Application Data\Mozilla\Firefox\Profiles\bpb5z2gu.default\\'
conn = sqlite3.connect(path+'places.sqlite')
c = conn.cursor()
#tables = c.execute("select * from SQLITE_MASTER")
#relevant tables are moz_places and moz_historyvisits



c.close()
