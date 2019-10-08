import os


def colored_print(text, color):
    if color == 'printg':
        print("\033[40m{}\033[00m".format(text))
    elif color == 'printg2':
        print("\033[40m{}\033[00m".format(text), end='')
    elif color == 'printm':
        print("\033[100m{}\033[00m".format(text))
    elif color == 'printm2':
        print("\033[100m{}\033[00m".format(text), end='')
    elif color == 'printr':
        print("\033[91m{}\033[00m".format(text))
    elif color == 'printr2':
        print("\033[91m{}\033[00m".format(text), end='')
    elif color == 'printb':
        print("\033[34m{}\033[00m".format(text))
    elif color == 'printb2':
        print("\033[34m{}\033[00m".format(text), end='')
    elif color == 'printy':
        print("\033[93m" + str(text) + "\033[" + str(40) + "m".format(text))
    elif color == 'printy2':
        print("\033[93m{}\033[00m".format(text), end='')
    elif color == 'printbl':
        print("\033[5m{}\033[00m".format(text))
    elif color == 'printbl2':
        print("\033[5m{}\033[00m".format(text), end='')




class txt():  # -------------------- repetitive messages class

    def head(map):
        os.system('clear')

        colored_print(map, 'printb')
        print(61*'-')
    def invInput(errorHint):
        colored_print('-------------------------------', 'printr')
        print(errorHint)
        colored_print('>>', 'printr2')
        colored_print(' Hit enter to try again', 'printbl2')
        wait = input('')