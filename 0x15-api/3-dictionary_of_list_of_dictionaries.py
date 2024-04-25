import json
import requests
import sys

def export_to_json(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{base_url}/todos?userId={employee_id}'

    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetch user's tasks
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Organize tasks by user ID
    tasks_by_user = {}
    for task in todo_data:
        task_dict = {
            "username": user_data['username'],
            "task": task['title'],
            "completed": task['completed']
        }
        user_id = user_data['id']
        if user_id not in tasks_by_user:
            tasks_by_user[user_id] = []
        tasks_by_user[user_id].append(task_dict)

    # Write to JSON file
    with open(f'{employee_id}.json', 'w') as json_file:
        json.dump(tasks_by_user, json_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    export_to_json(employee_id)
