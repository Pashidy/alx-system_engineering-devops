#!/usr/bin/python3
"""
Script to retrieve TODO list progress for a given employee ID from a REST API and export data in CSV format.
"""

import sys
import requests
import csv

if __name__ == "__main__":
    # Get the user ID from the command-line arguments provided to the script
    user_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/{}".format(user_id)).json()

    username = user.get("username")

    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]

