import os
import tarfile
from zipfile import ZipFile

from archive_toolbox.utils import check_double_point_type, is_zip


def extract_archive(filename: str) -> None:
    archive_name = os.path.splitext(filename)[0]

    if check_double_point_type(filename):
        archive_name = os.path.splitext(archive_name)[0]
    
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


def create_tar_file(filename: str) -> None:
    with tarfile.open(filename, 'w') as tar:
        tar.add(filename)
    print(f"Created tar file {filename}")
