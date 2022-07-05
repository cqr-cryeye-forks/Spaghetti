from request import request, urlcheck
from utils import output


class BackDoorDirectory:
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
            'name': 'BDir',
            'fullname': 'Backup Dirs',
            'author': 'Momo Outaadi (M4ll0k)',
            'description': 'Find Backup Dirs'
        }
        self.output.test('Checking common backup dirs..')
        # noinspection SpellCheckingInspection
        backdoor_file = open('data/bdir.txt', 'r')
        backdoor_dirs_files = [x.split('\n') for x in backdoor_file]
        db = open('data/cdir.txt', 'r')
        db_files = [x.split('\n') for x in db]
        try:
            for directory in backdoor_dirs_files:
                for file_name in db_files:
                    back_door_dir = directory[0].replace('[name]', file_name[0])
                    url = self.ucheck.path(self.url, back_door_dir)
                    resp = self.request.send(
                        url=url,
                        method="GET",
                        payload=None,
                        headers=None,
                        cookies=self.cookie
                    )
                    if resp.status_code == 200 and resp.url == url.replace(' ', '%20'):
                        self.output.plus('Found directory "%s" Backup at %s' % (file_name[0], resp.url))
        except Exception as e:
            print(e)
