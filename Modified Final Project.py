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