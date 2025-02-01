#!/usr/bin/env python3
"""change topics of a school"""


def update_topics(mongo_collection, name, topics):
    """change topics of school"""
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
