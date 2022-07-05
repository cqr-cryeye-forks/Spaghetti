import re

from request import request
from utils import output


class HtmlObject:
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
            'name': 'HtmlObject',
            'fullname': 'Html Object',
            'author': 'Momo Outaadi (M4ll0k)',
            'description': 'Find Html Object'
        }
        self.output.test('Checking html object..')
        try:
            resp = self.request.send(
                url=self.url,
                method="GET",
                payload=None,
                headers=None,
                cookies=self.cookie
            )
            if re.search(r'<object.*?>.*?</object>', resp.content.decode('utf-8'), re.I):
                self.output.plus('Found HTML Object, logs the existence of HTML object tags at:' % self.url)
        except Exception as e:
            print(e)
