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