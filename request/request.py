import sys

import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning

from request import ragent, urlcheck


class Request:
    def __init__(self, **kwargs):
        self.agent = None if "agent" not in kwargs else kwargs["agent"]
        self.proxy = None if "proxy" not in kwargs else kwargs["proxy"]
        self.redirect = True if "redirect" not in kwargs else kwargs["redirect"]
        self.timeout = None if "timeout" not in kwargs else kwargs["timeout"]
        self.ragent = ragent.random_agent()
        self.ucheck = urlcheck.UrlCheck()

    def send(self, url, method="GET", payload=None, headers=None, cookies=None):
        if payload is None:
            payload = {}
        if headers is None:
            headers = {}
        if cookies is not None:
            cookies = {cookies: ''}
        if "--random-agent" in sys.argv:
            headers['User-Agent'] = self.ragent
        else:
            headers['User-Agent'] = self.agent
        # requests session
        request = requests.Session()
        urllib3.disable_warnings(InsecureRequestWarning)
        # get method
        if method.upper() == "GET":
            if payload:
                url = f"{self.ucheck.payload(url, payload)}"
            return request.request(method=method.upper(),
                                   url=url,
                                   headers=headers,
                                   cookies=cookies,
                                   timeout=self.timeout,
                                   allow_redirects=self.redirect,
                                   proxies={'http': self.proxy, 'https': self.proxy, 'ftp': self.proxy, },
                                   verify=False)

        elif method.upper() == "POST":
            return request.request(method=method.upper(),
                                   url=url,
                                   data=payload,
                                   headers=headers,
                                   cookies=cookies,
                                   timeout=self.timeout,
                                   allow_redirects=self.redirect,
                                   proxies={'http': self.proxy, 'https': self.proxy, 'ftp': self.proxy},
                                   verify=False)

        else:
            return request.request(method=method.upper(),
                                   url=url,
                                   data=payload,
                                   headers=headers,
                                   cookies=cookies,
                                   timeout=self.timeout,
                                   allow_redirects=self.redirect,
                                   proxies={'http': self.proxy, 'https': self.proxy, 'ftp': self.proxy},
                                   verify=False)
