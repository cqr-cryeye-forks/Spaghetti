import re


class Symfony:
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'symfony=*', item[1], re.I) is not None
            if _:
                return "Symfony PHP"
