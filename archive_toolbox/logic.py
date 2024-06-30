import os
import shutil


def extract_archive(filename: str) -> None:
    archive_name = os.path.splitext(filename)[0]
    if filename.endswith(".tar.gz"):
        archive_name = os.path.splitext(archive_name)[0]

    if not os.path.exists(archive_name):
        os.mkdir(archive_name)

    shutil.unpack_archive(filename, archive_name)
    print(f"Extracted all files from {filename} to {archive_name}")



# def extract_archive(filename: str, archive_type: Union[ZipFile]) -> None:
#     archive_name = os.path.splitext(filename)[0]
#     if not os.path.exists(archive_name):
#         os.mkdir(archive_name)
    
#     with archive_type(filename) as archive:
#         archive: Union[ZipFile]

#         for file in archive.namelist():
#             archive.extract(file, path=archive_name)
#             print(f"[+] File '{file}' extracted from '{filename}' to '{archive_name}'")
#         print(f"[!] Extracted all files from '{filename}' to '{archive_name}'")