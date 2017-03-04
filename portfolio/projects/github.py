from github3 import GitHub

GITHUB_USERNAME = 'SkullTech'

gh = GitHub()
repos = gh.iter_user_repos(GITHUB_USERNAME)


for repo in repos:
    pass