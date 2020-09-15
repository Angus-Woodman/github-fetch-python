from api import fetch_repos
from repos import Repos

username = input("Enter your Github username: ")

fetch_repos(username)

for idx, repo in enumerate(Repos.all, start=1):
    print(f'{idx}. {repo.get_name()}')

repo_num = input("Type a repo number to find out more: ")

print(Repos.find_by_input(repo_num).get_details())
