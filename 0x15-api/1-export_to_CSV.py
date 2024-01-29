#!/usr/bin/python3
"""
Implements a script to export data in the CSV format.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
    todo_url = f"{base_url}/todos?userId={user_id}"
    user_url = f"{base_url}/users/{user_id}"
    todos_response = requests.get(todo_url)
    users_response = requests.get(user_url)

    csv_file = f'{user_id}.csv'
    name = users_response.json().get('name')
    todos = todos_response.json()

    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow(
                [user_id, name, todo.get('completed'), todo.get('title')]
            )
