#!/usr/bin/python3
"""
Script to retrieve TODO list progress for a given employee ID from a REST API and export data in JSON format.
"""

import sys
import requests
import json

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch data from the API
    base_url = "https://jsonplaceholder.typicode.com"
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Failed to fetch data from the API.")
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    # Extract relevant information
    employee_username = user_data.get("username")

    # Prepare data for JSON
    json_data = {
        str(employee_id): [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_username
            }
            for task in todos_data
        ]
    }

    # Write data to JSON file
    json_filename = f"{employee_id}.json"
    with open(json_filename, "w") as json_file:
        json.dump(json_data, json_file, indent=4)

    print(f"Data exported to {json_filename} successfully.")
