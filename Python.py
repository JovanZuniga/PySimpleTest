import PySimpleGUI as sg

layout = [[sg.Text('Test')]]
window = sg.Window('Window Title', layout)

while True: 
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()