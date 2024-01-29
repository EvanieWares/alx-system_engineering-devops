#!/usr/bin/python3
"""
Implements a script to export data in the JSON format.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: 0-gather_data_from_an_API.py <employee ID>")
        exit(1)
    try:
        employee_id = int(sys.argv[1])
    except ValueError as e:
        print('Error:', e)
        exit(1)

    base_url = "https://jsonplaceholder.typicode.com"
    todo_url = f"{base_url}/todos?userId={employee_id}"
    user_url = f"{base_url}/users/{employee_id}"
    try:
        todos_response = requests.get(todo_url)
        users_response = requests.get(user_url)
        todos_response.raise_for_status()
        users_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error", e)
        exit(1)

    name = users_response.json().get('name')
    todos = todos_response.json()
    todo_list = []

    for todo in todos:
        todo_list.append({
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": name
        })
    print({str(employee_id): todo_list})
