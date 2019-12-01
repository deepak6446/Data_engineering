# sending email using aws ses (simple email service)

import boto3
import json
from datetime import datetime, timedelta

access_key = ''  # aws access key
secret_key = ''  # aws secret key
region = ''  # region
log_base_path = '/logs/'

client = boto3.client(
    'ses',
    region_name=region,
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
)


def getDates(dateDiff=1, format='%Y%m%d'):
    date = datetime.strftime(datetime.now() - timedelta(dateDiff), format)
    return date


def getTableHead(columns):
    ret = '<tr>'
    for i in range(0, len(columns)):
        if(columns[i] == 'processing_time'):
            columns[i] = 'processing_time_min'
        ret = ret + '<th>{0}</th>'.format(columns[i])
    return ret + '</tr>'


def getTableData(columns):
    ret = '\n <tr>'
    for i in range(0, len(columns)):
        ret = ret + '\n <td>{0}</td>'.format(columns[i])
    return ret + '\n </tr>'


report_date = getDates(1, '%Y%m%d')
logFile = log_base_path + report_date + "log.json"

with open(logFile, "r") as f:
    data = json.load(f)

style = '''
  <style>
  table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
  }
  </style>
'''

startTable = '\n <table style="width:100%">'
endTable = '\n</table>'

x = ['table']
x.extend(columns)
body = style + startTable + getTableHead(x)

tables_required = ['table1', 'tabe2']
columns = ['col1', 'col2']

for da in tables_required:
    cols = []
    for col in columns:
        try:
            cols.append("{:,}".format(data[da][col]))
        except:
            cols.append('---')
    cols.insert(0, da)
    body = body + getTableData(cols)

body = body + endTable
body = '''
<html>
<body>
''' + body + '''
</body>
</html>
'''

#   for text data in body
# 'Text': {
#     'Charset': 'UTF-8',
#     'Data': body,
# }

response = client.send_email(
    Destination={
        'ToAddresses': ['deepak.r.poojari@@gmail.com'],
    },
    Message={
        'Body': {
            'Html': {
                'Charset': 'UTF-8',
                'Data': body,
            }
        },
        'Subject': {
            'Charset': 'UTF-8',
            'Data': 'Automated Status Report For DataLake Date: ' + report_date,
        },
    },
    Source='deepak.r.poojari@gmail.com',
)

print(response)