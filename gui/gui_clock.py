import PySimpleGUI as sg
from datetime import datetime

layout = [
    [sg.Text('디지털시계')],
    [sg.Text('00:00:00', key='clock', font=('Helvetica', 72))]
]

window = sg.Window('시계', layout)

while True:
    (event, values) = window.read(timeout=100)

    if event in ('Exit', 'Quit', None):
        break

    s = datetime.now().strftime('%H:%M:%S')
    window['clock'].update(s)

window.close()
