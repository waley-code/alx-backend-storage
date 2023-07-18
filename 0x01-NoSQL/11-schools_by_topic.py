#!/usr/bin/env python3
""" returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic: str) -> list:
    """Retrieve the schools with the specified topic"""
    schools = mongo_collection.find({"topics": topic})

    # Return the list of schools
    return list(schools)

