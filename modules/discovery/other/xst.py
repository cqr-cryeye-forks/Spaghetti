import contextlib
import re

from request import request
from utils import output


class XST:
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
            'name': 'XST',
            'fullname': 'Cross Site Tracing',
            'author': 'Momo Outaadi (M4ll0k)',
            'description': 'Cross Site Tracing (XST) vulnerability'
        }
        self.output.test('Checking cross site tracing..')
        with contextlib.suppress(Exception):
            resp = self.request.send(
                url=self.url,
                method="TRACE",
                payload=None,
                headers={
                    'Spaghetti': 'PastaXST',
                },
                cookies=self.cookie
            )
            if re.search('Spaghetti: *?PastaXST', resp.content.decode('utf-8'), re.I):
                self.output.plus('That site is may be vulnerable to Cross Site Tracing (XST) vulnerability.')
