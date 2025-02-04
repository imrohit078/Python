from tkinter import * 
from PIL import ImageTk, Image
import pywhatkit as kit 

def send_message_at_time():
    try:
        kit.sendwhatmsg(num.get(), msg.get(), int(hour_entry.get()), int(minute_entry.get()))
        status_label.config(text="Message sent successfully", fg="green")
    
    except  Exception as e:
        status_label.config(text=f"Error : {str(e)}", fg="red")

root  = Tk()
root.title("Whatsapp Message")
root.geometry("900x700")
root.config(bg="black")

Label(root, text="Chat Blast", font="arial 40 bold", bg="black", fg="green").pack()
frm1 = Frame(root, bg="black" , height="400", width="400")
frm1.place(x=470, y=100)


msg  = Entry(frm1, font=("arial", 12), width=36)
msg.insert(0, "Enter the message... ")
msg.pack(pady=10)

num  = Entry(frm1, font=("arial", 12), width=36)
num.insert(0, "Enter the Phone number... ")
num.pack(pady=10)

Label(frm1, text="Enter the time in 24 hour format", font="arial 12", bg="black", fg="white").pack(pady=5)
hour_entry = Entry(frm1, font=("arial", 12), width=10)
hour_entry.pack(pady=5)

Label(frm1, text="Minute", font="arial 12", bg="black", fg="white").pack(pady=5)
minute_entry = Entry(frm1, font=("arial", 12), width=10)
minute_entry.pack(pady=5)

Button(frm1, text="Send Message at Time", font="arial 12", bg="green", fg="white" , command=send_message_at_time).pack(pady=10)
status_label = Label(frm1, text="", font="arial 12", bg="black", fg="red")
status_label.pack(pady=10)

frm = Frame(root, bg="black", height="300", width="100")
frm.place(x=10, y=200)

img = Image.open("D:/6 month/Python/TK inter/image.png").crop((20,20,300,300)).resize((430,500))
imgtk = ImageTk.PhotoImage(img)
Label(frm, image=imgtk, bg="black").pack(fill="both", expand=True)

root.mainloop()