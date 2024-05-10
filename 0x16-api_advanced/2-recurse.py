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
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        return None
    

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
