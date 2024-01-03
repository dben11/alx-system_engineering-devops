#!/usr/bin/python3
'''
Given an employee ID, returns information about his/her
TODO list progress
'''

import requests
from sys import argv

# Code should not be executed when imported
if __name__ == "__main__":
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
nameOf_emp = response.get('name')

# user todo response
todoResp = requests.get(todo_uri).json()

# Total number of task
TotalNum_task = len(todoResp)

# Total number of uncompleted task
uncompleted_task = sum([elem['completed'] is False for elem in todoResp])

# Number of completed task
completed_task = TotalNum_task - uncompleted_task

# Format the expected output
output = "Employee {} is done with tasks({}/{}):"
print(output.format(nameOf_emp, completed_task, TotalNum_task))

# Printing the completed tasks
for elem in todoResp:
    if elem.get("completed") is True:
        print("\t", elem.get("title"))
