# Python Weight Converter

from tkinter import *


master = Tk()
master.title("Weight Converter")
master.geometry("480x250")


# Input part of the converter

input_unit = Label(master, text="Select the unit in which you're inputting the weight").place(x=10, y=10)
rv1 = IntVar()
r1 = Radiobutton(master, text="Kilograms", variable=rv1, value=1).place(x=300, y=10)
r2 = Radiobutton(master, text="Pounds", variable=rv1, value=2).place(x=400, y=10)

input_weight = Label(master, text="Enter the weight").place(x=10, y=50)
ev1 = StringVar()
e1 = Entry(master, bg="lightpink", fg="black", textvariable=ev1).place(x=300, y=50)


# Converting part of the converter

def convert():
    if rv1.get() == 1 and rv2.get() == 2:
        output_weight_lbs = int(ev1.get()) * 2.20462
        final_result = "Weight after conversion = " + str(output_weight_lbs) + " lbs"
        Label(master, text=final_result).place(x=130, y=200)
    elif rv1.get() == 2 and rv2.get() == 1:
        output_weight_kg = int(ev1.get()) * 0.453592
        final_result = "Weight after conversion = " + str(output_weight_kg) + " kg"
        Label(master, text=final_result).place(x=130, y=200)
    elif rv1.get() == 1 and rv2.get() == 1:
        final_result = "Weight after conversion = " + ev1.get() + " kg"
        Label(master, text=final_result).place(x=130, y=200)
    elif rv1.get() == 2 and rv2.get() == 1:
        final_result = "Weight after conversion = " + ev1.get() + " lbs"
        Label(master, text=final_result).place(x=130, y=200)


# Output part of the converter
        
output_unit = Label(master, text="Select the unit in which you want the weight").place(x=10, y=90)

rv2 = IntVar()
r3 = Radiobutton(master, text="Kilograms", variable=rv2, value=1).place(x=300, y=90)
r4 = Radiobutton(master, text="Pounds", variable=rv2, value=2).place(x=400, y=90)

b1 = Button(master, text="Convert Weight", bg="lightpink", fg="black", command=convert).place(x=180, y=150)

master.mainloop()
