#!/usr/bin/python3
"""Fetches the latest commits from a GitHub repository"""

import sys
import requests

if __name__ == "__main__":

    # Obtain repository owner and name from command-line arguments
    repository_owner = sys.argv[1]
    repository_name = sys.argv[2]

	# URL to fetch commits from the GitHub API
    url = "https://api.github.com/repos/{}/{}/commits".format(
			repository_owner, repository_name)

    response = requests.get(url)
    commits = response.json()

    for i, commit in enumerate(commits[:10]):
        sha = commit.get("sha")
        author_name = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, author_name))
