#!/usr/bin/env python3
"""lists all docs"""

def list_all(mongo_collection):
    """return all docs"""
    docs = mongo_collection.find()
    if len(docs) == 0:
        return []
    return docs
