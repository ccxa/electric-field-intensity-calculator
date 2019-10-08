import os
from math import sqrt, degrees, acos, cos, sin, radians
import ui

# ui related functions
#clp = ui.colorful_prints
txt = ui.txt

# Menu
def menu():
    number = [0,1,2,3,4,5,6,7]
    item = ['Add','Remove','TestCharge','Run','Charges','Reset','Help','Exit']
    ui.colored_print('1.Add    2.Remove    3.TestCharge ', 'printb')
    ui.colored_print('4.Run    5.Charges   6.Reset      ', 'printb')
    ui.colored_print('7.Help   8.Exit                   ', 'printb')
#------------------------------------------------------------------------------- Dicts
charges = {}
tcharge = [1,0,0] #test charges primary intensity , x , y
vectors = {'i':[],'j':[]}
forces = {} # a place to store each vectors forces
#------------------------------------------------------------------------------- Add Charge
def addCharge():

    nameState = False #------------------------------ set name
    while nameState == False:
        txt.head('Set name :')
        print('Assign a number to q charge, input other than number = ',end='')
        ui.colored_print('cancel', 'printr')
        try :
            number = int(input('>> q'))
            name = 'q'+str(number)
            if name in charges:
                errorHint = name + ' charge name already exist!'
                txt.invInput(errorHint)
            else:
                nameState = True
        except ValueError:
            return None

    intensityState = False #------------------------------ intensity
    while intensityState == False:
        txt.head('Setting name > Intensity :')
        print('set intensity, it can be + / - :')
        try:
            intensity = int(input('>> q(MC): '))
            intensityState = True
        except ValueError:
            txt.invInput('Input integer only')

    positionState = False #------------------------------ position
    while positionState == False:
        txt.head('Setting name > Intensity > Position :')
        print('Define its position in (x,y) format, Scale is CM')
        try:
            x = int(input('x = '))
            y = int(input('y = '))
            positionState = True
        except ValueError:
            txt.invInput('Input integer only.')

    #------------------------------ success message
    txt.head('Setting name > Intensity > Position > Done!')
    ui.colored_print('added successfully: ', 'printb2')
    print(name,'(',x,',',y,')= ',intensity,' Coulomb\n',sep='')
    ui.colored_print('>>', 'printr2')
    ui.colored_print(' Hit enter to go menu', 'printbl2')
    wait = input('')
    #------------------------------ put info to charges
    charges[name] = [intensity,x,y]
#------------------------------------------------------------------------------- Rem Charge
def remCharge():

    removeState = False
    while removeState == False:
        txt.head('Input name :')
        print('Input charge name to remove, input other than number = ',end='')
        ui.colored_print('cancel', 'printr')
        try:
            number = int(input('>> q'))
            name = 'q'+str(number)
            if name not in charges:
                txt.invInput('This charge dos not exist')
            else:
                del charges[name]
                txt.head('Input name > Done!')
                print(name,end='')
                ui.colored_print(' removed from memory.\n', 'printb')
                ui.colored_print('>>', 'printr2')
                ui.colored_print(' Hit enter to open menu', 'printbl2')
                wait = input('')
                removeState = True
        except ValueError:
            return None
    vectors['i'],vectors['j']=[],[]
#------------------------------------------------------------------------------- Test Charge
def testCharge():
    txt.head('Test charge options :')
    ui.colored_print('Current values -> ', 'printb2')
    print('Tq(',tcharge[1],',',tcharge[2],')= ',tcharge[0],'MC\n',sep='')
    ui.colored_print('>>', 'printr2')
    answer = input(' 1.Change-it  2.Go-back [1/2]: ')
    if answer =='1':
        txt.head('Test charge options > Reseting values :')
        ui.colored_print('Defaults: ', 'printr2')
        print('intensity: +1MC    x,y: 0,0    distanse scale: CM\n')

        intensityState = False #------------------------------ intensity
        while intensityState == False:
            txt.head('Test charge options > Reseting values :')
            ui.colored_print('Defaults: ', 'printr2')
            print('intensity: +1MC    x,y: 0,0    distanse scale: CM\n')
            try:
                intensity = int(input('Intensity, can be + / - :\n>> q(MC): '))
                if intensity ==0:
                    txt.invInput('It cant be: 0')
                else:
                    intensityState = True
            except ValueError:
                txt.invInput('Input integer only')
    else:
        return None

    positionState = False #------------------------------ position
    while positionState == False:
        txt.head('Test charge options > Reseting values :')
        ui.colored_print('Defaults: ', 'printr2')
        print('intensity: 1MC    x,y: 0,0    distanse scale: CM\n')
        try:
            print('Now set its position(C.Meter).')
            x = int(input('x: '))
            y = int(input('y: '))
            positionState = True
        except ValueError:
            txt.invInput('Input integer only')

    #------------------------------ save data to tCharge list
    tcharge[0] = intensity
    tcharge[1] = x
    tcharge[2] = y

    #------------------------------ success message
    txt.head('Test charge options > Reseting values :')
    print('Old data replaced with Tq','(',x,',',y,')= ',intensity,'\n',sep='')
    ui.colored_print('>>', 'printr2')
    ui.colored_print(' Hit enter to go menu', 'printbl2')
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
    txt.head('Run > Resualts :')
    ui.colored_print('Total Force vector: ', 'printb2')
    print(i_total,'i',sep='',end='')
    ui.colored_print(' + ', 'printb2')
    print(j_total,'j',sep='')
    ui.colored_print('Total Electricity Field Intensity : ', 'printb2')
    print(total,end='')
    ui.colored_print(' N\n', 'printb')
    ui.colored_print('>> ', 'printr2')
    ui.colored_print('Press any key to go menu', 'printbl2')
    wait = input('')
#------------------------------------------------------------------------------- help
def help():
    txt.head('Help :')
    print('''First import your charges with them details.
then set TestCharge's intensity and its position.
at last hit the 'Run' to calculate imported data.
also you can monitor current imported data by selecting item '5'.
    ''')
    ui.colored_print('[Github]: github.com/ccxa\n', 'printb')
    ui.colored_print('>> ', 'printr2')
    ui.colored_print('Hit enter to go menu', 'printbl2')
    wait = input('')
#------------------------------------------------------------------------------- show list
def showList():
    txt.head('Show list > Current Data :')
    ui.colored_print('| {0:^7s}|{1:^7s}|{2:^7s}|{3:^7s}|{4:^11s}|'
    .format('Charge','x','y','MC','Force'), 'printr')
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
    ui.colored_print('\n', 'printb')
    ui.colored_print('>> ', 'printr2')
    ui.colored_print('Press any key to go menu', 'printbl2')
    wait = input('')
#------------------------------------------------------------------------------- Reset
def reset():
    txt.head('Reset :')
    answer = input('Erase all imported data from memory? [y/n]\n>> ')
    if answer in ['y','Y']:
        charges.clear()
        tcharge[0],tcharge[1],tcharge[2] = 1,0,0
        vectors['i'].clear()
        vectors['j'].clear()
        forces.clear()
        ui.colored_print('All data has been reset to default values.', 'printr')
        ui.colored_print('>> ', 'printr2')
        ui.colored_print('Hit enter to go menu.', 'printbl2')
        wait = input('')
    else:
        return None
#------------------------------------------------------------------------------- Execute
while True:
    os.system('clear')
    menu()
    cmd = input(">> ")
    if cmd == "1":
        addCharge()
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
