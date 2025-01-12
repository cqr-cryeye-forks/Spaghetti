from request import request, urlcheck
from utils import output


class Listing:
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
            'name': 'listing',
            'fullname': '.listing',
            'author': 'Momo Outaadi (M4ll0k)',
            'description': 'Find indexing page with .listing'
        }
        self.output.test('Checking listing..')
        try:
            url = self.ucheck.path(self.url, '.listing')
            resp = self.request.send(
                url=url,
                method="GET",
                payload=None,
                headers=None,
                cookies=self.cookie
            )
            if resp.status_code == 200 and resp.url == url.replace(' ', '%20'):
                self.output.plus(f'Indexing enabled with ".listing" file at {resp.url}')
        except Exception as e:
            print(e)
