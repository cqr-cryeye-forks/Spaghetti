import re


class TrafficShield:
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'F5-TrafficShield', item[1], re.I) is not None
            _ |= re.search(r'ASINFO=', item[1], re.I) is not None
            if _:
                return "TrafficShield (F5 Networks)"
