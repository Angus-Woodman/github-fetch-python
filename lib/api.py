import requests
from repos import Repos

def fetch_repos(username):

    URL = f'https://api.github.com/users/{username}/repos'

    ''' Call to API of Github '''
    req = requests.get(URL)
    for data in req.json():
        Repos(data)

        # repo = Repos(data)
        # print(repo.get_details())

# fetch_repos()
