from request import request, urlcheck
from utils import output


class Bfile:
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
            'name': 'Bfile',
            'fullname': 'Backup Files',
            'author': 'Momo Outaadi (M4ll0k)',
            'description': 'Find Backup Files'
        }
        self.output.test('Checking common backup files..')
        db = open('data/bfile.txt', 'r')
        backup_names = [x.split('\n') for x in db]
        db1 = open('data/cfile.txt', 'r')
        db_files = [x.split('\n') for x in db1]
        try:
            for name in backup_names:
                for file in db_files:
                    backup_file = name[0].replace('[name]', file[0])
                    url = self.ucheck.path(self.url, backup_file)
                    resp = self.request.send(
                        url=url,
                        method="GET",
                        payload=None,
                        headers=None,
                        cookies=self.cookie
                    )
                    if resp.status_code == 200 and resp.url == url.replace(' ', '%20'):
                        self.output.plus('Found file "%s" Backup at %s' % (file[0], resp.url))
        except Exception as e:
            print(e)
