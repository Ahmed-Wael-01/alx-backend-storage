#!/usr/bin/env python3
"""providing stats about nginx logs"""


from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    col = client.logs.nginx
    print(col.count_documents(), 'logs')
    print('Methods:')
    for meth in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print('\tmethod {}: {}'.format(meth, col.count_documents({"method": meth})))
    print('{} status check'.format(col.count_documents(
                                            {"method": "GET",
                                             "path": "/status"})))
