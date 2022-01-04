from google_trends import daily_trends
from gtrending import fetch_repos

def google_trends():
    """
    returns google trends from package
    """
    result = daily_trends(country='US')
    return result

def github_trends():
    repos = fetch_repos(language="python")
    return repos

