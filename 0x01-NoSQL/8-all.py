#!/usr/bin/env python3
"""
list all documents in a collection
"""


def list_all(mongo_collection):
    """
    list all documents in a collection
    """
    all_doc = []
    for doc in mongo_collection.find():
        all_doc.append(doc)
    return all_doc
