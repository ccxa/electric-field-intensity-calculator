import os


def colored_print(text, color):
    if color == 'red':
        print("\033[91m{}\033[00m".format(text))
    elif color == 'red2':
        print("\033[91m{}\033[00m".format(text), end='')
    elif color == 'blue':
        print("\033[34m{}\033[00m".format(text))
    elif color == 'blue2':
        print("\033[34m{}\033[00m".format(text), end='')
    elif color == 'blinking':
        print("\033[5m{}\033[00m".format(text), end='')


def header(header_text):
    os.system('clear')
    colored_print(header_text, 'blue')
    print(61*'-')


def invalid_input(error_hint):
    colored_print('-' * 31, 'red')
    print(error_hint)
    colored_print('>>', 'red2')
    colored_print(' Hit enter to try again', 'blinking')
    # simple way of waiting for user to press enter button
    input('')
