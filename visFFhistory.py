'''This program visualizes and/or selectively deletes the data from Firefox browser history'''
import sqlite3, os, csv

if os.name.lower() == 'nt': #windows case
    desktop = os.environ['USERPROFILE']+'\\Desktop'+'\\'
    #path = desktop #testing purposes only.
    path = os.environ['USERPROFILE']+r'\Application Data\Mozilla\Firefox\Profiles\j21f0cv4.default'+'\\'
else: #mac or unix case
    desktop = os.environ['HOME']+'/desktop/'
    path = desktop #testing purposes only. Provide the real path later.

def history2csv():
    '''exports the firefox browser history to a csv file stored on the desktop'''
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
    f = open(desktop+'FF_history.csv','wb')
    writer = csv.writer(f)
    writer.writerows(info)
    f.close()

def clearhistory(*args):
    '''removes all records from the history corresponding to the keyword arguments provided.'''
    conn = sqlite3.connect(path+'places.sqlite')
    c = conn.cursor()
    for arg in args:
        t = ('%'+arg+'%',)
        #delete all records from the history visits table
        c.execute("delete from moz_historyvisits where place_id in (select id from moz_places where url like ?);", t)
        assert c.execute("select count(*) from moz_historyvisits where place_id in (select id from moz_places where url like ?);", t).fetchall()[0][0] == 0
        #delete all input history
        c.execute("delete from moz_inputhistory where place_id in (select id from moz_places where url like ?);", t)
        #delete all records of typing a particular url
        c.execute("delete from moz_inputhistory where input like ?;", t)
        #delete all records from the places table (the main one that the others reference via foreign keys).        
        c.execute("delete from moz_places where url like ? and id not in ((select fk from moz_bookmarks) or (select place_id from moz_annos));", t)
        assert c.execute("select count(*) from moz_places where url like ? and id not in ((select fk from moz_bookmarks) or (select place_id from moz_annos));", t).fetchall()[0][0] == 0
    conn.commit()
    c.close()
    conn.close()

if __name__ == "__main__":
    keywords = raw_input("Type the keywords, separated by commas, for records to be removed from the firefox browser history.\n").split(',')
    clearhistory(*keywords)

