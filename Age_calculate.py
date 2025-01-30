from tkinter import *
from datetime import date
root = Tk()
root.geometry("700x600+500+100")
root.title("Age Calculator")

# Function for calculate age
def cal_age():
    today = date.today()
    b_date = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
    age = today.year - b_date.year - ((today.month, today.day) < (b_date.month, b_date.day))
    Label(text=f"Hey {nameEntry.get()}, Your age is {age}", font=("Arial", 20, "bold")).place(x=200, y=400)
    
nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

# Design part
Label(root,text="Age Calculator ", font=("Arial", 20, "bold") ).pack()
Label(root,text="Enter Name: ", font=("Arial", 20, "bold") ). place(x=100, y =100)
Label(root,text="Enter Year: ",  font=("Arial", 20, "bold") ). place(x=100, y =150)
Label(root,text="Enter Month: ",  font=("Arial", 20, "bold") ). place(x=100, y =200)
Label(root,text="Enter Day: ",  font=("Arial", 20, "bold") ). place(x=100, y =250)

nameEntry = Entry(root,text="Enter Name: ", font=("Arial", 20, "bold") )
yearEntry = Entry(root,text="Enter Year: ",  font=("Arial", 20, "bold") )
monthEntry = Entry(root,text="Enter Month: ",  font=("Arial", 20, "bold") )
dayEntry = Entry(root,text="Enter Day: ",  font=("Arial", 20, "bold") )

nameEntry.place(x=300, y =100)
yearEntry.place(x=300, y =150)
monthEntry.place(x=300, y =200)
dayEntry.place(x=300, y =250)

Button(root, text="Calculate Age", font=("Arial", 20, "bold"), bg="red", fg="white", command=cal_age).place(x=250, y=300)

root.mainloop()