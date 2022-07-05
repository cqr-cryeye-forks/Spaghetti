import contextlib
import re

from request import request
from utils import output, params


class Xpath:
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
            'name': 'XPath',
            'fullname': 'XPath Injection',
            'author': 'Momo Outaadi (M4ll0k)',
            'description': 'Find XPATH Injection'
        }
        db = open('data/xpath.txt', 'r')
        db_files = [x.split('\n') for x in db]
        self.output.test('Checking xpath injection...')
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
                            if re.search(r'XPATH syntax error:|XPathException', resp.content.decode('utf-8'), re.I):
                                self.output.plus(f'That site is may be vulnerable to XPath Injection at {para}')

                    elif len(param) == 1:
                        resp = self.request.send(
                            url=param[0],
                            method="GET",
                            payload=None,
                            headers=None,
                            cookies=self.cookie
                        )
                        if re.search(r'XPATH syntax error:|XPathException', resp.content.decode('utf-8'), re.I):
                            self.output.plus(f'That site is may be vulnerable to XPath Injection at {param[0]}')
