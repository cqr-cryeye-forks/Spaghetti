import re


class Linux:
    @staticmethod
    def run(os):
        for item in os.items():
            if _ := re.findall(r'linux|ubuntu|gentoo|debian|dotdeb|centos|redhat|sarge|etch|lenny|squeeze|wheezy|jessie|red hat|scientific linux', str(item), re.I):
                return _[0]
