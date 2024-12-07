import random
from tkinter import *
import tkinter.font as tkfont

# Lists and variables
aws_list = ["dog", "cat", "bird", "bunny", "dolphin", "tiger", "cheetah", "monkey", "human", "butterfly", "worm", "spider", "snake"]
AWS = random.choice(aws_list)
NUMGUESS = 2
GUESS = []
root = Tk()
root.title("Guessing Game")
HEIGHT = len(aws_list)*65
WIDTH = NUMGUESS*175
X = WIDTH // 2 - WIDTH / 10
FONT = tkfont.Font(family = "Century", size =  15)
#Create a background canvas
screen = Canvas(root, width=WIDTH, height=HEIGHT, bg= "grey")
screen.pack(fill=BOTH, expand=True)

# Feedback label
FB = Label(root, text="", font=FONT)
FB.place(x=10, y= HEIGHT - 100)

# Correct? Feedback
AFB = Label(root, text="", font=FONT)
AFB.place(x=10, y=20)

#Exit Button
EXIT = Button(root, text = "EXIT", font=FONT,command= root.destroy)
EXIT.place(x=WIDTH-75, y=HEIGHT-50)


# Display answer buttons.
def display():
    for i in range(len(aws_list)):
        button = Button(root, text=aws_list[i], font=FONT ,command=lambda i=i: button_click(i))
        button.place(x=X, y=80+i*50)

# Convert button clicks into variables.
def button_click(id):
    global GUESS
    if len(GUESS) < NUMGUESS:
        GUESS.append(aws_list[id])
        if len(GUESS) == NUMGUESS:
            CHECK()
        update_feedback()

# Check answers
def CHECK():
    global GUESS
    if AWS in GUESS:
        feedback = f'Correct! You guessed: {str(AWS)}'
    else:
        feedback = f'Incorrect. The answer was: {str(AWS)}'
    FEEDBACK(feedback)

# Correct or wrong to user.
def FEEDBACK(feedback):
    AFB.config(text=feedback)
    

# Update feedback display
def update_feedback():
    FB.config(text=f'Your guesses: {", ".join(GUESS)}')

# Start code
display()
root.mainloop()