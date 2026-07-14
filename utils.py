from colorama import init, Fore, Style

init(autoreset=True)

def color_money(value):
    if value < 0:
        color = Fore.RED
    elif value > 0:
        color = Fore.GREEN
    else:
        color = Fore.YELLOW

    return f"{color}${value:.2f}"

def color_percent(value):
    if value < 0:
        color = Fore.RED
    elif value > 0:
        color = Fore.GREEN
    else:
        color = Fore.YELLOW

    return f"{color}{value:.2f}%"


def divider():
    return "=" * 35