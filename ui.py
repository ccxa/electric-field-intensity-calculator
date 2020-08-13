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


def head(map):
    os.system('clear')
    colored_print(map, 'blue')
    print(61*'-')


def invInput(errorHint):
    colored_print('-' * 31, 'red')
    print(errorHint)
    colored_print('>>', 'red2')
    colored_print(' Hit enter to try again', 'blinking')
    wait = input('')


