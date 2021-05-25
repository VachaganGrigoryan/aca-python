from pathlib import Path
from typing import Iterable


def application(environ: dict, start_response: callable) -> Iterable:
    if environ['REQUEST_METHOD'] != 'GET':
        start_response(
            '405 Method Not Allowed',
            [
                ('Content-Type', 'text/html'),
                ('Cache-Control', 'no-store'),
            ]
        )
        return [b'<h1>405 Only "GET" HTTP method is allowed</h1>']
        
    root = Path('html')
    route = environ['PATH_INFO']

    # TODO: assert root path
    filepath = root / 'index.html' if route == '/' else root / route.lstrip('/')

    if filepath.suffix != '.html' or not filepath.is_file:
        start_response(
            '404 Not Found',
            [
                ('Content-Type', 'text/html'),
                ('Cache-Control', 'no-store'),
            ]
        )
        return [b'<h1>404 Nothing here</h1>']

    start_response(
        '200 OK',
        [
            ('Content-Type', 'text/html'),
            ('Cache-Control', 'no-store'),
        ]
    )
    with open(filepath, 'rb') as fd:
        return [fd.read()]
