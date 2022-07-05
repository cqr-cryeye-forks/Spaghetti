import re


class SonicWall:
    @staticmethod
    def run(content):
        _ = False
        _ = re.search(r'This request is blocked by the SonicWALL', content, re.I) is not None
        _ |= re.search(r'Web Site Blocked.+\bnsa_banner', content, re.I) is not None
        if _:
            return "SonicWALL (Dell)"
