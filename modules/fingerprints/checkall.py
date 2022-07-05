import contextlib

from modules.fingerprints.cms import cms
from modules.fingerprints.framework import framework
from modules.fingerprints.header import headers, cookie
from modules.fingerprints.lang import lang
from modules.fingerprints.os_types.os_type import detect_os
from modules.fingerprints.server import server
from modules.fingerprints.waf import waf
from request.request import Request
from utils import output


class Checkall:
    def __init__(self, agent, proxy, redirect, timeout, url, cookies):
        self.url = url
        self.cookie = cookies
        self.output = output.Output()
        self.request = Request(
            agent=agent,
            proxy=proxy,
            redirect=redirect,
            timeout=timeout
        )

    def run(self):
        self.output.info('Starting fingerprints module...')
        with contextlib.suppress(Exception):
            resp = self.request.send(
                url=self.url,
                method="GET",
                payload=None,
                headers=None,
                cookies=self.cookie
            )
            content = resp.content.decode('utf-8')
            try:
                ser = server.Server(self.url).run(resp.headers)
                self.output.plus(f'Server: {ser}')
            except Exception as e:
                print(f"Detect Server error: {e}")
            try:
                os_ = list(detect_os(resp.headers))
                for x in os_:
                    if x is not None:
                        self.output.plus(f'Operating system: {x}')
            except Exception as e:
                print(f"Detect OS error: {e}")
            try:
                firewall = list(waf.test_waf(resp.headers, content))
                for x in firewall:
                    if x is not None:
                        self.output.plus(f'Firewall: {x}')
            except Exception as e:
                print(f"Detect Firewall error: {e}")
            try:
                cms_ = list(cms.check_cms(content))
                for x in cms_:
                    if x is not None:
                        self.output.plus(f'Content Management System (CMS): {x}')
            except Exception as e:
                print(f"Detect CMS error: {e}")
            try:
                lang_ = list(lang.detect_langs(content, resp.headers))
                for x in lang_:
                    if x is not None:
                        self.output.plus(f'Language: {x}')
            except Exception as e:
                print(f"Detect Language error: {e}")
            try:
                frame = list(framework.test_frameworks(resp.headers, content))
                for x in frame:
                    if x is not None:
                        self.output.plus(f'Framework: {x}')
            except Exception as e:
                print(f"Detect Framework error: {e}")
            headers.Headers().run(resp.headers)
            cookie.Cookie().run(resp.headers)
