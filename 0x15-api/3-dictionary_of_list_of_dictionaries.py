#!/usr/bin/python3
"""
Implements a script to export data in the JSON format.
"""
import json
import requests

if __name__ == "__main__":
    json_file = 'todo_all_employees.json'
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"
    try:
        users_response = requests.get(users_url)
        users_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error", e)
        exit(1)

    users = users_response.json()
    all_todos = {}

    for user in users:
        todo_url = f"{base_url}/todos?userId={user.get('id')}"
        try:
            todos_response = requests.get(todo_url)
            todos_response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print("Error", e)
            exit(1)

        todos = todos_response.json()
        todo_list = []

        for todo in todos:
            todo_list.append({
                "username": user.get('name'),
                "task": todo.get('title'),
                "completed": todo.get('completed')
            })

        all_todos[str(user.get('id'))] = todo_list

    with open(json_file, 'w') as f:
        json.dump(all_todos, f)
