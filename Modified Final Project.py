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

# Labels and UI elements
fontlabel = Label(root, text='', font=('arial', 25, 'italic bold'), fg='purple', bg='black', width=40)
fontlabel.place(x=10, y=10)
slider()

startlabel=Label(root,text='Start Typing',font=('airal',30,
                  'italic bold'),bg='black',fg='white')
startlabel.place(x=275,y=50)

random.shuffle(words)
wordlabel=Label(root,text=words[0],font=('airal',45,
                'italic bold'),fg='green' ,bg='black')
wordlabel.place(x=300,y=240)

# Add a button to show the record board
record_button = Button(root, text='Record Board', font=('arial', 20, 'bold'), bg='green', fg='white', command=show_record_board)
record_button.place(x=570, y=420)
# Add a button to show the retry and exit
retry_button = Button(root, text='Retry', font=('arial', 20, 'bold'), bg='blue', fg='white', command=reset_game)
retry_button.place(x=330, y=420)
exit_button = Button(root, text='Exit', font=('arial', 20, 'bold'), bg='red', fg='white', command=root.destroy)
exit_button.place(x=450, y=420)

scorelabel=Label(root,text='Your Score:',font=('arial',25,
                'italic bold'),fg='blue' ,bg='black')
scorelabel.place(x=10,y=100)

scorelabelcount=Label(root,text=score,font=('arial',25,
                'italic bold'),fg='blue' ,bg='black')
scorelabelcount.place(x=100,y=180)

score_to_beat_label = Label(root, text=f"Score to Beat: {score_to_beat}", font=('arial', 25, 'italic bold'), fg='purple' ,bg='black')
score_to_beat_label.place(x=270, y=100)


timerlabel=Label(root,text='Time Left:',font=('arial',25,
                'italic bold'),fg='red' ,bg='black')
timerlabel.place(x=600,y=100)

timerlabelcount=Label(root,text=timer,font=('arial',25,
                'italic bold'),fg='red' ,bg='black')
timerlabelcount.place(x=660,y=180)



gameinstruction= Label(root,text='Type the Word and hit enter button',
                       font=('arial',25,'italic bold'),fg='grey' ,bg='black')
gameinstruction.place(x=150,y=500)

########################################################################

wordentry= Entry(root,font=('airal',25,'italic bold'),bd=10,justify='center' )
wordentry.place(x=210,y=330)
wordentry.focus_set()

#################################################################
root.bind('<Return>',startgame)
root.mainloop()
