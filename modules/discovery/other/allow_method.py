import contextlib
import re

from request import request
from utils import output


class AllowMethod:
    def __init__(self, agent, proxy, redirect, timeout, url, cookie):
        self.url = url
        self.cookie = cookie
        self.output = output.Output()
        self.request = request.Request(
            agent=agent,
            proxy=proxy,
            redirect=redirect,
            timeout=timeout
        )

    def run(self):
        info = {
            'name': 'AllowMethod',
            'fullname': 'Allow Method',
            'author': 'Momo Outaadi (M4ll0k)',
            'description': 'HTTP Allow Method'
        }
        self.output.test('Checking http allow methods..')
        # noinspection SpellCheckingInspection
        db = open('data/allowmethod.txt', 'r')
        db_files = [x.split('\n') for x in db]
        with contextlib.suppress(Exception):
            for method in db_files:
                resp = self.request.send(url=self.url, method=method[0], payload=None, headers=None,
                                         cookies=self.cookie)
                if re.search(r'allow|public', str(resp.headers.keys()), re.I):
                    allow = resp.headers['allow']
                    if allow is None:
                        allow = resp.headers['public']
                    if allow not in [None, '']:
                        self.output.plus(f'HTTP Allow Method: {allow}')
                        break
