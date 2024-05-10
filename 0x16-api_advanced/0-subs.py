#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the No. of subers for a given subreddit

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: No. of subers subreddit. Returns 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
