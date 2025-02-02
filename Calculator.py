from tkinter import *

root = Tk()
root.geometry("700x500+500+100")
root.title("Calculator")

e = Entry(root, font=("arial", 30), width=25)
e.grid(padx=70, pady=40)

def numbtn(num):
    value = e.get()
    e.delete(0, END)
    e.insert(0, str(value)+ str(num))
    
def add():
    global add
    add = e.get() 
    e.delete(0, END)
    global oper 
    oper = "+"
    
def sub():
    global sub
    sub = e.get() 
    e.delete(0, END)
    global oper 
    oper = "-"
    
def mul():
    global mul
    mul = e.get() 
    e.delete(0, END)
    global oper 
    oper = "*"
    
def div():
    global div
    div = e.get() 
    e.delete(0, END)
    global oper 
    oper = "/"

def mod():
    global mod
    mod = e.get() 
    e.delete(0, END)
    global oper 
    oper = "%"
    
def eql():
    second = e.get()
    e.delete(0, END)
    if oper == "+":
        e.insert(0, int(add) + int(second))
    elif oper == "-":
        e.insert(0, int(sub) - int(second))
    elif oper == "*":
        e.insert(0, int(mul) * int(second))
    elif oper == "/":
        if int(second) == 0:
            e.insert(0, "Error! Division by zero")
        else:
            e.insert(0, int(div) / int(second))
    elif oper == "%":
        e.insert(0, int(mod) % int(second))

def clearr():
    e.delete(0, END)
    
def dell():
    value = e.get()
    if value:
        e.delete(len(value)-1)
    
    

btn_clear = Button(root, text="CL", font=("arial", 10), width=13, command=clearr).place(x=70,y=150)
btn_delete = Button(root, text="DEL", font=("arial", 10), width=13, command=dell).place(x=210,y=150)
btn_per = Button(root, text="%", font=("arial", 10), width=13, command=mod).place(x=360,y=150)
btn_div = Button(root, text="/", font=("arial", 10), width=13, command=div).place(x=510,y=150)

btn_7 = Button(root, text="7", font=("arial", 10), width=13, command= lambda : numbtn(7)).place(x=70,y=200)
btn_8 = Button(root, text="8", font=("arial", 10), width=13, command= lambda : numbtn(8)).place(x=210,y=200)
btn_9 = Button(root, text="9", font=("arial", 10), width=13, command= lambda : numbtn(9)).place(x=360,y=200)
btn_mul = Button(root, text="*", font=("arial", 10), width=13, command=mul).place(x=510,y=200)

btn_4 = Button(root, text="4", font=("arial", 10), width=13, command= lambda : numbtn(4)).place(x=70,y=250)
btn_5 = Button(root, text="5", font=("arial", 10), width=13, command= lambda : numbtn(5)).place(x=210,y=250)
btn_6 = Button(root, text="6", font=("arial", 10), width=13, command= lambda : numbtn(6)).place(x=360,y=250)
btn_sub = Button(root, text="-", font=("arial", 10), width=13, command=sub).place(x=510,y=250)

btn_1 = Button(root, text="1", font=("arial", 10), width=13, command= lambda : numbtn(1)).place(x=70,y=300)
btn_2 = Button(root, text="2", font=("arial", 10), width=13, command= lambda : numbtn(2)).place(x=210,y=300)
btn_3 = Button(root, text="3", font=("arial", 10), width=13, command= lambda : numbtn(3)).place(x=360,y=300)
btn_add = Button(root, text="+", font=("arial", 10), width=13, command=add).place(x=510,y=300)

btn_0 = Button(root, text="0", font=("arial", 10), width=31, command= lambda : numbtn(0)).place(x=70,y=350)
btn_eql = Button(root, text="=", font=("arial", 10), width=32, command=eql).place(x=360,y=350)




root.mainloop()