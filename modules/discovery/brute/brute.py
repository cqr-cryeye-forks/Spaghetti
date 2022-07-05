from modules.discovery.brute import file, admin, backdoor, bdir, bfile, log
from modules.discovery.brute.dir import Dir
from utils import output


class Brute:
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
        self.output.info('Starting bruteforce module...')
        file.File(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            url=self.url,
            cookie=self.cookie
        ).run()
        admin.Admin(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            url=self.url,
            cookie=self.cookie
        ).run()
        backdoor.Backdoor(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            url=self.url,
            cookie=self.cookie
        ).run()
        bdir.BackDoorDirectory(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            url=self.url,
            cookie=self.cookie
        ).run()
        bfile.Bfile(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            url=self.url,
            cookie=self.cookie
        ).run()
        Dir(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            url=self.url,
            cookie=self.cookie
        ).run()
        log.Log(
            agent=self.agent,
            proxy=self.proxy,
            redirect=self.redirect,
            timeout=self.timeout,
            url=self.url,
            cookie=self.cookie
        ).run()
