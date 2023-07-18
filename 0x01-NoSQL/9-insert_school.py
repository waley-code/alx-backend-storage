#!/usr/bin/env python3
""" 9-main inserting a school"""


def insert_school(mongo_collection, **kwargs):
    """Insert the document into the collection
        and return the new _id
    """
    return mongo_collection.insert_one(kwargs).inserted_id

