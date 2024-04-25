#!/usr/bin/python3
"""
Script to retrieve TODO list progress for a given employee ID from a REST API and export data in CSV format.
"""

import sys
import requests
import csv

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 export_to_CSV.py <employee_id>")
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
    employee_name = user_data.get("username")

    # Prepare data for CSV
    csv_data = []
    for task in todos_data:
        task_completed_status = "True" if task.get("completed") else "False"
        task_title = task.get("title")
        csv_data.append([employee_id, employee_name, task_completed_status, task_title])

    # Write data to CSV file
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        csv_writer.writerows(csv_data)

    print(f"Data exported to {csv_filename} successfully.")
