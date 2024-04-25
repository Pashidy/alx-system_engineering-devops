#!/usr/bin/python3
"""
Script to retrieve TODO list progress for a given employee ID from a REST API.
"""

import sys
import requests

if __name__ == "__main__":
    
    url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()

    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    [print("\t {}".format(complete)) for complete in completed]


0x15-api/1-export_to_CSV.py
