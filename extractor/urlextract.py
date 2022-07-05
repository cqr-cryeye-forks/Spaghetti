import contextlib
import re


class UrlExtract:
    @staticmethod
    def run(content):
        with contextlib.suppress(Exception):
            return re.findall(
                r'href=[\'"]?([^\'" >]+)|Allow: (/.*)|Disallow: (/.*)|<loc>(.+?)</loc>',
                content)
