import random
import PySimpleGUI as sg

sg.theme('Material1')

choices = ['Rock', 'Paper', 'Scissors']

# Define global variables
player_score = 0
computer_score = 0

layout = [[sg.Button('Rock'), sg.Text('You:'), sg.Text('', size=(15,1), key='-PLAYER-')],
          [sg.Button('Paper'), sg.Text('Computer:'), sg.Text('', size=(15,1), key='-COMPUTER-')],
          [sg.Button('Scissors')],
          [sg.Text('Let\'s Begin', key='-INFO-')],
          [sg.Text('Your Score'), sg.Text(f'{player_score}', key='-PLAYERSCORE-')],
          [sg.Text('Computer\'s Score'), sg.Text(f'{computer_score}', key='-COMPUTERSCORE-')],
          [sg.Button('Play Again', disabled=True), sg.Button('Quit', disabled=True)]
]

window = sg.Window('PySimpleGUI : RPS', layout)

def play_round(player_choice):
    '''Computer makes a random choice, update the UI'''
    computer_choice = random.choice(choices)
    window['-PLAYER-'].update(player_choice)
    window['-COMPUTER-'].update(computer_choice)

    check_round_result(player_choice, computer_choice)

def check_round_result(player_choice, computer_choice):
    '''Checks who wins the round or if theres a tie'''
    global player_score
    global computer_score

    player_win = [player_choice == "Rock" and computer_choice == "Scissors",
    player_choice == "Paper" and computer_choice == "Rock",
    player_choice == "Scissors" and computer_choice == "Paper"]

    computer_win = [computer_choice == "Rock" and player_choice == "Scissors",
    computer_choice == "Paper" and player_choice == "Rock",
    computer_choice == "Scissors" and player_choice == "Paper"]

    if computer_choice == player_choice:
        window['-INFO-'].update('Tie')
    elif any(player_win):
        window['-INFO-'].update(f'{player_choice} beats {computer_choice}')
        player_score += 1
        window['-PLAYERSCORE-'].update(f'{player_score}')
    elif any(computer_win):
        window['-INFO-'].update(f'{computer_choice} beats {player_choice}')
        computer_score += 1
        window['-COMPUTERSCORE-'].update(f'{computer_score}')

    check_match_win()

def check_match_win():
    '''Checks if player or computer has reached 5 points'''
    if player_score == 5:
        handle_win('You Win! Congratulations!!!')
    if computer_score == 5:
        handle_win('You Lose! :sad face:')

def handle_win(msg):
    '''Handles how the UI changes when the match ends'''
    window['-INFO-'].update(msg)
    window['Rock'].update(disabled=True)
    window['Paper'].update(disabled=True)
    window['Scissors'].update(disabled=True)
    window['Play Again'].update(disabled=False)
    window['Quit'].update(disabled=False)

def play_again():
    '''Resets the game state'''
    global player_score
    global computer_score

    window['-INFO-'].update('Let\'s begin')
    window['Rock'].update(disabled=False)
    window['Paper'].update(disabled=False)
    window['Scissors'].update(disabled=False)
    window['Play Again'].update(disabled=True)
    window['Quit'].update(disabled=True)

    player_score = 0
    computer_score = 0

    window['-PLAYERSCORE-'].update(f'{player_score}')
    window['-COMPUTERSCORE-'].update(f'{computer_score}')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == 'Rock':
        play_round('Rock')
    if event == 'Paper':
        play_round('Paper')
    if event == 'Scissors':
        play_round('Scissors')
    if event == 'Play Again':
        play_again()

window.close()
