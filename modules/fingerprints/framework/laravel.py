import re


class Laravel:
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'laravel_session=', item[1], re.I) is not None
            if _:
                return "Laravel (PHP)"
