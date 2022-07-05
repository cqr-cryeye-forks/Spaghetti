import re


class Php:
    @staticmethod
    def run(content, headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'X-PHP-PID|PHP\S*|PHPSESSID', str(item)) is not None
            if not _:
                _ |= re.search(r'\.php$|\.phtml$', content) is not None
            if _:
                return "PHP"
