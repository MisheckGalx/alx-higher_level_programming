#!/usr/bin/python3
"""Using the GitHub API to list commits"""

import sys
import requests

if __name__ == "__main__":
    # Repository name and owner name from the command-line
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    # GitHub API URL for fetching commits
    url = f'https://api.github.com/repos/{owner_name}/{repository_name}/commits'

    # Limit the number of commits per page
    params = {'per_page': 10}
    response = requests.get(url, params=params)

    # JSON response into a list of commits
    commits = response.json()
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
