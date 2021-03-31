from xml.etree import ElementTree as ET
from argparse import ArgumentParser
import requests


class Parser:
    def __init__(self):
        self._arguments = self.__parse_arguments()

    def __parse_arguments(self):
        argparser = ArgumentParser(description="Reddit RSS Client")
        argparser.add_argument("sub", type=str, help="subreddit")
        args = argparser.parse_args()
        return {'sub': args.sub}

    def get_argument(self, arg):
        return self._arguments[arg]


class Scrapper:
    def __init__(self, sub, out_file='rss.xml'):
        self._file = out_file
        self._url = f"https://www.reddit.com/r/{sub}/.rss"

    def extract(self):
        response = requests.get(self._url)
        raw_xml = response.text
        with open(self._file, 'w') as rss:
            rss.write(raw_xml)

    @property
    def file(self):
        return self._file


class Formatter:
    def __init__(self, in_file):
        self._source = in_file

    def show_feeds(self):
        root = ET.parse('rss.xml').getroot()
        entry_tag = '{http://www.w3.org/2005/Atom}entry'
        for i, feed in enumerate(root.findall(entry_tag)):
            title = link = author = updated = ''
            for child in feed:
                if 'author' in child.tag:
                    author = child[0].text
                elif 'link' in child.tag:
                    link = child.attrib['href']
                elif 'title' in child.tag:
                    title = child.text
                elif 'updated' in child.tag:
                    updated = child.text
            print("{:<5}".format(f"{i + 1}."), title)
            print("     ", "-" * len(title))
            print(f"      {link}")
            print(f"      Author: {author}   Updated: {updated}")
            print()


def main():
    parser = Parser()
    sub = parser.get_argument('sub')
    scrapper = Scrapper(sub)
    scrapper.extract()
    formatter = Formatter(scrapper.file)
    formatter.show_feeds()


if __name__ == "__main__":
    main()
