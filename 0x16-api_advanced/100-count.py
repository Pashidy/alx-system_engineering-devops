#!/usr/bin/python3

import requests


def count_words(subreddit, word_list, word_count=None, after=None):
    """
    Recursively queries the Reddit API, parses the title of articles & prints
    a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count occurrences of.
        word_count (dict, optional): A dictionary to store the keywrd
                                     Default is None.
        after (str, optional): The parameter used for pagination.
                                Default is None.

    Returns:
        None
    """
    if word_count is None:
        word_count = {}

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
            title = post["data"]["title"].lower()  # Convert title to lowercase
            for word in word_list:
                if word.lower() in title:
                    word = word.lower()
                    word_count[word] = word_count.get(word, 0) + 1

        after = data["data"]["after"]
        if after:  # If there's a "after" token, recursively call the function
            count_words(subreddit, word_list, word_count, after)
        else:
            print_results(word_count)
    else:
        return None


def print_results(word_count):
    """
    Prints the sorted count of given keywords in descending order by count
    and ascending order alphabetically for words with the same count.

    Args:
        word_count (dict): A dictionary containing counts of keywords.

    Returns:
        None
    """
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_words:
        print(f"{word}: {count}")
