#!/usr/bin/python3
"""Accessing a REST API for employees todo lists"""

import json
import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/" + employeeId
    response = requests.get(url)
    userName = response.json().get('username')
    url += "/todos"
    response = requests.get(url)
    allTasks = response.json()
    done = 0
    mydic = {employeeId: []}
    for task in allTasks:
        mydic[employeeId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": userName
        })
    with open('{}.json'.format(employeeId), 'w') as myfile:
        json.dump(mydic, myfile)
