import re


class Hyperguard:
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'^WODSESSION=', item[1], re.I) is not None
            if _:
                return "Hyperguard Web Application Firewall (art of defence)"
