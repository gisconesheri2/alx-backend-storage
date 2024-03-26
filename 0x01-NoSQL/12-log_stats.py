"""
parse nginx log files in a mogodb database
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    print('\tmethod GET: {}'
          .format(nginx_collection.count_documents({'method': "GET"})))
    print('\tmethod POST: {}'
          .format(nginx_collection.count_documents({'method': "POST"})))
    print('\tmethod PUT: {}'
          .format(nginx_collection.count_documents({'method': "PUT"})))
    print('\tmethod PATCH: {}'
          .format(nginx_collection.count_documents({'method': "PATCH"})))
    print('\tmethod DELETE: {}'
          .format(nginx_collection.count_documents({'method': "DELETE"})))
    print('{} status check'
          .format(nginx_collection.count_documents({'method': "GET",
                                          'path': "/status"})))
