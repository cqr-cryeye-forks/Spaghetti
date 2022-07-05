import re


class Barracuda:
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'barracuda*', item[1], re.I) is not None
            _ |= re.search(r'barra_counter_session=', item[1], re.I) is not None
            _ |= re.search(r'barracuda_', item[1], re.I) is not None
            if _:
                return "Barracuda Web Application Firewall (Barracuda Networks)"
