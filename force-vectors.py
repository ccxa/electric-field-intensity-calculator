import os
from math import sqrt, degrees, acos, cos, sin, radians
import ui
import functions

# Dicts
charges = {}
test_charge = [1, 0, 0]  # test charges primary intensity , x , y
vectors = {'i': [], 'j': []}
forces = {}  # a place to store each vectors forces
# Add Charge



#------------------------------------------------------------------------------- Reset
def reset():
    ui.header('Reset :')
    answer = input('Erase all imported data from memory? [y/n]\n>> ')
    if answer in ['y','Y']:
        charges.clear()
        test_charge[0],test_charge[1],test_charge[2] = 1,0,0
        vectors['i'].clear()
        vectors['j'].clear()
        forces.clear()
        ui.colored_print('All data has been reset to default values.', 'red')
        ui.colored_print('>> ', 'red2')
        ui.colored_print('Hit enter to go menu.', 'blinking')
        wait = input('')
    else:
        return None
#------------------------------------------------------------------------------- Execute
while True:
    os.system('clear')
    functions.menu(ui)
    cmd = input(">> ")
    if cmd == "1":
        functions.add_charge(ui, charges)
    elif cmd == "2":
        functions.remove_charge(ui, charges, vectors)
    elif cmd == "3":
        functions.test_charge(ui, test_charge)
    elif cmd == "4":
        functions.run(vectors, forces, charges, sqrt, degrees, acos, cos, sin, radians, ui, test_charge)
    elif cmd == "5":
        functions.show_list(ui, charges, forces)
    elif cmd == "6":
        reset()
    elif cmd == "7":
        functions.help_message(ui)
    elif cmd == "8":
        os.system('clear')
        exit()
    else:
        print("Invalid Command")
