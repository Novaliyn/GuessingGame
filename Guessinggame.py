import random
from tkinter import *
import tkinter.font as tkfont
'''
The purpose of this program is a simple guessing game, with multiple options on types of objects.
it uses Tkinter to display a gui and uses buttons and widgets to display buttons for the user to interact with the game.
Input: Button clicks from user, lists that give the user options for the game.
Outputs: If user got answer correct, and the list of objects they chose.

'''
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

def display():
    global HEIGHT, FB, AFB
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

    FB = Label(root, text="", font=FONT)
    FB.place(x=10, y= HEIGHT - 100)

    AFB = Label(root, text="", font=FONT)
    AFB.place(x=10, y=20)

    EXIT = Button(root, text = "EXIT", font=FONT,command= root.destroy)
    EXIT.place(x=WIDTH-75, y=HEIGHT-50)

def button_click(id2):
    global GUESS
    if len(GUESS) < NUMGUESS:
        GUESS.append(LIST[id2])
        if len(GUESS) == NUMGUESS:
            CHECK()
        FB.config(text=f'Your guesses: {", ".join(GUESS)}')

def CHECK():
    global GUESS
    a1 = 0
    a2 = 0
    for a in range(NUMGUESS):
        a1+=1
        if AWS == GUESS[a]:
            a2 = 1
            feedback = f'Correct! You guessed: {str(AWS)}'
        elif a1 == NUMGUESS and a2 == 0:
            feedback = f'Incorrect. The answer was: {str(AWS)}'
    AFB.config(text = feedback)

start()
root.mainloop()