"""
@see https://amazinghiring.com/searching-for-developers-on-github/
but: https://www.benfrederickson.com/github-wont-help-with-hiring/
"""

from github import Github   # PyGithub module, @see https://pygithub.readthedocs.io/en/latest/examples.html
from os import environ as env
from sys import exit
from dotenv import load_dotenv


def init_github_client():
    tok_var = 'GITHUB_ACCESS_TOKEN_GH4HR'
    load_dotenv()
    gh_tok = env.get(tok_var)

    if not gh_tok:
        exit("Can't get Github access token from environment variable, check, that it's set")

    g = Github(gh_tok)
    return g

def search_users(g, q):
    """
    @see https://developer.github.com/v3/search/#search-users
    @see https://help.github.com/en/github/searching-for-information-on-github/searching-users
    Note: g.search_users() returns PaginatedList
    # >>> g.search_users(query='language:python location:Moscow')
    # <github.PaginatedList.PaginatedList object at 0x7f27c0afdac8>

    Cheatsheet:
    type: user/org
    repos: n
    location: aha

    :param g:
    :param q:
    :return:
    """
    pass

if __name__ == '__main__':
    g = init_github_client()
    print("Entering main loop")
    try:
        while True:
            # listen for input
            print("Enter search query for users: ")
            q = input()
            result = g.search_users(query=q)
            if result and result.totalCount > 0:
                print(f"Got {result.totalCount} results. Printing")
                for r in result:
                    print(r)
            else:
                print("Sorry, no result this time")

    except KeyboardInterrupt:
        print("Interrupted, exiting")
        exit()


# >>> result = g.search_users(query='language:python location:Moscow pushed:>2019-10-21')

# fun example
# >>> repositories = g.search_repositories(query='good-first-issues:>3')
# >>> for repo in repositories:
# ...    print(repo)
