import configparser
from github3 import login


def repositories():
    config = configparser.ConfigParser()
    config.read('credentials.ini')
    github = login(config['GITHUB']['USERNAME'], password=config['GITHUB']['PASSWORD'])
    repos = github.iter_user_repos(config['GITHUB']['USERNAME'])
    return repos