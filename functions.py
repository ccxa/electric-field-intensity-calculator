def menu(ui):
    number = [0, 1, 2, 3, 4, 5, 6, 7]
    item = ['Add', 'Remove', 'TestCharge', 'Run',
            'Charges', 'Reset', 'Help', 'Exit'
            ]
    ui.colored_print('1.Add    2.Remove    3.TestCharge ', 'printb')
    ui.colored_print('4.Run    5.Charges   6.Reset      ', 'printb')
    ui.colored_print('7.Help   8.Exit                   ', 'printb')