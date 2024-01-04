#!/usr/bin/python3
"""
Given an employee ID, return information
about his/her TODO list progress
"""

import requests
from sys import argv

if __name__ == "__main__":
    try:
        empId = int(argv[1])
    except ValueError:
        exit()

    # Dummy variables fro REST API
    api_url = "https://jsonplaceholder.typicode.com"
    user_uri = "{}/users/{}".format(api_url, empId)
    todo_uri = "{}/todos".format(user_uri)

    # User Response
    response = requests.get(user_uri).json()

    # Name of employee
    empName = response.get("name")

    # User TODO response
    response = requests.get(todo_uri).json()

    # Total number of tasks: sum of completed and non-completed task
    totalNumOfTask = len(response)

    # Number of non-completed tasks
    nonCompletedTask = sum([elem["completed"] is False for elem in response])

    # Number of completed tasks
    completedTask = totalNumOfTask - nonCompletedTask

    # Formating the expected output
    str = "Employee {} is done with tasks({}/{}):"
    print(str.format(empName, completedTask, totalNumOfTask))

    # Printing completed tasks
    for elem in response:
        if elem.get("completed") is True:
            print("\t", elem.get("title"))
