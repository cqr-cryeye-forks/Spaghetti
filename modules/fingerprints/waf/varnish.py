import re


class Varnish:
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'X-Varnish', item[0], re.I) is not None
            _ |= re.search(r'varnish*', item[1], re.I) is not None
            if _:
                return "Varnish FireWall (OWASP)"
