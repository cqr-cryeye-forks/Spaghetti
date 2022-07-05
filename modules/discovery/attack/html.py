import contextlib
import re

from request import request
from utils import output, params


class Html:
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
            'name': 'Html',
            'fullname': 'Html code injection',
            'author': 'Momo Outaadi (M4ll0k)',
            'description': 'Find html code injection'
        }
        self.output.test('Checking html injection...')
        with contextlib.suppress(Exception):
            payload = "<h1><a href=\"http://www.google.com\">Click Spaghetti!</a></h1>"
            for url in self.urls:
                # replace queries with payload
                param = params.Params(url, payload).process()
                if len(param) > 1:
                    for para in param:
                        resp = self.request.send(
                            url=para,
                            method="GET",
                            payload=None,
                            headers=None,
                            cookies=self.cookie
                        )
                        if resp.status_code == 200 and re.search(payload, resp.content.decode('utf-8')):
                            self.output.plus(
                                f'That site is may be vulnerable to HTML Code Injection at {para}')
                elif len(param) == 1:
                    resp = self.request.send(
                        url=param[0],
                        method="GET",
                        payload=None,
                        headers=None,
                        cookies=self.cookie
                    )
                    if resp.status_code == 200 and re.search(payload, resp.content.decode('utf-8')):
                        self.output.plus(
                            f'That site is may be vulnerable to HTML Code Injection at {param[0]}'
                        )
