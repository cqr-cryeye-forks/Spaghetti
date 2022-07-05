import re


class Cloudflare:
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            # noinspection RegExpDuplicateCharacterInClass
            _ = re.search(r'cloudflare[-nginx]', item[1], re.I) is not None
            _ |= re.search(r'__cfduid=', item[1], re.I) is not None
            _ |= re.search(r'cf-ray', item[0], re.I) is not None
            if _:
                return "CloudFlare Web Application Firewall (CloudFlare)"
