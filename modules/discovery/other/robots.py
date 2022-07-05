import contextlib
import re

from request import request, urlcheck
from utils import output


class Robots:
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
            'name': 'Robots',
            'fullname': 'Robots',
            'author': 'Momo Outaadi (M4ll0k)',
            'description': 'Checking Robots Paths'
        }
        self.output.test('Checking robots paths..')
        with contextlib.suppress(Exception):
            url = self.ucheck.path(self.url, 'robots.txt')
            resp = self.request.send(
                url=url,
                method="GET",
                payload=None,
                headers=None,
                cookies=self.cookie
            )
            if resp.url == url:
                if found_paths := re.findall(r' (/\S*)', resp.content.decode('utf-8')):
                    print("")
                    for path in found_paths:
                        if path.startswith('/'):
                            path = path[1:]
                        url2 = self.ucheck.path(self.url, path)
                        resp = self.request.send(
                            url=url2,
                            method="GET",
                            payload=None,
                            headers=None,
                            cookies=self.cookie
                        )
                        print(f" - [{resp.status_code}] {url2}")
                    print("")
