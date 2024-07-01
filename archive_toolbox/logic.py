import datetime
import os
import tarfile
from zipfile import ZipFile

from archive_toolbox.utils import get_archive_name, is_zip


def extract_archive(filename: str) -> None:
    archive_name = get_archive_name(filename)
    
    if not os.path.exists(archive_name):
        os.mkdir(archive_name)

    if is_zip(filename):
        with ZipFile(filename) as archive:
            for file in archive.namelist():
                print(f'[+] Extracting {file} from {filename}')
                archive.extract(file, archive_name)
    else:
        with tarfile.open(filename) as archive:
            for file in archive.getmembers():
                print(f'[+] Extracting {file.name} from {filename}')
                archive.extract(file, archive_name)

    print(f"Extracted all files from {filename} to {archive_name}")


def show_info_zip(filename: str):
    with ZipFile(filename) as archive:
        for file in  archive.filelist:
            print(f'[+] File {file.filename}')
            print(f'\t- Size {file.file_size}')
            print(f'\t- Created at {file.date_time[:3]}')
            print(f'\t- Compress size {file.compress_size}')

def show_info_tar(filename: str):
    with tarfile.open(filename) as archive:
        for file in archive.getmembers():
            print(f'[+] File {file.name}')
            print(f'\t- Size {file.size}')


def show_info(filename: str):
    if is_zip(filename):
        show_info_zip(filename)
    else:
        show_info_tar(filename)
