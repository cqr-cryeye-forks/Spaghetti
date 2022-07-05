import contextlib

from modules.discovery.disclosure.card import print_credit_cards
from modules.discovery.disclosure.email import print_emails
from modules.discovery.disclosure.ip import print_ip
from request import request
from utils import output


class Disclosure:
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
        print("")
        self.output.info('Starting disclosures module...')
        with contextlib.suppress(Exception):
            resp = self.request.send(
                url=self.url,
                method="GET",
                payload=None,
                headers=None,
                cookies=self.cookie
            )
            content = resp.content.decode('utf-8')
            print_ip(content)
            print_emails(content)
            print_credit_cards(content)
