#!/usr/bin/env python3

"""  function that lists all documents in a collection """


def list_all(mongo_collection):
    """retrieve all documents in the collection"""

    documents = mongo_collection.find()
    return list(documents)
