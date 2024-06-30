import pyfiglet


SUPPORTED_TYPES = [
    'tar.bz2',
    'tar.xz',
    'tar.gz', 
    'tgz',
    'tar',
    'zip'
]

def check_correct_type(filename):
    return filename.endswith(tuple(SUPPORTED_TYPES))


def check_double_point_type(filename):
    return filename.endswith(tuple(SUPPORTED_TYPES[:4]))
        

def show_logo(logo_text: str):
    banner = pyfiglet.figlet_format(text=logo_text)
    print(banner)
