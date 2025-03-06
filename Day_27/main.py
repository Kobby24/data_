from tkinter import *
def buttonclicked():
    my_label["text"] = input_.get()


window = Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)

my_label = Label(text="I am a Label")
my_label.grid(row=0,column=0 )

button = Button(text="Click Me", command=buttonclicked,)
button.grid(row=1,column=1)
new_button = Button(text="New Button" )
new_button.grid(row=0,column=2)
input_ = Entry(width=30)
input_.grid(row=2,column=3)

print(input_.get())


window.mainloop()

