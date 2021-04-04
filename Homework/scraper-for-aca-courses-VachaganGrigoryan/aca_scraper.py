
import json
import requests
from pathlib import Path
from bs4 import BeautifulSoup, SoupStrainer

import logging

logging.basicConfig(format="Datetime :: %(asctime)s %(message)s", level=logging.INFO)


class LookUpACACourses:

    def __init__(self, aca_url: str, local_path: str = './html'):
        self.url = aca_url
        self.local_path = local_path

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
                page = f'{self.url}{page}'
            yield self._get_(page)

    @staticmethod
    def _get_(page_url: str):
        logging.info(f'Getting the ACA {page_url} Course Page.')
        response = requests.get(page_url)
        if response.status_code != 200:
            logging.warning(f'Request failed: [{response.status_code}]')

        return response.url, response.content

    def save_as_html(self, path: str = None):
        path = path or self.local_path
        Path(path).mkdir(exist_ok=True)
        for url, content in self:
            self.write_file(url, content, path)

    def write_file(self, url, content, path):
        name = url.replace(self.url, '').replace('/', '__')
        logging.info(f'Saved the {name} file!')
        with open(Path(f'{path}/{name}'), 'wb') as html_file:
            html_file.write(content)

    def read_files(self, path: str = None):
        path = path or self.local_path
        for entry in Path(path).iterdir():
            if not entry.is_dir():
                logging.info(f'Reading the {entry} file!')
                with open(entry, encoding='utf-8') as file:
                    yield entry, file.read()

    def get_parsed_data(self, url: str, content: str):
        data = {
            'course_id': url.replace(self.url, '').split('.')[0],
            'course_url': url
        }

        soup = BeautifulSoup(content, 'html.parser')
        try:
            data['course_name'] = soup.find('h1').text.strip()
            details = soup.find('div', attrs={'id': 'details'})
            for row in details.find_all('tr'):
                rows = row.find_all('td')
                try:
                    data[rows[1].text.strip().lower()] = rows[2].text.strip()
                except:
                    pass

            teachers = soup.find('div', attrs={'id': 'tutors'})
            text = list(teachers.find('div').stripped_strings)
            data['teachers'] = [
                {
                    'full_name': text[i],
                    'company': text[i + 1]
                } for i in range(0, len(text), 2)
            ]
        except:
            pass

        return data

    def get_data(self, local=False, path: str = None):
        aca_lessons = []
        path = path or self.local_path
        local_dir = Path(path)
        if local and local_dir.exists():
            for page, content in self.read_files(path):
                url = f'{self.url}{page.name.replace("__", "/")}'
                aca_lessons.append(self.get_parsed_data(url, content))

                self.courses_link = [k for k in self.courses_link if k
                                     and not (k.endswith(page.name) or page.name.replace("__", "") in k)]
        if not local_dir.exists():
            local_dir.mkdir()

        for url, content in self:
            self.write_file(url, content, path)
            aca_lessons.append(self.get_parsed_data(url, str(content, encoding='utf-8')))

        return aca_lessons


def run():
    ACA_URL = 'https://aca.am/en/'
    look_up = LookUpACACourses(ACA_URL)
    # look_up.save_as_html('./html')
    data = look_up.get_data(local=True)

    with open(Path('data.json'), 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(data, indent=4, ensure_ascii=False))

    print(json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    run()
