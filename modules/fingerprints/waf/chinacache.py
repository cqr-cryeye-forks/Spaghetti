import re


class ChinaCache:
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'Powered-By-ChinaCache', item[0], re.I) is not None
            if _:
                return "ChinaCache-CDN"
