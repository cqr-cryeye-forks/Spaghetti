import contextlib
import re

from request import request
from utils import output, params


class Php:
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
            'name': 'Php',
            'fullname': 'PHP Code Injection',
            'author': 'Momo Outaadi (M4ll0k)',
            'description': 'Find PHP Code Injection Vulnerability'
        }
        self.output.test('Checking php code injection...')
        payload = "1;phpinfo()"
        with contextlib.suppress(Exception):
            for url in self.urls:
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
                        if resp.status_code == 200 and re.search(
                                r'<title>phpinfo[()]</title>|<h1 class="p">PHP Version (.*?)</h1>', resp.content.decode('utf-8')):
                            self.output.plus(f'That site is may be vulnerable to PHP Code Injection at {para}')

                elif len(param) == 1:
                    resp = self.request.send(
                        url=param[0],
                        method="GET",
                        payload=None,
                        headers=None,
                        cookies=self.cookie
                    )
                    if resp.status_code == 200 and re.search(
                            r'<title>phpinfo[()]</title>|<h1 class="p">PHP Version (.*?)</h1>', resp.content.decode('utf-8')):
                        self.output.plus(f'That site is may be vulnerable to PHP Code Injection at {param[0]}')
