import os
from math import sqrt, degrees, acos, cos, sin, radians
import ui
import functions

# Dicts
charges = {}
tcharge = [1, 0, 0]  # test charges primary intensity , x , y
vectors = {'i': [], 'j': []}
forces = {}  # a place to store each vectors forces
# Add Charge



#------------------------------------------------------------------------------- Rem Charge
def remCharge():

    removeState = False
    while removeState == False:
        ui.header('Input name :')
        print('Input charge name to remove, input other than number = ',end='')
        ui.colored_print('cancel', 'red')
        try:
            number = int(input('>> q'))
            name = 'q'+str(number)
            if name not in charges:
                ui.invalid_input('This charge dos not exist')
            else:
                del charges[name]
                ui.header('Input name > Done!')
                print(name,end='')
                ui.colored_print(' removed from memory.\n', 'blue')
                ui.colored_print('>>', 'red2')
                ui.colored_print(' Hit enter to open menu', 'blinking')
                wait = input('')
                removeState = True
        except ValueError:
            return None
    vectors['i'],vectors['j']=[],[]
#------------------------------------------------------------------------------- Test Charge
def testCharge():
    ui.header('Test charge options :')
    ui.colored_print('Current values -> ', 'blue2')
    print('Tq(',tcharge[1],',',tcharge[2],')= ',tcharge[0],'MC\n',sep='')
    ui.colored_print('>>', 'red2')
    answer = input(' 1.Change-it  2.Go-back [1/2]: ')
    if answer =='1':
        ui.header('Test charge options > Reseting values :')
        ui.colored_print('Defaults: ', 'red2')
        print('intensity: +1MC    x,y: 0,0    distanse scale: CM\n')

        intensityState = False #------------------------------ intensity
        while intensityState == False:
            ui.header('Test charge options > Reseting values :')
            ui.colored_print('Defaults: ', 'red2')
            print('intensity: +1MC    x,y: 0,0    distanse scale: CM\n')
            try:
                intensity = int(input('Intensity, can be + / - :\n>> q(MC): '))
                if intensity ==0:
                    ui.invalid_input('It cant be: 0')
                else:
                    intensityState = True
            except ValueError:
                ui.invalid_input('Input integer only')
    else:
        return None

    positionState = False #------------------------------ position
    while positionState == False:
        ui.header('Test charge options > Reseting values :')
        ui.colored_print('Defaults: ', 'red2')
        print('intensity: 1MC    x,y: 0,0    distanse scale: CM\n')
        try:
            print('Now set its position(C.Meter).')
            x = int(input('x: '))
            y = int(input('y: '))
            positionState = True
        except ValueError:
            ui.invalid_input('Input integer only')

    #------------------------------ save data to tCharge list
    tcharge[0] = intensity
    tcharge[1] = x
    tcharge[2] = y

    #------------------------------ success message
    ui.header('Test charge options > Reseting values :')
    print('Old data replaced with Tq','(',x,',',y,')= ',intensity,'\n',sep='')
    ui.colored_print('>>', 'red2')
    ui.colored_print(' Hit enter to go menu', 'blinking')
    wait = input('')
#------------------------------------------------------------------------------- Run
def run():
                                    #--------- free memory to calculation
    vectors['i'],vectors['j'] = [],[]
    forces.clear()

    for charge in charges.keys():

        x,y = charges[charge][1],charges[charge][2] # (x,y) of charge
        q,tc = charges[charge][0],tcharge[0] # charge & testCharge

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
        tcharge[0],tcharge[1],tcharge[2] = 1,0,0
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
        remCharge()
    elif cmd == "3":
        testCharge()
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
