from modules.discovery.vulns import crime, anonymous, shellshock, strutsshock
from utils import output


class Vulnerabilities:
    def __init__(self, agent, proxy, redirect, timeout, url, cookie):
        self.agent = agent
        self.proxy = proxy
        self.redirect = redirect
        self.timeout = timeout
        self.url = url
        self.cookie = cookie
        self.output = output.Output()

    def run(self):
        print("")
        self.output.info('Starting vulnerabilities module...')
        crime.Crime(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            url=self.url,
            cookie=self.cookie
        ).run()
        anonymous.Anonymous(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            url=self.url,
            cookie=self.cookie
        ).run()
        shellshock.Shellshock(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            url=self.url,
            cookie=self.cookie
        ).run()
        strutsshock.StrutsShock(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            url=self.url,
            cookie=self.cookie
        ).run()
