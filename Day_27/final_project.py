from tkinter import *

window = Tk()
window.title("Mile to Kilo")
window.config(padx=20, pady=20)


def convert():
    num = int(inout_.get())
    ans = num * 0.621371
    answer["text"] = ans


inout_ = Entry()
inout_.grid(row=0, column=2)

label = Label(text="Is equal to")
label.grid(row=1, column=0)

answer = Label(text="0")
answer.grid(row=1, column=2)

unit1 = Label(text="Miles")
unit1.grid(row=0, column=3)

unit2 = Label(text="Km")
unit2.grid(row=1, column=3)

button = Button(text="Calculate", command=convert)
button.grid(row=2, column=2)

window.mainloop()
