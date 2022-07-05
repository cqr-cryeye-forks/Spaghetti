import re


class Wallarm:
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'nginx-wallarm', item[1], re.I) is not None
            if _:
                return "Wallarm Web Application Firewall (Wallarm)"
