import contextlib
import re

from request import request
from utils import output, params


class Xss:
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
            'name': 'Xss',
            'fullname': 'Cross Site Scripting',
            'author': 'Momo Outaadi (M4ll0k)',
            'description': 'Find Cross Site Scripting (XSS) vulnerability'
        }
        db = open('data/xss.txt', 'r')
        db_files = [x.split('\n') for x in db]
        self.output.test('Checking cross site scripting...')
        with contextlib.suppress(Exception):
            for payload in db_files:
                for url in self.urls:
                    # replace queries with payload
                    parameters = params.Params(url, payload[0]).process()
                    if len(parameters) > 1:
                        for param in parameters:
                            resp = self.request.send(
                                url=param,
                                method="GET",
                                payload=None,
                                headers=None,
                                cookies=self.cookie
                            )
                            if resp.status_code == 200 and re.search(payload[0], resp.content.decode('utf-8'), re.I):
                                self.output.plus(f'That site is may be vulnerable to '
                                                 f'Cross Site Scripting (XSS) at {param}')

                    elif len(parameters) == 1:
                        resp = self.request.send(
                            url=parameters[0],
                            method="GET",
                            payload=None,
                            headers=None,
                            cookies=self.cookie
                        )
                        if resp.status_code == 200 and re.search(payload[0], resp.content.decode('utf-8'), re.I):
                            self.output.plus(f'That site is may be vulnerable to '
                                             f'Cross Site Scripting (XSS) at {parameters[0]}')
