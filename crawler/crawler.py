import contextlib
import itertools
import re
import sys
from urllib import parse

from constants.constants import BLACKLIST_EXTENSIONS
from extractor import urlextract, forms
from request import request, urlcheck, urlparser
from utils import output


class Crawler:

    def __init__(self, agent, proxy, redirect, timeout, url, cookie):
        self.url = url
        self.cookie = cookie
        self.forms = forms.Forms()
        self.output = output.Output()
        self.ucheck = urlcheck.UrlCheck()
        self.parser = urlparser.UrlParser(url)
        self.extract = urlextract.UrlExtract()
        self.request = request.Request(
            agent=agent,
            proxy=proxy,
            redirect=redirect,
            timeout=timeout
        )

    @staticmethod
    def get(data_list):
        return [i for i in data_list if re.search('=', i, re.I)]

    def run(self):
        links_list = []
        with contextlib.suppress(Exception):
            for path in ('', 'robots.txt', 'sitemap.xml', 'sp4gh3tt1'):
                url = self.ucheck.path(self.url, path)
                resp = self.request.send(url, cookies=self.cookie)
                content = resp.content.decode('utf-8')
                links = self.extract.run(content)
                if links is None:
                    links = []
                result_forms = self.forms.run(content, self.url)
                if result_forms is None:
                    result_forms = []
                links_list += links
                links_list += result_forms
            return self.parse(links_list)

    def thread_run(self):
        links = self.run()
        links_list = []
        if '--crawler' in sys.argv:
            self.output.info(f'Starting deep crawler for {self.parser.host()}')
            with contextlib.suppress(Exception):
                for link in links:
                    resp = self.request.send(link, cookies=self.cookie)
                    content = resp.content.decode('utf-8')
                    links_extract = self.extract.run(content)
                    if links_extract is None:
                        links_extract = []
                    forms_extract = self.forms.run(content, self.url)
                    if forms_extract is None:
                        forms_extract = []
                    links_list += links_extract
                    links_list += forms_extract
                links_list = self.get(self.parse(links_list))
                links_list = links_list + self.get(links)
                return links_list
        return links

    def parse(self, links):
        complete = []
        flinks = []
        def_links = []
        t_links = []
        d_links = []
        for link in links:
            t_links.extend(i for i in link if i != '' and i not in flinks)

        p_black_list = [link for link, bl in itertools.product(t_links, BLACKLIST_EXTENSIONS) if bl in link]

        for link, bl in itertools.product(t_links, p_black_list):
            if bl == link:
                index = t_links.index(bl)
                del t_links[index]
        for link in t_links:
            if link.startswith('./'):
                link = link.split('.')[1]
            if link.startswith('http://') or link.startswith('https://'):
                if link not in d_links:
                    d_links.append(link)
            elif link.startswith('www.'):
                link = f'http://{link}'
                if link not in d_links:
                    d_links.append(link)
            elif link.startswith('/'):
                link = self.ucheck.path(self.url, link)
                if link not in d_links:
                    d_links.append(link)
            else:
                link = self.ucheck.path(self.url, link)
                if link not in d_links:
                    d_links.append(link)
        for link in d_links:
            if not link.startswith('http'):
                continue
            if self.parser.host() not in link:
                pass
            elif link.startswith('http://http://') or link.startswith('https://http://'):
                link = 'http' + link.split('http')[2]
                complete.append(link)
            else:
                complete.append(link)
        for i in complete:
            i = parse.unquote(i)
            i = i.replace('&amp;', '&')
            if i not in def_links:
                def_links.append(i)
        return def_links

    def process(self):
        self.output.info(f'Starting crawler for {self.parser.host()}')
        return self.thread_run()
