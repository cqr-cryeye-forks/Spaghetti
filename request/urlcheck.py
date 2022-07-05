class UrlCheck:
    @staticmethod
    def payload(url, payload):
        if url.endswith('/') & payload.startswith('/'):
            return f"{url[:-1]}?{payload[1:]}"
        elif not url.endswith('/') & (payload.startswith('/')):
            return f"{url}?{payload[1:]}"
        elif url.endswith('/') and not (payload.startswith('/')):
            return f"{url[:-1]}?{payload}"
        else:
            return f"{url}?{payload}"

    @staticmethod
    def path(url, path):
        if url.endswith('/') & path.startswith('/'):
            return str(url + path[:-1]) if path.endswith('/') else str(url[:-1] + path)
        elif not url.endswith('/') and not path.startswith('/'):
            return str(f"{url}/{path[:-1]}") if path.endswith('/') else str(f"{url}/{path}")

        else:
            return str(url + path[:-1]) if path.endswith('/') else str(url + path)
