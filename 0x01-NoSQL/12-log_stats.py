"""
parse nginx log files in a mogodb database
"""
from pymongo import MongoClient


if __name__ == "__main":
    client = MongoClient("'mongodb://127.0.0.1:27017'")
    nginx_collection = client.logs.nginx
    print('{} logs'.format(nginx_collection.count()))
    print('Methods:')
    print('\tmethod GET: {}'
          .format(nginx_collection.count({'method': "GET"})))
    print('\tmethod POST: {}'
          .format(nginx_collection.count({'method': "POST"})))
    print('\tmethod PUT: {}'
          .format(nginx_collection.count({'method': "PUT"})))
    print('\tmethod PATCH: {}'
          .format(nginx_collection.count({'method': "PATCH"})))
    print('\tmethod DELETE: {}'
          .format(nginx_collection.count({'method': "DELETE"})))
    print('{} status check'
          .format(nginx_collection.count({'method': "GET",
                                          'path': "/status"})))
