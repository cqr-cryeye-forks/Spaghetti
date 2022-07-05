import contextlib
import re


class Joomla:
    @staticmethod
    def run(content):
        _ = False
        with contextlib.suppress(Exception):
            _ = re.search(
                r'/index.php?option=(\S*)|<meta name="generator" content="Joomla*|Powered by '
                r'<a href="http://www.joomla.org">Joomla!</a>*',
                content) is not None
            if _ and re.search('/templates/*', content, re.I):
                return "Joomla"
