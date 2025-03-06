from tkinter import *

window = Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)

my_label = Label(text="I am a Label")
my_label.pack()

input_ = Entry(width=30)
input_.pack()
input_.insert(END,"Some text to begin with")
print(input_.get())
text_box = Text(width=30, height=5)
# text_box_input = text_box.get()
text_box.insert(END,"Example of multi-line text")
text_box.focus()
text_box.pack()
print(text_box.get("1.0",END))
def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to= 10, width= 5, command=spinbox_used)
spinbox.pack()
def buttonclicked():
    my_label["text"] = input_.get()


button = Button(text="Click Me", command=buttonclicked,)
button.pack()
def scale_used(value):
    print(value)
scale = Scale(from_= 0, to= 100,command=scale_used)
scale.pack()
def checkbox_used():
    print(checkstate.get())
checkstate = IntVar()
checkbox = Checkbutton(text="Is on?",variable=checkstate,command=checkbox_used)
checkstate.get()
checkbox.pack()
def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radio_button1 = Radiobutton(text="Option 1",value= 1, variable= radio_state,command=radio_used)
radio_button1.pack()
radio_button2 = Radiobutton(text="Option 2", value= 2, variable= radio_state, command=radio_used)
radio_button2.pack()
def list_(event):
    print(list_box.get(list_box.curselection()))
list_box = Listbox(height=4)
fruits = ["orange", "mango", "apple", "banana"]
for fruit in fruits:
    list_box.insert(fruits.index(fruit),fruit)
list_box.bind("<<ListboxSelect>>", list_)
list_box.pack()
window.mainloop()