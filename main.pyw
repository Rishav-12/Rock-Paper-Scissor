from tkinter import *
import random
import sys

root = Tk()
root.geometry("680x600")
root.title("Rock Paper Scissors")
icon = PhotoImage(file = "rock-paper-scissors.png")
root.iconphoto(False, icon)

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

    player_win = [player == "Rock" and comp == "Scissors",
    player == "Paper" and comp == "Rock",
    player == "Scissors" and comp == "Paper"]

    comp_win = [comp == "Rock" and player == "Scissors",
    comp == "Paper" and player == "Rock",
    comp == "Scissors" and player == "Paper"]
    
    if comp == player:
        result.config(text = 'Tie')
    elif any(player_win):
        result.config(text = f"{player} beats {comp}")
        p_score += 1
    elif any(comp_win):
        result.config(text = f"{comp} beats {player}")
        c_score += 1
    
    label_pscore.config(text = f'Your score: {p_score}')
    label_cscore.config(text = f"Computer's score: {c_score}")
    
    # Checking if anyone has won
    if p_score == 5:
        handle_win("You win the contest.\nCongratulations!!")
    elif c_score == 5:
        handle_win("You lose the contest.\nBetter luck next time.")

def handle_restart(ans): # Function either plays a new game or quits the app according to button pressed
    global p_score
    global c_score
    play_again = ans
    if play_again == 'y': # If player chooses to play again, everything is reset
        p_score = 0
        c_score = 0
        play_again = ""
        quit_btn.config(state = DISABLED)
        play_again_btn.config(state = DISABLED)
        rockbutton.config(state = NORMAL)
        paperbutton.config(state = NORMAL)
        scissorsbutton.config(state = NORMAL)
        label_pscore.config(text = f'Your score: {p_score}')
        label_cscore.config(text = f"Computer's score: {c_score}")
        result.config(text = "Let's Begin!")
        who_won.config(text = "")
    elif play_again == 'n': # If player chooses to quit, we exit the game
        sys.exit()

def handle_win(message):
    who_won.config(text = message)
    quit_btn.config(state = NORMAL)
    play_again_btn.config(state = NORMAL)
    rockbutton.config(state = DISABLED)
    paperbutton.config(state = DISABLED)
    scissorsbutton.config(state = DISABLED)

# Shows the points and other info about the current game
playingFrame = Frame(root, bg = 'lightblue')
playingFrame.grid(row = 0, column = 1, pady = 10)

# Holds the options to play again or quit
optionsFrame = Frame(root, bg = 'cyan')
optionsFrame.grid(row = 1, column = 0, columnspan = 2, pady = 5)

# Holds the buttons from which user chooses 'Rock', 'Paper' or 'Scissors'
choicesFrame = Frame(root, bg = 'green')
choicesFrame.grid(row = 0, column = 0, padx = 10)

# Stuff in the playingFrame ------------------------
label_player = Label(playingFrame, text = f'Player : {player}', font = ('Comic Sans MS', 20, 'bold'), padx = 30, pady = 5)
label_player.pack(pady = 15)
label_comp = Label(playingFrame, text = f'Computer : {comp}',font = ('Comic Sans MS', 20, 'bold'), padx = 30, pady = 5)
label_comp.pack(pady = 15)

result = Label(playingFrame, text = "Let's Begin!",font = ('Comic Sans MS', 20, 'bold'), padx = 30, pady = 5)
result.pack(pady = 15)

label_pscore = Label(playingFrame, text = f'Your score: {p_score}',font = ('Comic Sans MS', 20, 'bold'), padx = 30, pady = 5)
label_pscore.pack(pady = 15)
label_cscore = Label(playingFrame, text = f"Computer's score: {c_score}",font = ('Comic Sans MS', 20, 'bold'), padx = 30, pady = 5)
label_cscore.pack(pady = 15)

who_won = Label(playingFrame, text = "",font = ('Comic Sans MS', 20, 'bold'), bg = 'lightblue', padx = 30)
who_won.pack()
#---------------------------------------------------

# Stuff in the optionsFrame ------------------------
play_again_btn = Button(optionsFrame, text = 'Play Again', state = DISABLED, command = lambda: handle_restart('y'), padx = 20, pady = 10)
play_again_btn.grid(row = 0, column = 0, padx = 100, pady = 15)

quit_btn = Button(optionsFrame, text = 'Quit', state = DISABLED, command = lambda: handle_restart('n'), padx = 35, pady = 10)
quit_btn.grid(row = 0, column = 1, padx = 100, pady = 15)
#---------------------------------------------------

# Stuff in the choicesFrame ------------------------
choose_here = Label(choicesFrame, text = "Choose here",font = 'bold', padx = 105, relief = RAISED)
choose_here.pack(side = TOP)

# Buttons for playing
rockbutton = Button(choicesFrame, text = 'ROCK',font = ('Comic Sans MS', 20, 'bold'), padx = 32, pady = 10, command = lambda: choose("Rock"))
rockbutton.pack(pady = 25)
paperbutton = Button(choicesFrame, text = 'PAPER',font = ('Comic Sans MS', 20, 'bold'), padx = 25, pady = 10, command = lambda: choose("Paper"))
paperbutton.pack(pady = 25)
scissorsbutton = Button(choicesFrame, text = 'SCISSORS',font = ('Comic Sans MS', 20, 'bold'), pady = 10, command = lambda: choose("Scissors"))
scissorsbutton.pack(pady = 25)
#---------------------------------------------------

root.mainloop()
