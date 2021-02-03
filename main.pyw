from tkinter import *
import random
import sys

root = Tk()
root.geometry("680x600")
root.title("Rock Paper Scissors")

choice_list = ["Rock", "Paper", "Scissors"]
global comp
comp = ""
player = ""
global p_score
p_score = 0
global c_score
c_score = 0

def choose(ch):
    global p_score
    global c_score
    comp = random.choice(choice_list) # Computer makes a random choice
    player = ch # Player's choice is set according to the button he/she presses
    label_player.config(text = f'Player : {player}')
    label_comp.config(text = f'Computer : {comp}')
    
    # Analysing all the possible combinations
    if comp == player:
        label_res.config(text = 'Tie')
    elif player == "Rock" and comp == "Scissors":
        label_res.config(text = f"{player} beats {comp}")
        p_score += 1
    elif player == "Paper" and comp == "Rock":
        label_res.config(text = f"{player} beats {comp}")
        p_score += 1
    elif player == "Scissors" and comp == "Paper":
        label_res.config(text = f"{player} beats {comp}")
        p_score += 1
    elif comp == "Rock" and player == "Scissors":
        label_res.config(text = f"{comp} beats {player}")
        c_score += 1
    elif comp == "Paper" and player == "Rock":
        label_res.config(text = f"{comp} beats {player}")
        c_score += 1
    elif comp == "Scissors" and player == "Paper":
        label_res.config(text = f"{comp} beats {player}")
        c_score += 1
    
    label_pscore.config(text = f'Your score: {p_score}')
    label_cscore.config(text = f"Computer's score: {c_score}")
    
    # Checking if anyone has won
    if p_score == 5:
        label_res2.config(text = "You win the contest.\nCongratulations!!")
        quit_btn.config(state = NORMAL)
        play_again_btn.config(state = NORMAL)
        choice1button.config(state = DISABLED)
        choice2button.config(state = DISABLED)
        choice3button.config(state = DISABLED)
    elif c_score == 5:
        label_res2.config(text = "You lose the contest.\nBetter luck next time.")
        quit_btn.config(state = NORMAL)
        play_again_btn.config(state = NORMAL)
        choice1button.config(state = DISABLED)
        choice2button.config(state = DISABLED)
        choice3button.config(state = DISABLED)

def take(ans): # Function either plays a new game or quits the app according to button presed
    global p_score
    global c_score
    play_again = ans
    if play_again == 'y': # If player chooses to play again, everything is reset
        p_score = 0
        c_score = 0
        play_again = ""
        quit_btn.config(state = DISABLED)
        play_again_btn.config(state = DISABLED)
        choice1button.config(state = NORMAL)
        choice2button.config(state = NORMAL)
        choice3button.config(state = NORMAL)
        label_pscore.config(text = f'Your score: {p_score}')
        label_cscore.config(text = f"Computer's score: {c_score}")
        label_res.config(text = "Let's Begin!")
        label_res2.config(text = "")
    elif play_again == 'n': # If player chooses to quit, we exit the game
        sys.exit()

# playingFrame shows the current game's information
playingFrame = Frame(root, bg = 'lightblue')
playingFrame.grid(row = 0, column = 1, pady = 10)

# This frame holds the options to play a new game or quit
newFrame = Frame(root, bg = 'cyan')
newFrame.grid(row = 1, column = 0, columnspan = 2, pady = 5)

label_player = Label(playingFrame, text = f'Player : {player}', font = ('Comic Sans MS', 20, 'bold'), padx = 30, pady = 5)
label_player.pack(pady = 15)
label_comp = Label(playingFrame, text = f'Computer : {comp}',font = ('Comic Sans MS', 20, 'bold'), padx = 30, pady = 5)
label_comp.pack(pady = 15)

label_res = Label(playingFrame, text = "Let's Begin!",font = ('Comic Sans MS', 20, 'bold'), padx = 30, pady = 5)
label_res.pack(pady = 15)

label_pscore = Label(playingFrame, text = f'Your score: {p_score}',font = ('Comic Sans MS', 20, 'bold'), padx = 30, pady = 5)
label_pscore.pack(pady = 15)
label_cscore = Label(playingFrame, text = f"Computer's score: {c_score}",font = ('Comic Sans MS', 20, 'bold'), padx = 30, pady = 5)
label_cscore.pack(pady = 15)

label_res2 = Label(playingFrame, text = "",font = ('Comic Sans MS', 20, 'bold'), bg = 'lightblue', padx = 30)
label_res2.pack()

play_again_btn = Button(newFrame, text = 'Play Again', state = DISABLED, command = lambda: take('y'), padx = 20, pady = 10)
play_again_btn.grid(row = 0, column = 0, padx = 100, pady = 15)

quit_btn = Button(newFrame, text = 'Quit', state = DISABLED, command = lambda: take('n'), padx = 35, pady = 10)
quit_btn.grid(row = 0, column = 1, padx = 100, pady = 15)

# This frame holds the buttons from which user chooses 'Rock', 'Paper' or 'Scissors'
optionsFrame = Frame(root, bg = 'green')
optionsFrame.grid(row = 0, column = 0, padx = 10)

l = Label(optionsFrame, text = "Choose here",font = 'bold', padx = 105, relief = RAISED)
l.pack(side = TOP)

# Buttons for playing
choice1button = Button(optionsFrame, text = 'ROCK',font = ('Comic Sans MS', 20, 'bold'), padx = 32, pady = 10, command = lambda: choose("Rock"))
choice1button.pack(pady = 25)
choice2button = Button(optionsFrame, text = 'PAPER',font = ('Comic Sans MS', 20, 'bold'), padx = 25, pady = 10, command = lambda: choose("Paper"))
choice2button.pack(pady = 25)
choice3button = Button(optionsFrame, text = 'SCISSORS',font = ('Comic Sans MS', 20, 'bold'), pady = 10, command = lambda: choose("Scissors"))
choice3button.pack(pady = 25)

root.mainloop()
