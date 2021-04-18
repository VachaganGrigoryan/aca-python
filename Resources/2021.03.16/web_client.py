from urllib.parse import urlparse, parse_qs, urlencode
from urllib.request import urlopen, Request

from html.parser import HTMLParser


class CustomHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag, "with attributes", attrs)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


def url_handling():
    url: str = 'https://aca.am/hy/'
    parsed_url = urlparse(url)
    print(parsed_url)
    print(parse_qs(parsed_url.query))

    new_query = {
        'target': '_blank',
        'page': 12,
        'limit': 10,
        'percentage': '100%',
        'lang': 'hy'
    }
    print(urlencode(new_query))


def url_request():
    # response = urlopen('https://aca.am/hy/')
    # response.close()

    request = Request(
        'https://auto.am/',
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        }
    )
    with urlopen('https://aca.am/hy/') as response:
    # with urlopen(request) as response:
        print(response.headers)
        print('>>>', response.headers['Content-Type'])
        binary_html = response.read()

    with open('aca.html', 'wb') as fd:
        fd.write(binary_html)

    html_parser = CustomHTMLParser()
    html_parser.feed(binary_html.decode())

    
if __name__ == '__main__':
    url_request()
