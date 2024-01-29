#!/usr/bin/python3
"""
Implements a script to export data in the JSON format.
"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    r = requests.get(url)
    users = r.json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
