from tkinter import *
import string
import pyperclip
import random


root = Tk()
root.title("Password Generator")
root.geometry("500x500")
root.resizable( False, False)


Label(root, font=("times new roman", 20, "bold"), text="Password generator", bg="green", fg="white").pack(fill=X)
def gen_pass():
    length = int(ln_entry.get())
    inc_num = num_var.get()
    inc_spec_char = spec_char_var.get()
    
    characters = string.ascii_letters
    
    if inc_num:
        characters += string.digits
    if inc_spec_char:
        characters += string.punctuation
    
    if not characters:
        password_output.config(text="Please select an option")
        return
    
    password = ''.join(random.choice(characters) for i in range(length))
    password_output.config(text=password)
    
def coopy_to_clipboard():
    password = password_output.cget("text")
    pyperclip.copy(password)
    

ln_label = Label(root, text="Password length: ")
ln_label.pack()
ln_entry = Entry(root)
ln_entry.pack()

num_var = BooleanVar()
num_check = Checkbutton(root, text="Include Numbers", variable=num_var)
num_check.pack()

spec_char_var = BooleanVar()
spec_char_check = Checkbutton(root, text="Include Special Characters", variable=spec_char_var)
spec_char_check.pack()

btn =Button(root, text="Generate Password", bg="blue", fg="white", command=gen_pass)
btn.pack()

password_output = Label(root, text="")
password_output.pack()

copy_btn = Button(root, text="Copy to Clipboard", bg="green", fg="white", command=coopy_to_clipboard)
copy_btn.pack()

root.mainloop()