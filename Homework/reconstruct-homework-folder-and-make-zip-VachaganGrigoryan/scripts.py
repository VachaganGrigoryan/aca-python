import zipfile
import tempfile
from pathlib import Path


def reconstruct_folder_and_make_zip(path: str, file_types: list, esc_dir: list):
    def walk(path: str, new_zip: zipfile.ZipFile, tmp_root: str):
        entries = Path(path)
        for entry in entries.iterdir():
            if entry.name not in esc_dir:
                if entry.is_dir():
                    tmp_dir = f"{tmp_root}/{entry.name.rstrip('-VachaganGrigoryan')}"
                    Path(tmp_dir).mkdir()
                    walk(f'{path}/{entry.name}', new_zip, tmp_dir)

                if entry.name.split('.')[-1] in file_types:
                    with open(f'{tmp_root}/{entry.name}', 'wb+') as tmp_file:
                        with open(entry, 'rb') as py_file:
                            tmp_file.write(py_file.read())
                    new_zip.write(f'{tmp_root}/{entry.name}')

    with zipfile.ZipFile('./homework.zip', 'w') as new_zip:
        with tempfile.TemporaryDirectory(dir='./', prefix='homework_') as tmp_root:
            esc_dir.append(tmp_root.lstrip('./'))
            walk(path, new_zip, tmp_root)


if __name__ == '__main__':
    path = './..'
    file_types = ['py']
    esc_dir = ['.git', '.vscode', '.idea', 'venv', '__pycache__']

    reconstruct_folder_and_make_zip(path, file_types, esc_dir)
