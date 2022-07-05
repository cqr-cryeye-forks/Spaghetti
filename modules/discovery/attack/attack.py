from modules.discovery.attack import Rfi, Sql, Xss, Php, LDAP, Html, Xpath
from utils import output


class Attack:
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
        self.output.info('Starting attacks module...')
        Rfi(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            urls=self.url,
            cookie=self.cookie
        ).run()
        Sql(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            urls=self.url,
            cookie=self.cookie
        ).run()
        Xss(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            urls=self.url,
            cookie=self.cookie
        ).run()
        Php(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            urls=self.url,
            cookie=self.cookie
        ).run()
        LDAP(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            urls=self.url,
            cookie=self.cookie
        ).run()
        Html(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            urls=self.url,
            cookie=self.cookie
        ).run()
        Xpath(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            urls=self.url,
            cookie=self.cookie
        ).run()
