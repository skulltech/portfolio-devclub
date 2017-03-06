import os
from github3 import login

def repositories():
    github_username = os.environ.get('GITHUB_USERNAME', None)
    github_password = os.environ.get('GITHUB_PASSWORD', None)
    github = login(username=github_username, password=github_password)
    repos = github.iter_user_repos(github_username)
    return repos