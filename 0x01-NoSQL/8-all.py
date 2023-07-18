#!/usr/bin/env python3
"""8 -all document"""


def list_all(mongo_collection):
    """ lists all documents in a collection"""

    documents = []

    # Check if the collection is empty
    if mongo_collection.count_documents({}) == 0:
        return documents

    # Retrieve all documents in the collection
    cursor = mongo_collection.find({})

    # Iterate over the cursor and append each document to the list
    for document in cursor:
        documents.append(document)

    return documents
