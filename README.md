# Python
# GUI Program

from tkinter import *
from tkinter import messagebox

master = Tk()
master.title("Student Details")
master.geometry("500x600")
responses = []

name = Label(master, text="Name").place(x=10, y=10)
ev1 = StringVar()
e1 = Entry(master, bg="lightpink", fg="black", textvariable=ev1).place(x=100, y=10)

gender = Label(master, text="Gender").place(x=10, y=50)
rv1 = IntVar()
r1 = Radiobutton(master, text="Male", variable=rv1, value=1).place(x=100, y=50)
r2 = Radiobutton(master, text="Female", variable=rv1, value=2).place(x=150, y=50)

qualification = Label(master, text="Qualifications").place(x=10, y=100)
cv1 = IntVar()
cv2 = IntVar()
cv3 = IntVar()
cv4 = IntVar()

c1 = Checkbutton(master, text="Python", variable=cv1, onvalue=1, offvalue=0, height=2, width=10).place(x=107, y=100)
c2 = Checkbutton(master, text="C++", variable=cv2, onvalue=1, offvalue=0, height=2, width=10).place(x=100, y=130)
c3 = Checkbutton(master, text="Java", variable=cv3, onvalue=1, offvalue=0, height=2, width=10).place(x=100, y=160)
c4 = Checkbutton(master, text="SQL", variable=cv4, onvalue=1, offvalue=0, height=2, width=10).place(x=100, y=190)

marks = Label(master, text="Marks obtained in class XII").place(x=10, y=240)
english = Label(master, text="English").place(x=10, y=270)
maths = Label(master, text="Maths").place(x=10, y=300)
science = Label(master, text="Science").place(x=10, y=330)

ev2 = StringVar()
ev3 = StringVar()
ev4 = StringVar()

e2 = Entry(master, bg="lightpink", fg="black", textvariable=ev2).place(x=110, y=270)
e3 = Entry(master, bg="lightpink", fg="black", textvariable=ev3).place(x=110, y=300)
e4 = Entry(master, bg="lightpink", fg="black", textvariable=ev4).place(x=110, y=330)


def save():
    if (len(ev1.get())) == 0 and ev1.get().isnumeric():
        messagebox.showerror("Error", "Please Enter Valid Response...")
    elif (len(ev2.get())) == 0 and not ev2.get().isnumeric():
        messagebox.showerror("Error", "Please Enter Valid Response...")
    elif (len(ev3.get())) == 0 and not ev3.get().isnumeric():
        messagebox.showerror("Error", "Please Enter Valid Response...")
    elif (len(ev4.get())) == 0 and not ev4.get().isnumeric():
        messagebox.showerror("Error", "Please Enter Valid Response...")
    elif (rv1.get()) == 0:
        messagebox.showerror("Error", "Please Select an option for gender")
    else:
        responses.append(ev1.get())
        responses.append(ev2.get())
        responses.append(ev3.get())
        responses.append(ev4.get())
        responses.append(rv1.get())
        responses.append(cv1.get())
        responses.append(cv2.get())
        responses.append(cv3.get())
        responses.append(cv4.get())

        Label(master, text="Success").place(x=50, y=400)


b1 = Button(master, text="Submit", bg="lightblue", fg="black", command=save).place(x=50, y=360)


def percentage():
    total_marks = int(ev2.get()) + int(ev3.get()) + int(ev4.get())
    if total_marks is None:
        messagebox.showerror("Error", "Enter marks first")
    else:
        final_result = "The total percentage =" + str(float(total_marks / 3))
        Label(master, text=final_result).place(x=50, y=480)


b2 = Button(master, text="Calculate Percentage", bg="lightblue", fg="black", command=percentage).place(x=50, y=430)


master.mainloop()


