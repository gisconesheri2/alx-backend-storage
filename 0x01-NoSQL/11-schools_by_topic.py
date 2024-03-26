#!/usr/bin/env python3
"""
filter documents in a collection using values
in an array
"""


def schools_by_topic(mongo_collection, topic):
    """
    filter documents in a collection using values
    in an array
    """
    school_teach_python = []
    schools = mongo_collection.find({'topics': topic})
    for sch in schools:
        school_teach_python.append(sch)
    return school_teach_python
