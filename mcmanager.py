#! /usr/bin/env python3
# Copyright (c) 2019 Joe Becher
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT


from urllib.request import urlopen, Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def fetch_page(url, user_agent):
    """Fetch a web page and return the contents."""
    try:
        req = Request(url,
                      headers={'User-Agent': user_agent})
        with urlopen(req) as r:
            return(r.read())
    except HTTPError as err:
        print('whoops! ' + err.msg)
        print(err.headers)

# https://minecraft.curseforge.com/modpacks?filter-game-version=2020709689%3A7132&filter-sort=4

# https://minecraft.curseforge.com/modpacks

def fetch_game_versions(user_agent):
    page_contents = fetch_page("https://minecraft.curseforge.com/modpacks", user_agent)
    soup = BeautifulSoup(page_contents, 'html.parser')
    versions = []
    for version in soup.find(id="filter-game-version").find_all("option"):
        try:
            if not version['class'] == "game-version-type":
                versions.append({'name': version.string, 'id': version['value']})
        except KeyError:
            pass

    return versions


def main():
    url = 'http://drazisil.com'

    admin_email = "<jwbecher@drazisil.com>"

    user_agent = "MCManager {}".format(admin_email)

    game_versions = fetch_game_versions(user_agent)
    for version in game_versions:
        print(version['name'])
    #
    # page_contents = fetch_page(url, user_agent)
    #
    # soup = BeautifulSoup(page_contents, 'html.parser')
    # print(soup.title.string)


if __name__ == "__main__":
    # execute only if run as a script
    main()
