import random
from tkinter import *
import tkinter.font as tkfont

# Lists and variables
NUMGUESS = 3
GUESS = []
LISTS = [
    ["Fortnite", "Roblox", "Valorant", "Minecraft", "Destiny 2", "Call of Duty"],
    ["dog", "cat", "bird", "bunny", "dolphin", "tiger", "cheetah", "monkey", "human", "butterfly", "worm", "spider", "snake"],
    ["Potatos", "French Fries", "Pizza", "Salad", "Sushi", "Tacos", "Burgers", "Sandwiches"],
    ["Taco Bell", "McDonalds", "Burger King", "Subway", "Wendys", "In-N-Out", "Chick-fil-A", "KFC"],
]
CLIST = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Purple", "Pink", "Brown", "White"]
LISTSN= ["Games", "Animals", "Food","Resturaunts"]
LIST = []
root = Tk()
root.title("Guessing Game")
WIDTH = (NUMGUESS*150)+50
X = WIDTH // 2 - WIDTH / 10
FONT = tkfont.Font(family = "Century", size =  15)

def start():
    screen = Canvas(root, width=200, height=len(LISTS)*65, bg= "grey")
    screen.pack(fill=BOTH, expand=True)
    for i in range(len(LISTS)):
        for C in range(NUMGUESS):
            COLOR = random.choice(CLIST)
        button = Button(root, text=LISTSN[i], font=FONT, bg = COLOR ,command=lambda i=i: LISTCHOICE(i))
        button.place(x=10, y=20+i*50)

def LISTCHOICE(id):
    global LIST, AWS
    LIST = LISTS[id]
    AWS = random.choice(LIST)
    for widget in root.winfo_children():
        widget.destroy()
    display()

# Display answer buttons.
def display():
    global HEIGHT, FB, AFB
    #Create a background canvas
    HEIGHT = len(LIST)*65
    if HEIGHT < 600:
        HEIGHT = 600
    screen = Canvas(root, width=WIDTH, height=HEIGHT, bg= "grey")
    screen.pack(fill=BOTH, expand=True)


    for f in range(len(LIST)):
        for c in range(NUMGUESS):
            COLOR = random.choice(CLIST)
        button = Button(root, text=LIST[f], font=FONT, bg = COLOR,command=lambda f=f: button_click(f))
        button.place(x=X, y=80+f*50)

    # Feedback label
    FB = Label(root, text="", font=FONT)
    FB.place(x=10, y= HEIGHT - 100)

    # Correct? Feedback
    AFB = Label(root, text="", font=FONT)
    AFB.place(x=10, y=20)

    #Exit Button
    EXIT = Button(root, text = "EXIT", font=FONT,command= root.destroy)
    EXIT.place(x=WIDTH-75, y=HEIGHT-50)

# Convert button clicks into variables.
def button_click(id2):
    global GUESS
    if len(GUESS) < NUMGUESS:
        GUESS.append(LIST[id2])
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
start()
root.mainloop()