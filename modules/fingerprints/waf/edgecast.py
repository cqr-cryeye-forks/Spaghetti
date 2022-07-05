import re


class Edgecast:
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'ECDF', item[1], re.I) is not None
            if _:
                return "EdgeCast Web Application Firewall (Verizon)"
