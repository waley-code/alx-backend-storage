#!/usr/bin/env python3
"""10 update topics in school"""


def update_topics(mongo_collection, name, topics):
    """Update the topics of the school document
        based on the name
    """
    result = mongo_collection.update_many({"name": name},
            {"$set": {"topics": topics}})

    # Return the number of documents matched and modified
    return result.modified_count

