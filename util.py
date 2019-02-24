RED = '\033[0;31m'
DEFAULT = '\033[m'


def print_red(msg, end='\n', flush=False):
    print(RED + msg + DEFAULT, end=end, flush=flush)
