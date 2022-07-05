import contextlib
import re
from urllib import parse

from bs4 import BeautifulSoup

from request import urlcheck
from utils import text


class Forms:
    def run(self, content, url):
        forms = []
        with contextlib.suppress(Exception):
            soup = BeautifulSoup(content, features="html.parser")
            for match in soup.findAll('form'):
                if match not in forms:
                    forms.append(match)
            for form in forms:
                return urlcheck.UrlCheck().path(url, self.extractor(form))

    @staticmethod
    def extractor(form):
        form = text.convert_to_utf_8(form)
        method = []
        action = []
        names = []
        values = []
        with contextlib.suppress(Exception):
            method += re.findall(r'method=\"(.+?)\"', form, re.I)
            action += re.findall(r'action=\"(.+?)\"', form, re.I)
            names += re.findall(r'name=\"(.+?)\"', form, re.I)
            values += re.findall(r'value=(\S*)', form, re.I)
        params = []
        with contextlib.suppress(Exception):
            for i in range(len(names)):
                values[i] = values[i].split('"')[1]
                params.extend((names[i], values[i]))
        with contextlib.suppress(Exception):
            params = list(zip(*[iter(params)]*2))
            data = parse.unquote(parse.urlencode(params))
            if not method:
                method = ['get']
            method = method[0]
            if method.upper() == "GET":
                return data
