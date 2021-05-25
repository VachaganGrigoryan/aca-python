from importlib import import_module
from configparser import ConfigParser
from wsgiref.simple_server import make_server


if __name__ == '__main__':
    config = ConfigParser()
    config.read('config.ini')

    ip = config.get('server', 'ip') or ''
    port = config.getint('server', 'port', fallback=8000)
    wsgi_app = config['server']['application']

    # TODO: implement proper validation of WSGI callable configuration
    module, app = wsgi_app.split('.')
    wsgi_application = getattr(import_module(module), app)

    try:
        with make_server(ip, port, wsgi_application) as httpd:
            print('Starting WSGI server on', ip, ':', port, 'address')
            httpd.serve_forever()
    except KeyboardInterrupt:
        print('Stopping web server.....Have a nice day!')
