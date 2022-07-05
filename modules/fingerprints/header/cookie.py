import re

from utils import output


class Cookie:
    @staticmethod
    def run(headers):
        cookie = headers['set-cookie'] or None
        if cookie is not None:
            if re.search(r'domain=\S*', cookie, re.I):
                output.Output().plus(
                    f"Cookies are only accessible to this domain: {re.findall(r'domain=(.+?);', cookie, re.I)[0]}")

            if not re.search('httponly', cookie, re.I):
                output.Output().plus('Cookies created without HTTPOnly Flag.')
            if not re.search('secure', cookie, re.I):
                output.Output().plus('Cookies created without Secure Flag.')
