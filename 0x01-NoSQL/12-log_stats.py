#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB
"""


if __name__ == "__main__":
    """
    12-log_stats
    """
    from pymongo import MongoClient

    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx

    print(f"{nginx_collection.count_documents({})} logs")
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    filter_path = {"method": "GET", "path": "/status"}
    print(f"{nginx_collection.count_documents(filter_path)} status check")
