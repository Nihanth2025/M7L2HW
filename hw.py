from tkinter import *
from datetime import date

root = Tk()
root.title("Age Calculator App")
root.geometry("500x500")

f = Frame(master=root, height=300, width=400, bg="lightblue")
f.place(x=50, y=20)

l1 = Label(f, text="Enter your birth date:", width=20, bg="lightblue")
l1.place(x=10, y=20)
birth_date_entry = Entry(f)
birth_date_entry.place(x=180, y=20)

l2 = Label(f, text="Enter your birth month:", width=20, bg="lightblue")
l2.place(x=10, y=60)
birth_month_entry = Entry(f)
birth_month_entry.place(x=180, y=60)

l3 = Label(f, text="Enter your birth year:", width=20, bg="lightblue")
l3.place(x=10, y=100)
birth_year_entry = Entry(f)
birth_year_entry.place(x=180, y=100)

tb = Text(f, fg="black", bg="yellow", height=4, width=45)
tb.place(x=10, y=180)

def display():
    day = int(birth_date_entry.get())
    month = int(birth_month_entry.get())
    year = int(birth_year_entry.get())

    today = date.today()
    b_date = date(year, month, day)
    age = today.year - b_date.year - ((today.month, today.day) < (b_date.month, b_date.day))
    message = f"Hurray! You have created a new account.\nYour Age is: {age} years"
    
    tb.delete(1.0, END)
    tb.insert(END, message)

b = Button(f, text="Current age", command=display)
b.place(x=130, y=140)

root.mainloop()