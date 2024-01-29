#!/usr/bin/python3
"""Accessing a REST API for employees todo lists"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/" + employeeId
    response = requests.get(url)
    employeeName = response.json().get('name')
    url += "/todos"
    response = requests.get(url)
    allTasks = response.json()
    done = 0
    doneTasks = []
    with open('{}.csv'.format(employeeId), 'w') as myfile:
        for task in allTasks:
            line = '"{},"{}","{}","{}"\n'.format(employeeId, emplyeeName,
                task.get('completed'), task.get('title')
            myfile.write(line)
        if task.get('completed'):
            doneTasks.append(task)
            done += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, done, len(allTasks)))
    for task in doneTasks:
        print("\t {}".format(task.get('title')))
