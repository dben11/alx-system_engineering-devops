#!/usr/bin/python3
"""
A python script that uses a REST API
Given an employee ID,
Returns information about his/her TODO list progress.
"""

import requests
from sys import argv

# Code should not be executed when imported
if __name__ == '__main__':
    try:
        empId = int(argv[1])
    except ValueError:
        exit()

# Creating a rest api
api_url = 'https://jsonplaceholder.typicode.com'
user_uri = '{}/users/{}'.format(api_url, empId)
todo_uri = '{}/todos'.format(user_uri)

# User response
response = requests.get(user_uri).json()

# Name of employee
nameOfEmp = response.get('name')

# user todo response
response = requests.get(todo_uri).json()

# Total number of task
totalNumTask = len(response)

# Total number of uncompleted task
uncompletedTask = sum([elem['completed'] is False for elem in response])

# Number of completed task
completedTask = totalNumTask - uncompletedTask

# Format the expected output
output = "Employee {} is done with tasks({}/{}):"
print(output.format(nameOfEmp, completedTask, totalNumTask))

# Printing the completed tasks
for elem in response:
    if elem.get("completed") is True:
        print("\t", elem.get("title"))
