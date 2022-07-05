from urllib import parse


class UrlParser:
    def __init__(self, url):
        self.url = url
        self.scheme = parse.urlsplit(url).scheme
        self.netloc = parse.urlsplit(url).netloc
        self.path = parse.urlsplit(url).path
        self.query = parse.urlsplit(url).query

    def host(self):
        return self.path.split('/')[0] if self.netloc == "" else self.netloc

    def host_path(self):
        if self.netloc == "":
            return f"http://{self.path}"
        else:
            return f"{self.scheme}://{self.netloc}{self.path}"

    def complete(self):
        if self.netloc == "":
            return f"http://{self.path}?{self.query}"
        else:
            return f"{self.scheme}://{self.netloc}{self.path}?{self.query}"
