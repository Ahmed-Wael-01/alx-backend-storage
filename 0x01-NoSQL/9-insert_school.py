#!/usr/bin/env python3
"""insert with kwargs"""


def insert_school(mongo_collection, **kwargs):
    """insert a doc"""
    return mongo_collection.insert(kwargs)
