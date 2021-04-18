from pathlib import Path
from typing import Iterable
from urllib.parse import parse_qs
from http.cookies import SimpleCookie


class HTTPError(Exception):

    def __init__(self, code: int, reason: str):
        super().__init__(reason)
        self.code = code
        self.reason = reason


class HTTPNotFoundError(HTTPError):

    def __init__(self):
        super().__init__(404, 'Not Found')


class HTTPMethodNotAllowedError(HTTPError):

    def __init__(self):
        super().__init__(405, 'Method Not Allowed')


class HTTPRequest:

    __slots__ = (
        'method',
        'path',
        'query',
        'remote_addr',
        'cookies',
        'headers',
        'form',
    )

    def __init__(self, environ: dict):
        self.method = environ['REQUEST_METHOD']
        self.path = environ['PATH_INFO']
        self.query = parse_qs(environ['QUERY_STRING'])
        self.remote_addr = environ['REMOTE_ADDR']
        self.cookies = SimpleCookie()
        self.headers = {
            key[5:].replace('_', '-'): val
            for key, val in environ.items()
            if key.startswith('HTTP_')
        }

        ctype = environ.get('CONTENT_TYPE', '')
        clen = int(environ.get('CONTENT_LENGTH') or 0)
        self.headers['CONTENT-TYPE'] = ctype
        self.headers['CONTENT-LENGHT'] = clen

        if 'COOKIE' in self.headers:
            self.cookies.load(self.headers['COOKIE'])

        if self.method == 'POST' and ctype == 'application/x-www-form-urlencoded':
            self.form = parse_qs(environ['wsgi.input'].read(clen).decode())

    def __repr__(self) -> str:
        return (
            f'HTTPRequest(method="{self.method}", path="{self.path}"), '
            f'query={self.query}, remote_addr="{self.remote_addr}", '
            f'headers={self.headers}'
        )


class WebApp:

    def __init__(self):
        self.default_http_headers = [
            ('Content-Type', 'text/html'),
            ('Cache-Control', 'no-store'),
        ]

    def do_get(self, request: HTTPRequest) -> tuple:
        print(request.cookies)

        root = Path('html')
        route = request.path

        # TODO: assert root path
        filepath = root / 'index.html' if route == '/' else root / route.lstrip('/')

        if filepath.suffix != '.html' or not filepath.is_file():
            raise HTTPNotFoundError()

        with open(filepath, 'rb') as fd:
            return fd.read(), None

    def do_post(self, request: HTTPRequest) -> tuple:
        # print(repr(request))

        # POST request routing
        if not request.path != 'feedback.html':
            raise HTTPMethodNotAllowedError()

        return self.do_get(request)[0], [
            (
                'Set-Cookie',
                f'feedback_email={request.form["email"][0]}; Max-Age=30'
            )
        ]

    def __call__(self, environ: dict, start_response: callable) -> Iterable:
        request = HTTPRequest(environ)
        http_method = request.method.lower()

        # for key, val in environ.items():
        #    print(key, '=', val)

        try:
            handler = getattr(self, f'do_{http_method}')
        except AttributeError:
            start_response('405 Method Not Allowed', self.default_http_headers)
            return [b'<h1>405 Only "GET" HTTP method is allowed</h1>']

        try:
            body, headers = handler(request)
            headers = headers or []
        except HTTPError as herr:
            start_response(f'{herr.code} {herr.reason}', self.default_http_headers)
            return [f'<h1>{herr.code} {herr.reason}</h1>'.encode()]
        except Exception as ex:
            print('[ERROR]', str(ex))
            start_response('500 Internal Server Error', self.default_http_headers)
            return [b'<h1>500 Internal Server Error</h1>']

        start_response('200 OK', self.default_http_headers + headers)
        return [body]


application = WebApp()
