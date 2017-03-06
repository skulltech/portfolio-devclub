from github3 import login
from .credentials import GITHUB_USERNAME, GITHUB_PASSWORD


def repositories():
    github = login(username=GITHUB_USERNAME, password=GITHUB_PASSWORD)
    repos = github.iter_user_repos(GITHUB_USERNAME)
    return repos