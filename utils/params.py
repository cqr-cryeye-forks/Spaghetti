import contextlib


class Params:
    def __init__(self, url, payload):
        self.url = url
        self.payload = payload

    def get(self):
        with contextlib.suppress(Exception):
            if '?' in self.url:
                params = self.url.split('?')[1]
                return params.split('&')

    def post(self):
        with contextlib.suppress(Exception):
            if '?' not in self.url:
                return self.url.split('&')

    def process(self):
        test_url = []
        links = []
        get = self.get()
        if get is not None:
            for x in get:
                if x not in links:
                    links.append(x)
        post = self.post()
        if post is not None:
            for y in post:
                if y not in links:
                    links.append(y)
        for param in links:
            p = param.replace(param.split('=')[1], self.payload)
            sp = param.replace(p.split('=')[1], param.split('=')[1])
            test_url.append(self.url.replace(sp, p))
        return test_url
