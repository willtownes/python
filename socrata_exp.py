'''experimenting with the socrata API'''
#useful info at:
# http://dev.socrata.com/getting-started/
# http://opendata.socrata.com/api/docs/
# https://github.com/socrata/socrata-python/blob/master/Socrata.py
# http://docs.python.org/library/configparser.html
import ConfigParser
config = ConfigParser.RawConfigParser()
config.add_section('credentials')
#no credential values actually needed for read-only access
config.set('credentials','user','')
config.set('credentials','password','')
config.set('credentials','app_token','')
config.add_section('server')
config.set('server','host','http://explore.data.gov')

import Socrata
#interface to the server, can get any dataset from its methods.
d = Socrata.Dataset(config) 
#list of datasets with certain attributes
v = d.find_datasets({'limit':'1','tags':'congress'}) 
report_id = v['results'][0]['view']['id']
print('Report ID is : '+report_id)
isvalid = d.is_id(report_id)
print('Is report ID valid? '+str(isvalid))
d.use_existing(report_id) #sets the d.id attribute to "report_id"
metadata = d.metadata()
print('Here is the report metadata:')
print(metadata)

#another example URL:
#url = 'https://explore.data.gov/views/6qji-a8pa.xml'

#I should write my own methods for fetching the actual datasets.
#Current methods only provide for updating the data and fetching metadata
#example would be a method to save x number of rows from a specified dataset to a CSV on desktop


