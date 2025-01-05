import random
from tkinter import *
from tkinter import Tk

guess_counter=0
chances=50
target=random.randrange(100)

def guess_number():
    global guess_counter
    
    try:
        my_guess = int(user_input)  # Convert the input to an integer
    except ValueError:  # Handle non-integer input
        label_result.config(text="Invalid input! Please enter a valid number.", fg="orange")
        return
        
    guess_counter += 1
    entry_guess.delete(0, END)
        
    if my_guess==target:
        print("Correct guess")
        label_result.config(text=f"You guessed it right in {guess_counter} times" ,fg="blue")
        entry_guess.config(state="disabled")
        # return

    elif my_guess>target:
        print("Correct guess")
        label_result.config(text="Your guess was too high!", fg="blue")

    elif my_guess<target:
            print("Correct guess")
            label_result.config(text="Your guess was too low!", fg="blue")

    else:
        # print("Invalid input")
            label_result.config(text="Invalid input...", fg="blue")

#Function to reset the game         
def reset_game():
    global guess_counter, target
    guess_counter=0
    target=random.randrange(100)
    entry_guess.config(state="normal")
    entry_guess.delete(0, END)
    label_result.config(text="Game Reset! Start guessing now...")

root = Tk()
root.title("Guess The Number Game")
root.attributes("-fullscreen", True)
root.configure(bg="brown")

label_title=Label(root, text="GUESS THE NUMBER", font=("Helvatics", 30), pady=20)

entry_guess=Entry(root, font=("Roman", 16), width=10, justify="center")

button_guess=Button(root, text="Guess", font=("Roman",14), command=guess_number)

label_result=Label(root, font=("Roman", 14), pady=10)

button_reset=Button(root, text="Reset Game", font=("Roman", 14), justify="center", command=reset_game)

button_exit=Button(root, text="Exit Game", font=("Roman, 14"), justify="center",command=root.destroy)

# Place widgets on the window
label_title.pack()
entry_guess.pack(pady=10)
button_guess.pack(pady=10)
label_result.pack(pady=20)
button_reset.pack(side="bottom", padx=100, pady=100)
button_exit.pack(side="bottom", padx=100, pady=100)

root.mainloop()

guess_number()
