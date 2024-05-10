#!/usr/bin/python3

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API,returns list of the titles of articles
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot articles
        after (str): The parameter used for pagination to fetch the next page

    Returns:
        list or None: A list of the titles of articles for the subreddit,
                      or None if no results found or the subreddit is invalid
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "my_bot"}  # Set a custom User-Agent
    params = {"limit": 100, "after": after}  # Fetch 100 posts per request

    response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
            )

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            hot_list.append(post["data"]["title"])

        after = data["data"]["after"]
        if after:  # If there's a "after" token, recursively call the fxn
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list  # Return the accumulated list
    else:
        return None
