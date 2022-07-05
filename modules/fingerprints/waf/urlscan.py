import re


class Urlscan:
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'Rejected-By-UrlScan', item[0], re.I) is not None
            if _:
                return "UrlScan Firewall (Microsoft)"
