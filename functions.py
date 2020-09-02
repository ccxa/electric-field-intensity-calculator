def menu(ui):
    ui.colored_print('1.Add    2.Remove    3.TestCharge ', 'blue')
    ui.colored_print('4.Run    5.Charges   6.Reset      ', 'blue')
    ui.colored_print('7.Help   8.Exit                   ', 'blue')


def add_charge(ui, charges):

    # init variables to avoid any warnings ^^
    x, y, name, intensity = None, None, None, None

    # set name
    name_state = False
    while not name_state:
        ui.header('Set name :')
        print('Assign a number to name q charge, (integer only) = ', end='')
        ui.colored_print('cancel', 'red')
        try:
            number = int(input('>> q'))
            name = 'q'+str(number)
            if name in charges:
                error_hint = name + ' charge name already exist!'
                ui.invalid_input(error_hint)
            else:
                name_state = True
        except ValueError:
            ui.invalid_input("Input only integer!")
            return None

    # intensity
    intensity_state = False
    while not intensity_state:
        ui.header('Setting name > Intensity :')
        print('set intensity, it can be + / - :')
        try:
            intensity = int(input('>> q(MC): '))
            intensity_state = True
        except ValueError:
            ui.invalid_input('Input integer only')

    # position
    position_state = False
    while not position_state:
        ui.header('Setting name > Intensity > Position :')
        print('Define its position in (x,y) format, Scale is CM')
        try:
            x = int(input('x = '))
            y = int(input('y = '))
            position_state = True
        except ValueError:
            ui.invalid_input('Input integer only.')

    # success message
    ui.header('Setting name > Intensity > Position > Done!')
    ui.colored_print('added successfully: ', 'blue2')
    print(name, '(', x, ',', y, ')= ', intensity, ' Coulomb\n', sep='')
    ui.colored_print('>>', 'red2')
    ui.colored_print(' Hit enter to go menu', 'blinking')

    input('')
    # put info to charges
    charges[name] = [intensity, x, y]


def remove_charge(ui, charges, vectors):

    remove_state = False
    while not remove_state:
        ui.header('Input name :')
        print('Input charges number to remove it, (integer only)  = ', end='')
        ui.colored_print('cancel', 'red')

        try:
            number = int(input('>> q'))
            name = 'q'+str(number)
            if name not in charges:
                ui.invalid_input('This charge dos not exist')
            else:
                del charges[name]
                ui.header('Input name > Done!')
                print(name, end='')
                ui.colored_print(' removed from memory.\n', 'blue')
                ui.colored_print('>>', 'red2')
                ui.colored_print(' Hit enter to open menu', 'blinking')
                input('')
                remove_state = True
        except ValueError:
            return None

    vectors['i'], vectors['j'] = [], []


def test_charge(ui, t_charge):

    ui.header('Test charge options :')
    ui.colored_print('Current values -> ', 'blue2')
    print('Tq(', t_charge[1], ',', t_charge[2], ')= ', t_charge[0], 'MC\n', sep='')
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

    #------------------------------ save data to t_charge list
    t_charge[0] = intensity
    t_charge[1] = x
    t_charge[2] = y

    #------------------------------ success message
    ui.header('Test charge options > Reseting values :')
    print('Old data replaced with Tq','(',x,',',y,')= ',intensity,'\n',sep='')
    ui.colored_print('>>', 'red2')
    ui.colored_print(' Hit enter to go menu', 'blinking')
    wait = input('')