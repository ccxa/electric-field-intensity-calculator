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

    if position_state and name_state:
        # success message
        ui.header('Setting name > Intensity > Position > Done!')
        ui.colored_print('added successfully: ', 'blue2')
        print(name, '(', x, ',', y, ')= ', intensity, ' Coulomb\n', sep='')
        ui.colored_print('>>', 'red2')
        ui.colored_print(' Hit enter to go menu', 'blinking')

    input('')

    # put info to charges
    charges[name] = [intensity, x, y]
