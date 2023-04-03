class Colors:
    RESET = "\033[0;0m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    BLUE = "\033[0;34m"
    MAGENTA = "\033[0;35m"
    CYAN = "\033[0;36m"
    WHITE = "\033[0;37m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    BOLD_CYAN = "\033[1;36m"
    BOLD_YELLOW = "\033[1;33m"
    PURPLE = "\033[38;5;128m"

def print_colored(text, color):
    print(f"{color}{text}{Colors.RESET}")