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