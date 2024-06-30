import pyfiglet


SUPPORTED_TYPES = {
    'tar.bz2',
    'tar.gz', 
    'tgz',
    'tar',
    'tar.xz',
    'zip'
}

def check_correct_type(filename):
    return filename.endswith(tuple(SUPPORTED_TYPES))
        


def show_logo(logo_text: str):
    banner = pyfiglet.figlet_format(text=logo_text)
    print(banner)