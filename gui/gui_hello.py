import PySimpleGUI as sg

layout = [
    [sg.Text('간단한 GUI 앱입니다.')],
    [sg.Text('버튼을 클릭해보세요.')],
    [sg.Button('Hello')], [sg.Button('Close')]
]

window = sg.Window('샘플', layout, size=(200, 100))

while True:
    (event, values) = window.read()

    if event in ('Exit', 'Quit', None):
        break

    if event == 'Hello':
        print('Hello 버튼 클릭')
    elif event == 'Close':
        print('Close 버튼 클릭')
        break

window.close()
