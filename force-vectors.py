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



#------------------------------------------------------------------------------- Run
def run():
                                    #--------- free memory to calculation
    vectors['i'],vectors['j'] = [],[]
    forces.clear()

    for charge in charges.keys():

        x,y = charges[charge][1],charges[charge][2] # (x,y) of charge
        q,tc = charges[charge][0],test_charge[0] # charge & testCharge

                                    #----------------------- calculate Force
        q = q * 0.000001
        tc = tc * 0.000001
        distanse = (sqrt( (x**2) + (y**2) )) * 0.01 # between q & tc
        k = (9 * (10**9)) # constant value in physics formula
        force = (round((k * ( q * tc )) / (distanse ** 2))) * 0.1
                                    #------------ (i,j) of this force vector
        if (q < 0 and tc < 0) or (q > 0 and tc > 0) :
            i,j = -x,-y
        else:
            i,j = x,y
                                    #------------------- degree force vector
        degree =  (( (i*5)+(j*0) ) / (distanse * 5) ) / 100
        degree = round(degrees(acos(degree)))
        if 180 > degree > 90:
            degree = 180 - degree
        elif degree == 180:
            degree = 0
                                    #------------------------ F >>> Fy & Fx
        if degree == 0:
            fx,fy = force * (i/abs(i)),0

        elif degree == 90:
            fy,fx = force * (j/abs(j)),0
        else:
            fx = force * cos(radians(degree)) * (i/abs(i))
            fy = force * sin(radians(degree)) * (j/abs(j))
                                    #------------------------- save to dict
        vectors['i'].append((fx))
        vectors['j'].append((fy))
        forces[charge] = force
                                    #---- final calculate and show resualts
    i_total = sum(vectors['i'])
    j_total = sum(vectors['j'])
    total = sqrt( (i_total**2) + (j_total**2) )
    ui.header('Run > Resualts :')
    ui.colored_print('Total Force vector: ', 'blue2')
    print(i_total,'i',sep='',end='')
    ui.colored_print(' + ', 'blue2')
    print(j_total,'j',sep='')
    ui.colored_print('Total Electricity Field Intensity : ', 'blue2')
    print(total,end='')
    ui.colored_print(' N\n', 'blue')
    ui.colored_print('>> ', 'red2')
    ui.colored_print('Press any key to go menu', 'blinking')
    wait = input('')
#------------------------------------------------------------------------------- help
def help():
    ui.header('Help :')
    print('''First import your charges with them details.
then set TestCharge's intensity and its position.
at last hit the 'Run' to calculate imported data.
also you can monitor current imported data by selecting item '5'.
    ''')
    ui.colored_print('[Github]: github.com/ccxa\n', 'blue')
    ui.colored_print('>> ', 'red2')
    ui.colored_print('Hit enter to go menu', 'blinking')
    wait = input('')
#------------------------------------------------------------------------------- show list
def showList():
    ui.header('Show list > Current Data :')
    ui.colored_print('| {0:^7s}|{1:^7s}|{2:^7s}|{3:^7s}|{4:^11s}|'
    .format('Charge','x','y','MC','Force'), 'red')
    for charge in charges:
        name = charge
        x,y = charges[charge][1],charges[charge][2]
        intensity = int((charges[charge][0]))
        try:
            force = forces[charge]
        except KeyError:
            force = '---'
        print('| {0:^7s}|{1:^7d}|{2:^7d}|{3:^7d}|{4:^11}|'
        .format(name,x,y,intensity,force))
    ui.colored_print('\n', 'blue')
    ui.colored_print('>> ', 'red2')
    ui.colored_print('Press any key to go menu', 'blinking')
    wait = input('')
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
        run()
    elif cmd == "5":
        showList()
    elif cmd == "6":
        reset()
    elif cmd == "7":
        help()
    elif cmd == "8":
        os.system('clear')
        exit()
    else:
        print("Invalid Command")
