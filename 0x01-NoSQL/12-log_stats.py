#!/usr/bin/env python3
"""providing stats about nginx logs"""


from pymongo import MongoClient

client = MongoClient()
col = client.logs.nginx
print(col.count(), 'logs')
print('Methods:')
for meth in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
    print('\tmethod {}: {}'.format(meth, col.count({"method": meth})))
print('{} status check'.format(col.count(
                                        {"method": "GET",
                                         "path": "/status"})))
