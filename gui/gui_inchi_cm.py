import PySimpleGUI as sg

layout = [
    [sg.Text('인치를 센티미터로 변환하기')],
    [sg.Text('인치'), sg.InputText(key='inch')],
    [sg.Button('변환')],
    [sg.Text('---', key='info', size=(40, 1))]
]

window = sg.Window('인치 → 센티미터 변환', layout)

while True:
    (event, values) = window.read()

    if event in ('Exit', 'Quit', None):
        break

    if event == '변환':
        inch = float(values['inch'])
        cm = inch * 2.54
        s = '{0}inch = {1}cm'.format(inch, cm)
        window['info'].update(s)

window.close()
