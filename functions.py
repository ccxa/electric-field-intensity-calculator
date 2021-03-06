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

    # init some vars to avoid warnings!
    x, y, intensity = None, None, None

    ui.header('Test charge options :')
    ui.colored_print('Current values -> ', 'blue2')
    print('Tq({},{})={}MC\n'.format(t_charge[1], t_charge[2], t_charge[0]),
          sep='')
    ui.colored_print('>>', 'red2')
    answer = input(' 1.Change-it  2.Go-back [1/2]: ')

    if answer == '1':
        ui.header('Test charge options > Resetting values :')
        ui.colored_print('Defaults: ', 'red2')
        print('intensity: +1MC    x,y: 0,0    distance scale: CM\n')

        # intensity
        intensity_state = False
        while not intensity_state:
            ui.header('Test charge options > Resetting values :')
            ui.colored_print('Defaults: ', 'red2')
            print('intensity: +1MC    x,y: 0,0    distance scale: CM\n')
            try:
                intensity = int(input('Intensity, can be + / - :\n>> q(MC): '))
                if intensity == 0:
                    ui.invalid_input('It cant be: 0')
                else:
                    intensity_state = True
            except ValueError:
                ui.invalid_input('Input integer only')
    else:
        return None

    # position
    position_state = False
    while not position_state:
        ui.header('Test charge options > Resetting values :')
        ui.colored_print('Defaults: ', 'red2')
        print('intensity: 1MC    x,y: 0,0    distance scale: CM\n')
        try:
            print('Now set its position(C.Meter).')
            x = int(input('x: '))
            y = int(input('y: '))
            position_state = True
        except ValueError:
            ui.invalid_input('Input integer only')

    # write data to t_charge list
    t_charge[0] = intensity
    t_charge[1] = x
    t_charge[2] = y

    # success message
    ui.header('Test charge options > Resetting values :')
    print('test charge updated >> Tq({},{})={}\n'.format(x, y, intensity),
          sep='')
    ui.colored_print('>>', 'red2')
    ui.colored_print(' Hit enter to go menu', 'blinking')
    input('')


def run(vectors, forces, charges, sqrt, degrees,
        a_cos, cos, sin, radians, ui, _test_charge
        ):

    # free memory to calculation
    vectors['i'], vectors['j'] = [], []
    forces.clear()

    for charge in charges.keys():

        # (x,y) of charge
        x, y = charges[charge][1], charges[charge][2]
        # Quantify charges and test charges values
        q = charges[charge][0]
        tc = _test_charge[0]

        # calculate Force
        q = q * 0.000001
        tc = tc * 0.000001

        # between q & tc
        distance = (sqrt((x**2) + (y**2))) * 0.01

        # constant value in physics formula
        k = (9 * (10**9))
        force = (round((k * (q * tc)) / (distance ** 2))) * 0.1

        # (i,j) of this force vector
        if (q < 0 and tc < 0) or (q > 0 and tc > 0):
            i, j = -x, -y
        else:
            i, j = x, y

        # degree force vector
        degree = (((i*5) + (j*0)) / (distance*5)) / 100
        degree = round(degrees(a_cos(degree)))
        if 180 > degree > 90:
            degree = 180 - degree
        elif degree == 180:
            degree = 0

        # separating F into Fx & Fy
        if degree == 0:
            fx, fy = force * (i/abs(i)), 0

        elif degree == 90:
            fy, fx = force * (j/abs(j)), 0
        else:
            fx = force * cos(radians(degree)) * (i/abs(i))
            fy = force * sin(radians(degree)) * (j/abs(j))

        # save to dict
        vectors['i'].append(fx)
        vectors['j'].append(fy)
        forces[charge] = force

    # final calculate and show results
    i_total = sum(vectors['i'])
    j_total = sum(vectors['j'])
    total = sqrt((i_total**2) + (j_total**2))
    ui.header('Run > Results :')
    ui.colored_print('Total Force vector: ', 'blue2')
    print(i_total, 'i', sep='', end='')
    ui.colored_print(' + ', 'blue2')
    print(j_total, 'j', sep='')
    ui.colored_print('Total Electricity Field Intensity : ', 'blue2')
    print(total, end='')
    ui.colored_print(' N\n', 'blue')
    ui.colored_print('>> ', 'red2')
    ui.colored_print('Press any key to go menu', 'blinking')
    input('')


def help_message(ui):
    ui.header('Help :')
    print('''Import charges with them details.
then set TestCharge's intensity and its position.
at last hit the 'Run' to calculate answer.
also you can monitor current imported data by selecting item '5'.
    ''')
    ui.colored_print('[Github]: github.com/ccxa\n', 'blue')
    ui.colored_print('>> ', 'red2')
    ui.colored_print('Hit enter to go menu', 'blinking')
    input('')


def show_list(ui, charges, forces):

    ui.header('Show list > Current Data :')
    ui.colored_print('| {0:^7s}|{1:^7s}|{2:^7s}|{3:^7s}|{4:^11s}|'
                     .format('Charge', 'x', 'y', 'MC', 'Force'), 'red')
    for charge in charges:
        name = charge
        x, y = charges[charge][1], charges[charge][2]
        intensity = int((charges[charge][0]))
        try:
            force = forces[charge]
        except KeyError:
            force = '---'
        print('| {0:^7s}|{1:^7d}|{2:^7d}|{3:^7d}|{4:^11}|'
              .format(name, x, y, intensity, force))
    ui.colored_print('\n', 'blue')
    ui.colored_print('>> ', 'red2')
    ui.colored_print('Press any key to go menu', 'blinking')
    input('')


def reset(ui, charges, vectors, forces, t_charge):
    ui.header('Reset :')
    answer = input('Erase all imported data from memory? [y/n]\n>> ')
    if answer in ['y', 'Y']:
        charges.clear()
        t_charge[0], t_charge[1], t_charge[2] = 1, 0, 0
        vectors['i'].clear()
        vectors['j'].clear()
        forces.clear()
        ui.colored_print('All data has been reset to default values.', 'red')
        ui.colored_print('>> ', 'red2')
        ui.colored_print('Hit enter to go menu.', 'blinking')
        input('')
    else:
        return None
