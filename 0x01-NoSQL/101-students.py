#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """


def top_students(mongo_collection):
    """ Returns all students sorted by average score """
    students = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return students