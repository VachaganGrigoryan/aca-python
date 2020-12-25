from pathlib import Path


def cat(filenames):
    for file in filenames:
        with open(file) as file:
            for line in file:
                yield line


def get_all_file_name(folder_name, files=[]):
    for file in folder_name.iterdir():
        if file.suffix == ".txt":
            files.append(file)
        elif file.is_dir():
            get_all_file_name(file, files)

    return files


def read_all_text_files(folder_name):
    folder_name = Path(folder_name)

    files = get_all_file_name(folder_name)

    with open(Path("./cat.txt"), "w") as file:
        for line in cat(files):
            file.write(line)


# read_all_text_files("./")


import os

def combine_all_texts():
    abs_path = os.getcwd()

    with open(os.path.join(abs_path, 'combine.txt'), 'w') as f:
        for root, directories, files in os.walk('.'):
            for file in files:
                if file.endswith('.txt'):
                    with open(os.path.join(abs_path, f'{root}/{file}')) as rf:
                        f.write(rf.read())


combine_all_texts()












