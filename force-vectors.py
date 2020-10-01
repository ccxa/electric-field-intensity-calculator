from math import sqrt, degrees, acos, cos, sin, radians
import functions
import os
import ui


# q charges dictionary
charges = {}
# test charge: (intensity , x , y)
test_charge = [1, 0, 0]
# a place to store each vectors forces
vectors = {'i': [], 'j': []}
# store each charge force
forces = {}

# app main loop to handle main menu
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
        functions.run(vectors, forces, charges, sqrt, degrees,
                      acos, cos, sin, radians, ui, test_charge)
    elif cmd == "5":
        functions.show_list(ui, charges, forces)
    elif cmd == "6":
        functions.reset(ui, charges, vectors, forces, test_charge)
    elif cmd == "7":
        functions.help_message(ui)
    elif cmd == "8":
        os.system('clear')
        exit()
    else:
        print("Invalid Command")
