from tkinter import *
import re
from tkinter.ttk import *
from tkinter import filedialog, simpledialog
from tkinter import messagebox
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
root = Tk()
root.geometry("1000x700+200+10")
root.title("Notepad ")
root.resizable(0, 0)
# frm = Frame(root, bg="grey").pack(fill=BOTH, expand=1)

note_pad = ScrolledText(root, wrap=WORD, width=1000, height=700)
file_name = ''
menu = tk.Menu()
root.config(menu=menu)

note_pad_menu = Menu(root)
root.configure(menu=note_pad_menu)


#   button functions
def new_file():
    global file_name
    if len(note_pad.get('1.0', END+'-1c'))>0:
        if messagebox.askyesno("Save", "Do you want to save changes?"):
            save_file()
        else:
            note_pad.delete('1.0', END)
    root.title("Notepad")
    
def open_file():
    fd = filedialog.askopenfile(parent=root, mode='r')
    t = fd.read()
    note_pad.delete('0.0', END)
    note_pad.insert('0.0', t)
    
def save_file():
    fd = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if fd != None:
        data = note_pad.get('1.0', END)
    try:
        fd.write(data)
    except:
        messagebox.showerror(title="Error", message="Unable to save file")
        

def save_as():
    fd = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    t = note_pad.get('0.0', END)
    try:
        fd.write(t.rstrip())
    except:
        messagebox.showerror(title="Error", message="Unable to save file")


def cut_option():
    note_pad.event_generate("<<Cut>>")
    
def copy_option():
    note_pad.event_generate("<<Copy>>")
    
def paste_option():
    note_pad.event_generate("<<Paste>>")
    
def delete_option():
    note_pad.delete(1.0, END)



def about():
    label = messagebox.showinfo("About Notepad", "Notepad by - \nCreated by Rohit Kumar")
#   menu items
file_menu = Menu(note_pad_menu, tearoff= False)
note_pad_menu.add_cascade(label="File", menu=file_menu)

#   file menu items
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


# #    Edit menu
edit_menu = Menu(note_pad_menu, tearoff= False)
note_pad_menu.add_cascade(label="Edit", menu=edit_menu)

#   edit menu items
edit_menu.add_command(label="Cut", command=cut_option)
edit_menu.add_command(label="Copy", command=copy_option)
edit_menu.add_command(label="Paste", command=paste_option)
edit_menu.add_command(label="Delete", command=delete_option)
# edit_menu.add_separator()


#   help menu

help_menu = Menu(note_pad_menu, tearoff= False)
note_pad_menu.add_cascade(label="Help", menu=help_menu)

help_menu.add_command(label="About Notepad", command=about) 
# edit_menu = tk.Menu(menu)
# menu.add_cascade(label="File", menu=edit_menu)
# edit_menu.add_command(label="New" )
# edit_menu.add_command(label="Open" )
# edit_menu.add_command(label="Save")


# #    help
# help_menu = tk.Menu(menu)
# menu.add_cascade(label="Help", menu=help_menu)
# help_menu.add_command(label="About Notepad" )



note_pad.pack()

root.mainloop()


