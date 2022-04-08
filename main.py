import PySimpleGUI as sg

sg.ChangeLookAndFeel('black')

layout = [  [sg.Text("Prénom")],
            [sg.Input()],
            [sg.Button('Valider')] ]

window = sg.Window('Qubits Ratz', layout, icon=r'assets\favicon.ico')

event, values = window.read()

print('Hello', values[0], " Bienvienue sur Qubitz Ratz")

window.close()