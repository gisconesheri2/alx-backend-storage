#!/usr/bin/env python3
"""
parse nginx log files in a mogodb database
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print('\tmethod {}: {}'
              .format(method,
                      nginx_collection.count_documents({'method': method})))

    print('{} status check'
          .format(nginx_collection.count_documents({'method': "GET",
                                                    'path': "/status"})))
    print ('IPs:')

    ips = nginx_collection.aggregate(
        [
            {
                "$group": {
                    "_id": "$ip",
                    "count": { "$sum": 1}
                }
            },
            {
                "$sort": {"count": -1}
            },
            {
                "$limit": 10
            }
        ]
    )
    for ip in ips:
        print('\t{}: {}'.format(
            ip.get('_id'),
            ip.get('count')
        ))
