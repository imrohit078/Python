from tkinter import *
import random


root = Tk()
root.title("Rock paper Scissors game using Python")
root.geometry("800x500")

def play_game():
    user_choice = use_var.get()
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    
    user_lbl.config(text=f"User: {user_choice}")
    computer_lbl.config(text=f"Computer: {computer_choice}")

    if user_choice == computer_choice:
        result_lbl.config(text="It's a tie!")
    elif (
        user_choice == "Rock" and computer_choice == "Scissors" or
        user_choice == "Paper" and computer_choice == "Rock" or
        user_choice == "Scissors" and computer_choice == "Paper"
        
    ):
        result_lbl.config(text="You win!")
    else:
        result_lbl.config(text="Computer wins!")
        

use_var = StringVar(value="Rock")

rock_btn = Radiobutton(root, text="Rock", value="Rock", variable=use_var, command=play_game)
rock_btn.pack()

paper_btn = Radiobutton(root, text="Paper", value="Paper", variable=use_var, command=play_game)
paper_btn.pack()

scissors_btn = Radiobutton(root, text="Scissors", value="Scissors", variable=use_var, command=play_game)
scissors_btn.pack()

user_lbl = Label(root, text="")
user_lbl.pack()

computer_lbl = Label(root, text="")
computer_lbl.pack()

result_lbl = Label(root, text="")
result_lbl.pack()

root.mainloop()