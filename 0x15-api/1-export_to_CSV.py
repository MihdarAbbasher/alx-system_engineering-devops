#!/usr/bin/python3
"""Accessing a REST API for employees todo lists"""

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
    doneTasks = []
    with open('{}.csv'.format(employeeId), 'w') as myfile:
        for task in allTasks:
            line = '"{},"{}","{}","{}"\n'.format(employeeId, userName,
                    task.get('completed'), task.get('title'))
            myfile.write(line)
