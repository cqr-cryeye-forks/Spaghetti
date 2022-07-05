from modules.discovery.other import allow_method, xst, listing, robots, phpinfo, htmlobject, dav
from utils import output


class Other:
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
        self.output.info('Starting others module...')
        allow_method.AllowMethod(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            url=self.url,
            cookie=self.cookie
        ).run()
        xst.XST(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            url=self.url,
            cookie=self.cookie
        ).run()
        dav.Dav(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            url=self.url,
            cookie=self.cookie
        ).run()
        listing.Listing(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            url=self.url,
            cookie=self.cookie
        ).run()
        robots.Robots(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            url=self.url,
            cookie=self.cookie
        ).run()
        phpinfo.Phpinfo(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            url=self.url,
            cookie=self.cookie
        ).run()
        htmlobject.HtmlObject(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            url=self.url,
            cookie=self.cookie
        ).run()
