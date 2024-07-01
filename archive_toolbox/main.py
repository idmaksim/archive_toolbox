import argparse

from archive_toolbox.logic import extract_archive, show_info
from archive_toolbox.utils import SUPPORTED_TYPES, check_correct_type, show_logo


def main():
    show_logo('Archive toolbox')
    
    parser = argparse.ArgumentParser(description='Archive toolbox')
    parser.add_argument('--extract', action='store_true', help='Extract the specified file')
    parser.add_argument('--info', action='store_true', help='Show info about the specified file')
    parser.add_argument('--filename', type=str, help='The archive file to process')

    args = parser.parse_args()

    try:
        
        if args.filename:
            if not check_correct_type(args.filename):
                raise Exception(f"Unsupported file type. Only {SUPPORTED_TYPES} are supported.")
            
            # extract archive        
            elif args.extract:
                extract_archive(args.filename)

            # show info
            elif args.info:
                show_info(args.filename)
            
        else:
            parser.print_help()
            
    except Exception as e:
        show_logo('ERROR')
        print(e)

if __name__ == '__main__':
    main()