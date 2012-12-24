'''
Script to export facebook contacts to a CSV based on the fbconsole tool
'''
import fbconsole as fb
import json,csv

fb.AUTH_SCOPE=['friends_education_history','friends_location','friends_work_history']
fb.authenticate()
friends=fb.fql("select uid,first_name,last_name,locale,affiliations,contact_email,email,current_address, current_location,birthday,friend_count,mutual_friend_count,hometown_location,languages,name,sex, website,education,work from user where uid in (select uid2 from friend where uid1=me())")
#uids=[i['uid'] for i in friends]
with open('fb_friends.json','w') as ofile:
    json.dump(friends,ofile)
fb.logout() #destroy locally stored auth token

names=[(i['first_name'],i['last_name']) for i in friends]
with open('fb_names2012.csv','w') as ofile:
    writer=csv.writer(ofile)
    writer.writerow(('First Name','Last Name'))
    for name in names:
        try: writer.writerow(name)
        except UnicodeEncodeError: print('Name %s %s could not be written to CSV'%name)

