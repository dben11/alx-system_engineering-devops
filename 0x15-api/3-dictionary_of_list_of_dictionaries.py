#!/usr/bin/python3
"""
Export data from an API to JSON format
"""

from json import dumps
import requests


def getTasksFromEmployee(response, employee):
    """
    Get all the tasks of an employee
    """
    # Creates a list to stores all the tasks of the employee
    empTasks = list()

    # Find the tasks that belongs to this employee
    for task in response:
        if task.get("userId") == employee.get("id"):
            taskData = {
                    'username': employee.get("username"),
                    'task': task.get("title"),
                    'completed': task.get("completed")
                    }

            empTasks.append(taskData)

    # Return the list of tasks
    return empTasks


if __name__ == "__main__":

    # Dummy variables from REST API
    api_url = "https://jsonplaceholder.typicode.com"
    users_uri = "{}/users".format(api_url)
    todos_uri = "{}/todos".format(api_url)
    filename = "todo_all_employees.json"

    # Users Response
    users_response = requests.get(users_uri).json()

    # Users TODO response
    todos_response = requests.get(todos_uri).json()

    # Dictionary of all tasks of users
    usersTasks = dict()

    # Stores all the tasks of each employee in the API data
    for user in users_response:
        user_id = user.get("id")

        # A list of all tasks of current employee
        userTasks = getTasksFromEmployee(todos_response, {
            'id': user_id,
            'username': user.get('username')
            })

        # Inserting the list of all tasks of current employee
        # to a dictionary that stores all the employees with their tasks
        usersTasks[user_id] = userTasks

    # Create the new file with all the information
    # Filename example: "todo_all_employees.json"
    with open(filename, 'w', encoding='utf-8') as jsonFile:
        jsonFile.write(dumps(usersTasks))
