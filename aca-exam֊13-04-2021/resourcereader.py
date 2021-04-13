from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError


class ResourceNotFoundError(Exception):

    def __init__(self, message: str):
        super().__init__(message)


class ResourceReader:

    def __init__(self, location: str):
        try:
            if location.split(':')[0] in ['http', 'https']:
                self.obj = urlopen(location)
            else:
                self.obj = open(Path(location), 'rb')
        except (URLError, FileNotFoundError):
            if __name__ == '__main__':
                exit(f'[ERROR] "{location}" not found')
            raise ResourceNotFoundError(location)

    def read(self):
        return self.obj.read().decode()

    def close(self):
        return self.obj.close()


def run():
    import argparse
    parser = argparse.ArgumentParser(description='Resource reader')
    parser.add_argument('location', type=str, help='path or URL address of the resource')
    args = parser.parse_args()

    res = ResourceReader(args.location)
    print(res.read())

    res.close()


if __name__ == '__main__':
    run()
