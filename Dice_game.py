from tkinter import *
import tkinter as tk
import random
from PIL import Image, ImageTk

root = Tk()
root.title("Dice Roller")
root.geometry("800x600")
root.resizable(False, False)

def roll_dice():
    num_dice = int(num_dice_entry.get())
    results = [random.randint(1, 6) for _ in range(num_dice)]
    result_label.config(text=f"Roll Results: {results}")

    for i, result in enumerate(results):
        image_path = f"D:/6 month/Python/Assignments/Assignment 3/die{result}.png"
        try:
            dice_image = Image.open(image_path)
            dice_image = ImageTk.PhotoImage(dice_image)
            dice_labels[i].config(image=dice_image)
            dice_labels[i].image = dice_image
        except FileNotFoundError:
             dice_labels[i].config(image='')
             dice_labels[i].config(text=str(result)) 

def create_dice_images(num_dice):
    for i in range(num_dice):
         label = Label(image_frame, width=50, height=50)
         dice_labels.append(label)
         label.pack(side=LEFT, padx=5)


num_dice_frame = Frame(root)
num_dice_frame.pack(pady=10)
num_dice_label = Label(num_dice_frame, text="Number of Dice:")
num_dice_label.pack(side=tk.LEFT)
num_dice_entry = Entry(num_dice_frame, width=5)
num_dice_entry.pack(side=tk.LEFT)
num_dice_entry.insert(0, "1") 

roll_button = Button(root, text="Roll Dice", command=roll_dice)
roll_button.pack(pady=10)

result_label = Label(root, text="Roll Results: ")
result_label.pack()

image_frame = Frame(root)
image_frame.pack()

dice_labels = []
create_dice_images(1)

root.mainloop()