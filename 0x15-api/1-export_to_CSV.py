#!/usr/bin/python3
"""
Export data in the CSV format
"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    # Check if the ID is an integer
    try:
        empId = int(argv[1])
    except ValueError:
        exit()

    # Dummy variables from REST API
    api_url = "https://jsonplaceholder.typicode.com"
    user_uri = "{}/users/{}".format(api_url, empId)
    todo_uri = "{}/todos".format(user_uri)
    filename = "{}.csv".format(empId)

    # User Response
    response = requests.get(user_uri).json()

    # username of employee
    username = response.get("username")

    # User TODO response
    response = requests.get(todo_uri).json()

    # Create the new filw for the save the information
    # Filename example: {user_id}.csv
    with open(filename, 'w', encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_ALL)

        for elem in response:
            # Completed or noncompleted task
            status = elem.get("completed")

            # The task name
            title = elem.get("title")

            # write each result of API response in a row of a CSV file
            writer.writerow([empId, username, status, title])
