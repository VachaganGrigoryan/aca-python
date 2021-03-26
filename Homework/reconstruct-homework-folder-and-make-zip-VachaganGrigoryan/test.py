import os
import zipfile
from typing import Iterable


def read_folder(path, file_types=[], esc_list=[], user_name=''):

    for root, folders, files in os.walk(path):
        if user_name in root and all(name not in root for name in esc_list):
            for file in files:
                if file.split('.')[-1] in file_types:
                    yield os.path.join(root, file)


def process_tmps(paths: Iterable, zip_name):

    with zipfile.ZipFile(zip_name + '.zip', 'w') as zip_file:
        for file_name in paths:
            zip_file.write(os.path.abspath(file_name), )
