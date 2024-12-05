import random

def guess(): #user input guess funcion
    global NUMGUESS
    while NUMGUESS>0:
        guess = input("Please give me an animal: ")
        if guess in aws_list:
            my_list.append(guess)
            NUMGUESS -= 1
        else:
            print(f"{guess} was not an option in the answer list.")
 

def intro_text(): #starting text
    print(f"Guess the hidden animal! You have {str(NUMGUESS)} choice(s)")
    print('Your choices are: ')
    print(aws_list)

#lists and variables
my_list = []
aws_list = ["dog", "cat", "bird", "bunny", "dolphin", "tiger", "cheatah", "monkey", "human", "butterfly"]
HALF_AWS = len(aws_list)//2
AWS = random.choice(aws_list)
NUMGUESS = random.randint(1, HALF_AWS)

#start code
intro_text()
guess()

#check if user gave the correct answer.
y = 0
for i in range(len(my_list)):
    if my_list[i] == AWS:
        y = 1
        break
if y==1:
    print(f"You are correct! The correct answer was:  {AWS}")
else:
    print(f"Incorrect. The correct answer was:  {AWS}")
input('Press Enter to quit')