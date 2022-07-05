import re


class CiscoAceXML:
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'ACE XML Gateway', item[1], re.I) is not None
            if _:
                return "Cisco ACE XML Gateway (Cisco Systems)"
