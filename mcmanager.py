#! /usr/bin/env python3

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


def main():
    url = 'http://drazisil.com'

    admin_email = "<jwbecher@drazisil.com>"

    user_agent = "MCManager {}".format(admin_email)

    page_contents = fetch_page(url, user_agent)

    soup = BeautifulSoup(page_contents, 'html.parser')
    print(soup.title.string)


if __name__ == "__main__":
    # execute only if run as a script
    main()
