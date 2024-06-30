import argparse

from logic import extract_archive
from utils import SUPPORTED_TYPES, check_correct_type, show_logo


def main():
    show_logo('Archive toolbox')

    parser = argparse.ArgumentParser(description='Archive toolbox')
    parser.add_argument('--extract', action='store_true', help='Extract the specified file')
    parser.add_argument('--filename', type=str, help='The archive file to process')

    args = parser.parse_args()

    try:
        if args.extract and args.filename:
            if not check_correct_type(args.filename):
                raise Exception(f"Unsupported file type. Only {SUPPORTED_TYPES} are supported.")    
            extract_archive(args.filename)
            
    except Exception as e:
        show_logo('ERROR')
        print(e)

main()