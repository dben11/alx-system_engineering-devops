#!/usr/bin/python3
"""
Queries the Reddit API abd return the number of subscribers
(not active users, total subscribers) for a given subreddit.

If not a valid subriddit, return 0
"""

import requests
import sys


def number_of_subscribers(subreddit):
    """Return the total number of subscribers
    for a given subreddit
    """
    # Set the Default URL strings
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Set an User-Agent
    user_agent = {"User-Agent": "python/requests"}

    # Get the Response of the Reddit API
    res = requests.get(url, headers=user_agent, allow_redirects=False)
        
    # Checks if the subreddit is invalid
    if res.status_code in [302, 404]:
        return 0
        
    # Return total subscribers of the subreddit
    results = res.json().get("data")
    return results.get("subscribers")
