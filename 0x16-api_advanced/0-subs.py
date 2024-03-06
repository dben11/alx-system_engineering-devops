#!/usr/bin/python3
"""
Number of subscribers for a given subreddit
"""

from requests import get

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    # Provide a more relevant user-agent for your script
    user_agent = {'User-agent': 'MyRedditScript'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    try:
        response = get(url, headers=user_agent)
        response.raise_for_status()  # Raise HTTPError for bad responses

        results = response.json()
        return results.get('data').get('subscribers')

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0

# Example usage:
subreddit_name = 'python'
subscribers_count = number_of_subscribers(subreddit_name)
print(f"Subscribers for r/{subreddit_name}: {subscribers_count}")

