from request import request, urlcheck
from utils import output


class MultipleIndex:
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
            'name': 'MultipleIndex',
            'fullname': 'Multiple Index',
            'author': 'Momo Outaadi (M4ll0k)',
            'description': 'Find Multiple Index Page'
        }
        self.output.test('Checking multiple index..')
        db = open('data/index.txt', 'r')
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
                if resp.status_code == 200 and resp.url == url.replace(' ', '%20'):
                    self.output.plus(f'Found Index Page at {resp.url}')
        except Exception as e:
            print(e)
