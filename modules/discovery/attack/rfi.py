import contextlib
import re

from request import request
from utils import output, params


class Rfi:
    def __init__(self, agent, proxy, redirect, timeout, urls, cookie):
        if type(urls) == str:
            urls = [urls]
        self.urls = urls
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
            'name': 'Rfi',
            'fullname': 'Remote File Inclusion',
            'author': 'Momo Outaadi (M4ll0k)',
            'description': 'Find Remote File Inclusion (RFI) Vulnerability'
        }
        self.output.test('Checking remote file inclusion...')
        db = open('data/rfi.txt', 'r')
        db_files = [x.split('\n') for x in db]
        pl = r"root:/root:/bin/bash|default=multi([0])disk([0])rdisk([0])partition([1])\\WINDOWS"
        with contextlib.suppress(Exception):
            for payload in db_files:
                for url in self.urls:
                    # replace queries with payload
                    param = params.Params(url, payload[0]).process()
                    if len(param) > 1:
                        for para in param:
                            resp = self.request.send(
                                url=para,
                                method="GET",
                                payload=None,
                                headers=None,
                                cookies=self.cookie
                            )
                            if re.search(pl, resp.content.decode('utf-8')):
                                self.output.plus(
                                    f'That site is may be vulnerable to Remote File Inclusion (RFI) at {para}')

                    elif len(param) == 1:
                        resp = self.request.send(
                            url=param[0],
                            method="GET",
                            payload=None,
                            headers=None,
                            cookies=self.cookie
                        )
                        if re.search(pl, resp.content.decode('utf-8')):
                            self.output.plus(
                                f'That site is may be vulnerable to Remote File Inclusion (RFI) at {param[0]}')
