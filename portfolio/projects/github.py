from github3 import GitHub

GITHUB_USERNAME = 'SkullTech'


def repositories():
    github = GitHub()
    repos = github.iter_user_repos(GITHUB_USERNAME)
    return repos