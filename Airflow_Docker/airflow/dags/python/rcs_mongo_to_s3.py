"""
    writing json file to s3 on memory 
    writing file to dist and the upload is timeconsuming
"""

from pymongo import MongoClient
from datetime import timedelta, datetime, date
from bson.json_util import dumps, RELAXED_JSON_OPTIONS
import boto3
import sys

execution_date = sys.argv[1]

def getDates(dateDiff = 1, format = '%Y-%m-%d'):
  print("execution_date: ", execution_date)  
  date = datetime.strftime(datetime.strptime(execution_date[:10], '%Y-%m-%d') - timedelta(dateDiff), format)
  return date

date = getDates(0)
print("current date: ", date)

host = ''
username = ''
password = ''
auth_db = ''
database = ''
collection = ''

mongo_client = MongoClient(host,
         username=username,
         password=password,
         authSource=auth_db)

# now connect to the database where your collection resides
mongo_db = mongo_client[database]

# finally, choose the collection we want to query documents from
mongo_collection = mongo_db[collection]

mongo_query = {'date': date}
file_name = date

print("writing to file: {0} with query{1}".format(file_name, mongo_query))

# partition based on month
result_docs = mongo_collection.find(mongo_query,  batch_size=1000)

x=[]
for i in result_docs:
    x.append(i)

# raise exception so that the job is failed till no data is available.
if(len(x) == 0):
    raise Exception('0 records found in mongo for query: {0}'.format(mongo_query))

# aws access keys
access_key = ''
secret_key = ''
region = ''

client = boto3.client(
    's3',
    region_name=region,
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
)

print("writing {0} to s3".format(len(x)))

x = dumps(x, json_options=RELAXED_JSON_OPTIONS).encode('UTF-8')

# write data to s3
try:
    responce = client.put_object(Bucket='rcsmongodata',Key=file_name.replace('-', '')+'.json',Body=(bytes(x)))
except Exception as e:
    print("error: ", e.args)

print('responce: ', responce)
print('Info: job end')