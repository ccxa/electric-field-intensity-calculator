class colorful_prints():
    def printg(text): print("\033[40m{}\033[00m".format(text))
    def printg2(text): print("\033[40m{}\033[00m".format(text), end='')
    def printm(text): print("\033[100m{}\033[00m".format(text))
    def printm2(text): print("\033[100m{}\033[00m".format(text), end='')
    def printr(text): print("\033[91m{}\033[00m".format(text))
    def printr2(text): print("\033[91m{}\033[00m".format(text), end='')
    def printb(text): print("\033[34m{}\033[00m".format(text))
    def printb2(text): print("\033[34m{}\033[00m".format(text), end='')
    def printy(text): print("\033[93m" + str(text) + "\033[" + str(40) + "m".format(text))
    def printy2(text): print("\033[93m{}\033[00m".format(text), end='')
    def printbl(text): print("\033[5m{}\033[00m".format(text))
    def printbl2(text): print("\033[5m{}\033[00m".format(text), end='')


class txt(): #-------------------- repetitive messages class

    def head(map):
        os.system('clear')
        clp.printb(map)
        print(61*'-')
    def invInput(errorHint):
        clp.printr('-------------------------------')
        print(errorHint)
        clp.printr2('>>')
        clp.printbl2(' Hit enter to try again')
        wait = input('')