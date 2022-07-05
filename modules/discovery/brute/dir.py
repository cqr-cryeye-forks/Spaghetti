import re

from request import request, urlcheck
from utils import output


class Dir:
    def __init__(self, agent, proxy, redirect, timeout, url, cookie):
        self.url = url
        self.cookie = cookie
        self.output = output.Output()
        self.ucheck = urlcheck.UrlCheck()
        self.request = request.Request(
            agent=agent,
            proxy=proxy,
            redirect=redirect,
            timeout=timeout
        )

    def run(self):
        info = {
            'name': 'Dir',
            'fullname': 'Common Directory',
            'author': 'Momo Outaadi (M4ll0k)',
            'description': 'Find Common Directory'
        }
        self.output.test('Checking common dirs..')
        db = open('data/cdir.txt', 'r')
        db_files = [x.split('\n') for x in db]
        try:
            for d in db_files:
                url = self.ucheck.path(self.url, d[0])
                resp = self.request.send(
                    url=url,
                    method="GET",
                    payload=None,
                    headers=None,
                    cookies=self.cookie
                )
                if resp.status_code == 200 and resp.url == url + "/".replace(' ', '%20'):
                    self.output.plus('Found "%s" directory at %s' % (d[0], resp.url))
                    if re.search(
                            r'Index Of|<a href="?C=N;O=D">Name</a>|<A HREF="?M=A">Last modified</A>|Parent Directory</a>|<TITLE>Folder Listing.|<<table summary="Directory Listing"',
                            resp.content.decode('utf-8'), re.I):
                        self.output.plus(f'Indexing enabled at {resp.url}')
        except Exception as e:
            print(e)
