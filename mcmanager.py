#! /usr/bin/env python3

from urllib.request import urlopen, Request
from urllib.error import HTTPError


def main():
    url = 'http://drazisil.com'

    admin_email = "<jwbecher@drazisil.com>"

    try:
        user_agent = "MCManager {}".format(admin_email)
        print(user_agent)
        req = Request(url,
                      headers={'User-Agent': user_agent})
        with urlopen(req) as r:
            print(r.info())
            print(r.read())
    except HTTPError as err:
        print('whoops! ' + err.msg)
        print(err.headers)


if __name__ == "__main__":
    # execute only if run as a script
    main()
