#!/usr/bin/env python3
"""list schools with a specific topics"""


def schools_by_topic(mongo_collection, topic):
    """return list of schools with specific topics"""
    return list(mongo_collection.find({"topics": topic}))
