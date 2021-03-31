import argparse

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional

from urllib.request import urlopen, Request
from xml.etree.ElementTree import fromstring, parse

import logging

logging.basicConfig(format="Datetime :: %(asctime)s %(message)s", level=logging.INFO)


@dataclass
class Post:
    id: int
    title: str
    link: str
    author: str
    updated: datetime

    def __str__(self):
        return f'{self.id}.\t{self.title}\n\t{"-" * len(self.title)}\n\t{self.link}\n' \
               f'\tAuthor: {self.author} Updated: {self.updated}\n'


class XMLReader:

    def __init__(self, xml):
        self.root = fromstring(xml)
        self.namespace = 'http://www.w3.org/2005/Atom'

    def get_feed(self):
        entry_id = 1
        for entry in self.root.findall(self.tag('entry')):
            yield Post(
                id=entry_id,
                title=entry.find(self.tag('title')).text,
                link=entry.find(self.tag('link')).attrib.get('href'),
                author=entry.find(self.tag('author')).find(self.tag('name')).text,
                updated=entry.find(self.tag('updated')).text
            )
            entry_id += 1

    def tag(self, name):
        return f'{{http://www.w3.org/2005/Atom}}{name}'


class RedditRSSClient:

    def __init__(self):
        self.url = 'https://www.reddit.com/r/{}/.rss'

    def get_content(self, pattern: str, headers: Optional = None):
        xml_data = self._fetch_rss_of_(self.url.format(pattern), headers)
        e_tree = XMLReader(xml_data)

        return e_tree.get_feed()

    @staticmethod
    def _fetch_rss_of_(url: str, headers: Optional):
        logging.info(f'Getting: {url} !\n')
        request = Request(
            url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
            }
        )

        with urlopen(request) as response:
            return response.read().decode()

        # with open('python.xml', 'rb') as rss_file:
        #     return rss_file.read().decode()


def run():
    parser = argparse.ArgumentParser(description='Reddit RSS Client')
    parser.add_argument('sub', type=str, help='subreddit')
    args = parser.parse_args()

    rss_client = RedditRSSClient()

    feeds = rss_client.get_content(args.sub)

    for feed in feeds:
        print(feed)


if __name__ == '__main__':
    run()
