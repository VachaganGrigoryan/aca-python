from pathlib import Path

import requests
from bs4 import BeautifulSoup, SoupStrainer

import logging

logging.basicConfig(format="Datetime :: %(asctime)s %(message)s", level=logging.INFO)


class LookUpACACourses:

    def __init__(self, aca_url: str):
        self.url = aca_url

        logging.info(f'Getting the ACA Home Page: {aca_url}.')
        response = requests.get(aca_url)
        if response.status_code != 200:
            logging.warning(f'Request failed: [{response.status_code}]')
            exit(1)
        strainer = SoupStrainer(name='div', attrs={'id': 'courses'})
        soup = BeautifulSoup(response.text, 'html.parser', parse_only=strainer)

        self.courses_link = [link.get('href') for link in soup.div.find_all('a')]

    def __iter__(self):

        for page in self.courses_link:
            if not page:
                continue
            if not page.startswith(self.url):
                page = f'{self.url}/{page}'
            yield self.get__(page)

    @staticmethod
    def get__(page_url: str):
        logging.info(f'Getting the ACA {page_url} Course Page.')
        response = requests.get(page_url)
        if response.status_code != 200:
            logging.warning(f'Request failed: [{response.status_code}]')

        return page_url, response.content

    def save_as_html(self, path):
        Path(path).mkdir(exist_ok=True)
        for url, content in self:
            name = url.replace(self.url, '').replace('/', '_').replace('..', '').replace('.', '-')
            logging.info(f'Getting the ACA {name} Course Page.')
            with open(Path(f'{path}/{name}.html'), 'wb') as html_file:
                html_file.write(content)


def read_files(path: str):
    for entry in Path(path).iterdir():
        print(entry)
        if entry.is_dir():
            read_files(f'{path}/{entry}')

        with open(entry) as file:
            yield file.read()



def get_parsed_data():
    pass



if __name__ == '__main__':
    # ACA_URL = 'https://aca.am/en'
    # look_up = LookUpACACourses(ACA_URL)
    # look_up.save_as_html('./html')
    for page in read_files('./html'):
        print(page)


