import re


class Senginx:
    @staticmethod
    def run(content):
        _ = False
        _ = re.search(r'SENGINX-ROBOT-MITIGATION', content, re.I) is not None
        if _:
            return "SEnginx (Neusoft Corporation)"
