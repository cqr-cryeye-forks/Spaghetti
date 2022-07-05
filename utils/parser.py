import re


class Parser:
    def __init__(self, results):
        self.results = results

    def clean(self):
        self.results = re.sub('<em>', '', self.results)
        self.results = re.sub('<b>', '', self.results)
        self.results = re.sub('</b>', '', self.results)
        self.results = re.sub('</em>', '', self.results)
        self.results = re.sub('%2f', ' ', self.results)
        self.results = re.sub('%3a', ' ', self.results)
        self.results = re.sub('<strong>', '', self.results)
        self.results = re.sub('</strong>', '', self.results)
        self.results = re.sub('<wbr>', '', self.results)
        self.results = re.sub('</wbr>', '', self.results)
        self.results = re.sub('<li>', '', self.results)
        self.results = re.sub('</li>', '', self.results)

        for x in ('>', ':', '=', '<', '/', '\\', ';', '&', '%3A', '%3D', '%3C'):
            self.results = self.results.replace(x, " ")

    def getmail(self):
        self.clean()
        return re.findall(r'[a-zA-Z\d.\-_+#~!$&\',;=:]+@+[a-zA-Z\d-]*\.\w*', self.results)

    def getip(self):
        self.clean()
        return re.findall(r'\d+(?:\.\d+){3}', self.results)

    def get_cards(self):
        self.clean()
        return re.findall(r'\d{4}[\s\-]*\d{4}[\s\-]*\d{4}[\s\-]*\d{4}', self.results)
