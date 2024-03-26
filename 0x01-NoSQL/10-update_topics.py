#!/usr/bin/env python3
"""
update a document in a collection
"""


def update_topics(mongo_collection, name, topics):
    """
    update a document in a collection
    """
    filter = {'name': name}
    new_values = {"$set": {'topics': topics}}

    mongo_collection.update_one(filter, new_values)
