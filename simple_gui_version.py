import random
import PySimpleGUI as sg

sg.theme('Material1')

choices = ['Rock', 'Paper', 'Scissors']

layout = [[sg.Button('Rock'), sg.Text('Player:'), sg.Text('', key='-PLAYER-')],
          [sg.Button('Paper'), sg.Text('Computer:'), sg.Text('', key='-COMPUTER-')],
          [sg.Button('Scissors')],
          [sg.Text('Let\'s Begin')],
          [sg.Text('Your Score'), sg.Text('', key='-PLAYERSCORE-')],
          [sg.Text('Computer\'s Score'), sg.Text('', key='-COMPUTERSCORE-')]
]

window = sg.Window('PSG:RPS', layout)

def play_round(player_choice):
    computer = random.choice(choices)
    window['-PLAYER-'].update(player_choice)
    window['-COMPUTER-'].update(computer)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Rock':
        play_round('Rock')
    if event == 'Paper':
        play_round('Paper')
    if event == 'Scissors':
        play_round('Scissors')

window.close()
