import re


class Python:
    @staticmethod
    def run(content, headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'python|zope|zserver|wsgi|plone|_ZopeId', item[1], re.I) is not None
            if not _:
                _ |= re.search(r'\.py$', content) is not None
            if _:
                return "Python"
