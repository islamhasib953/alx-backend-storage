#!/usr/bin/env python3

""" 101-students """


def top_students(mongo_collection):
    """function that returns all students sorted by average score"""
    pipeline = [
        {"$project": {"name": "$name", "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}},
    ]

    result = mongo_collection.aggregate(pipeline)

    return result
