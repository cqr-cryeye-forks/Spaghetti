import re


class SiteLock:
    @staticmethod
    def run(content):
        _ = False
        _ = re.search(r'SiteLock Incident ID', content, re.I) is not None
        if _:
            return "TrueShield Web Application Firewall (SiteLock)"
