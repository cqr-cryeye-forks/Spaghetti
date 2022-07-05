import contextlib
import re

from request import request
from utils import output, params


class LDAP:
    def __init__(self, agent, proxy, redirect, timeout, urls, cookie):
        if type(urls) == str:
            urls = [urls]
        self.urls = urls
        self.cookie = cookie
        self.output = output.Output()
        self.request = request.Request(
            agent=agent,
            proxy=proxy,
            redirect=redirect,
            timeout=timeout
        )

    @staticmethod
    def errors(data):
        error = (
            "supplied argument is not a valid ldap",
            "javax.naming.NameNotFoundException",
            "javax.naming.directory.InvalidSearchFilterException",
            "Invalid DN syntax",
            "LDAPException|com.sun.jndi.ldap",
            "Search: Bad search filter",
            "Protocol error occurred",
            "Size limit has exceeded",
            "The alias is invalid",
            "Module Products.LDAPMultiPlugins",
            "Object does not exist",
            "The syntax is invalid",
            "A constraint violation occurred",
            "An inappropriate matching occurred",
            "Unknown error occurred",
            "The search filter is incorrect",
            "Local error occurred",
            "The search filter is invalid",
            "The search filter cannot be recognized",
            "IPWorksASP.LDAP"
        )
        for error_message in error:
            if re.search(error_message, data):
                return "LDAP Injection"

    def run(self):
        info = {
            'name': 'LDAP',
            'fullname': 'LDAP Injection',
            'author': 'Momo Outaadi (M4ll0k)',
            'description': 'Find LDAP Injection'
        }
        self.output.test('Checking ldap injection...')
        db = open('data/ldap.txt', 'r')
        db_files = [x.split('\n') for x in db]
        with contextlib.suppress(Exception):
            for payload in db_files:
                for url in self.urls:
                    # replace queries with payload
                    param = params.Params(url, payload[0]).process()
                    if len(param) > 1:
                        for para in param:
                            resp = self.request.send(
                                url=para,
                                method="GET",
                                payload=None,
                                headers=None,
                                cookies=self.cookie
                            )
                            if self.errors(resp.content.decode('utf-8')):
                                self.output.plus(f'That site is may be vulnerable to LDAP Injection at {para}')

                    elif len(param) == 1:
                        resp = self.request.send(
                            url=param[0],
                            method="GET",
                            payload=None,
                            headers=None,
                            cookies=self.cookie
                        )
                        if self.errors(resp.content.decode('utf-8')):
                            self.output.plus(f'That site is may be vulnerable to LDAP Injection at {param[0]}')
