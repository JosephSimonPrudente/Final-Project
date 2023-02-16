from tkinter import *
import random
from words import words

root = Tk()
root.geometry('800x600+400+100')
root.title('Speed Typing Game')
root.configure(bg='black')

score = 0
miss = 0
timer = 60
count = 0
sliderwords = ''
score_to_beat = 0

# Function to animate the sliding text
def slider():
    global count, sliderwords
    text = 'Speed Typing Game'
    if count >= len(text):
        count = 0
        sliderwords = ''
    sliderwords += text[count]
    count += 1
    fontlabel.configure(text=sliderwords)
    fontlabel.after(150, slider)

# Function to handle the timer
def time():
    global timer, score, miss, score_to_beat
    if timer > 11:
        pass
    else:
        timerlabelcount.configure(fg='red')
    if timer > 0:
        timer -= 1
        timerlabelcount.configure(text=timer)
        timerlabelcount.after(1000, time)
    else:
        gameinstruction.configure(text='Hit = {} | Miss = {} | Score to Beat = {}'.format(score, miss, score_to_beat))
      
        wordentry.config(state='disabled') # disable the Entry widget
        if score > score_to_beat:
            score_to_beat = score
            score_to_beat_label.configure(text=f"Score to Beat: {score_to_beat}")

# Function to reset game
def reset_game():
    global timer, score, miss
    score = 0
    miss = 0
    timer = 60
    timerlabelcount.configure(text=timer)
    wordlabel.configure(text=words[0])
    scorelabelcount.configure(text=score)
    score_to_beat_label.configure(text=f"Score to Beat: {score_to_beat}")
    gameinstruction.configure(text='Type the Word and hit enter button')
    wordentry.config(state='normal') # enable the Entry widget

# Function to display the record board
def show_record_board():
    # Create a new window
    record_window = Toplevel(root)
    record_window.geometry('400x400+500+200')
    record_window.title('Record Board')
    
    # Create a label for the title
    title_label = Label(record_window, text='Record Board', font=('arial', 20, 'bold'))
    title_label.pack(pady=10)
    
    # Create a table for the scores
    score_table = Text(record_window, font=('arial', 14), width=30, height=10)
    score_table.insert(END, 'Try\tMisses\tScore\n')

    # Loop through each item in the score list and add it to the table
    for i, (score, miss) in enumerate(score_list):
        score_table.insert(END, f'{score}\t{miss}\t{score_to_beat}\n')
    score_table.pack(pady=10)

# Keep track of the scores in a list
score_list = []

# Function to start the game
def startgame(event):
    global score, miss, score_to_beat, score_list
    if timer == 60:
        time()
    gameinstruction.configure(text='')
    startlabel.configure(text='')
    
    if wordentry.get() == wordlabel['text']:
        score += 1
        scorelabelcount.configure(text=score)
        if score > score_to_beat:
            score_to_beat = score
            score_to_beat_label.configure(text=f"Score to Beat: {score_to_beat}")
    else:
        miss += 1
        
    # Add the score and miss count to the score list for each attempt
    score_list.append((score, miss))
        
    random.shuffle(words)
    wordlabel.configure(text=words[0])
    wordentry.delete(0, END)