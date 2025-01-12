import contextlib
import socket
import subprocess

from request import urlparser
from utils import output


class Anonymous:
    def __init__(self, agent, proxy, redirect, timeout, url, cookie):
        self.url = url
        self.cookie = cookie
        self.agent = agent
        self.proxy = proxy
        self.redirect = redirect
        self.timeout = timeout
        self.output = output.Output()
        self.parser = urlparser.UrlParser(url)

    def run(self):
        info = {
            'name': 'Anonymous',
            'fullname': 'Anonymous Cipher',
            'author': 'Momo Outaadi (M4ll0k)',
            'description': 'SSL insecure cipher: allows remote attackers to obtain sensitive information'
        }
        self.output.test('Scanning anonymous cipher vuln...')
        ip = ''
        port = '443'
        with contextlib.suppress(Exception):
            ip += socket.gethostbyname(self.parser.host())
            socket.inet_aton(ip)
            r = subprocess.Popen(
                ['timeout', '4', 'openssl', 's_client', '-connect', f"{ip}:{port}", "-cipher", "aNULL"],
                stderr=subprocess.STDOUT,
                stdout=subprocess.PIPE
            ).communicate()[0]

            if 'handshake failure' not in r:
                self.output.plus('That site is vulnerable to Anonymous Cipher, CVE-2007-1858.')
