import re


class Baidu:
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'yunjiasu-nginx', item[1], re.I) is not None
            _ |= re.search(r'YJS-ID', item[1], re.I) is not None
            _ |= re.search(r'fhl', item[1], re.I) is not None
            if _:
                return "Yunjiasu Web Application Firewall (Baidu)"
