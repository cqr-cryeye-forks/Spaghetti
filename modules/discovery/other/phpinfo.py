import re

from request import request, urlcheck
from utils import output


class Phpinfo:
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
            'name': 'PHPInfo',
            'fullname': 'PHPInfo',
            'author': 'Momo Outaadi (M4ll0k)',
            'description': 'Find PHPInfo page'
        }
        self.output.test('Checking phpinfo..')
        db = open('data/phpinfo.txt', 'r')
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
                if re.search(r'<h1 class="p">PHP Version (.*?)</h1>|(<tr class="h"><td>\n|alt="PHP Logo" /></a>)',
                             resp.content.decode('utf-8')):
                    self.output.plus(f'Found phpinfo page at {resp.url}')
                    break
        except Exception as e:
            print(e)
