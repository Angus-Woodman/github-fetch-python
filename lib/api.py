import requests
from repos import Repos


username = input("Enter your Github username:")

URL = f'https://api.github.com/users/{username}/repos'

def fetch_repos():
    ''' Call to API of Github '''
    req = requests.get(URL)
    for data in req.json():
        x = Repos(data)
        print(x.get_name())

fetch_repos()
