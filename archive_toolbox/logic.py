import os
import shutil

from utils import check_double_point_type


def extract_archive(filename: str) -> None:
    archive_name = os.path.splitext(filename)[0]

    if check_double_point_type(filename):
        archive_name = os.path.splitext(archive_name)[0]
    
    if not os.path.exists(archive_name):
        os.mkdir(archive_name)

    shutil.unpack_archive(filename, archive_name)
    print(f"Extracted all files from {filename} to {archive_name}")