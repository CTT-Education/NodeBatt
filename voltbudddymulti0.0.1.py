import PySimpleGUI as sg


def open_window():
    layout = [[sg.Text("Voltage Timer", key="new")]]
    window = sg.Window("Second Window", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        
    window.close()

layout = [
	[
        sg.Text('Please input highest node voltage'),
		sg.Input(key = '-INPUT-'),
		sg.Button('Calculate', key = '-CONVERT-')
	],
	[sg.Text('', key = '-TEXT-')],
    [sg.Text('', key = '-TEXT2-')],
    [sg.Button('', key = '-OPEN-')]
]

window = sg.Window('Converter',layout)

while True:
    event, values = window.read()

    if event == "-OPEN-":
            open_window()
    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        window['-TEXT-'].update('')
        input_value = values['-INPUT-']
        input_value = ''.join(filter(lambda x: x in '.0123456789', str(input_value)))
        if input_value and float(input_value) <= float('3.64'):
            window['-TEXT-'].update('Node below voltage please charge node.')
            window['-TEXT2-'].update('')
        if input_value and float(input_value) >= float('3.86'):
            window['-TEXT-'].update('Node Above Voltage please discharge.')
            window['-TEXT2-'].update('Node should take approximately 2 and a half hours to discharge.')
        if input_value and float(input_value) >= float('3.87'):
            window['-TEXT-'].update('Node Above Voltage please discharge.')
            window['-TEXT2-'].update('Node should take approximately 5 hours to discharge.')
        if input_value and float(input_value) >= float('3.88'):
            window['-TEXT-'].update('Node Above Voltage please discharge.')
            window['-TEXT2-'].update('Node should take approximately 7 and a half hours to discharge.')
        if input_value and float(input_value) >= float('3.89'):
            window['-TEXT-'].update('Node Above Voltage please discharge.')
            window['-TEXT2-'].update('Node should take approximately 10 hours to discharge.')
        if input_value and float(input_value) >= float('3.90'):
            window['-TEXT-'].update('Node Above Voltage please discharge.')
            window['-TEXT2-'].update('Node should take approximately 12 and a half hours to discharge.')
        if input_value and float(input_value) >= float('3.91'):
            window['-TEXT-'].update('Node Above Voltage please discharge.')
            window['-TEXT2-'].update('Node should take approximately 15 hours to discharge.')
        if input_value and float(input_value) >= float('3.92'):
            window['-TEXT-'].update('Node Above Voltage please discharge.')
            window['-TEXT2-'].update('Node should take approximately 17 and a half hours to discharge.')
        if input_value and float(input_value) >= float('3.93'):
            window['-TEXT-'].update('Node Above Voltage please discharge.')
            window['-TEXT2-'].update('Node should take approximately 20 hours to discharge.')
        if input_value and float(input_value) >= float('3.94'):
            window['-TEXT-'].update('Node Above Voltage please discharge.')
            window['-TEXT2-'].update('Node should take approximately 22 and a half hours to discharge.')
        if input_value and float(input_value) >= float('3.95'):
            window['-TEXT-'].update('Node Above Voltage please discharge.')
            window['-TEXT2-'].update('Node should take approximately over 24 hours to discharge, recheck tommorow.')
        if input_value and float(input_value) <= float('3.85') and input_value and float(input_value) >= float('3.65'):
            window['-TEXT-'].update('Node within shipping voltage.')
            window['-TEXT2-'].update('')
        window['-INPUT-'].update('')
