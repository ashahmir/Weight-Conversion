import tkinter
from tkinter import END

window = tkinter.Tk()

window.title("Weight Conversion")
window.minsize(width=300, height=150)
window.config(padx=40, pady=20)


my_label = tkinter.Label(text="=", font=("Arial", 12))
my_label.grid(column=1, row=2)

my_label1 = tkinter.Label(text="kg", font=("Arial", 12))
my_label1.grid(column=3, row=1)
my_label1.config(pady=10, padx=5)

my_label2 = tkinter.Label(text="lbs", font=("Arial", 12))
my_label2.grid(column=3, row=2)
my_label2.config(pady=10)

my_label3 = tkinter.Label(text="2.25", font=("Arial", 12))
my_label3.grid(column=2, row=2)


def click_listener():
    if my_label1["text"] == "kg":
        convert = (float(answer.get()) * 2.205).__round__(2)
    else:
        convert = (float(answer.get()) / 2.205).__round__(2)

    my_label3.config(text=convert)


my_button = tkinter.Button(text="Convert", command=click_listener)
my_button.grid(column=2, row=3)


def switch_weights():
    if my_label1["text"] == "kg":
        my_label1.config(text="lbs")
    else:
        my_label1.config(text="kg")

    if my_label2["text"] == "kg":
        my_label2.config(text="lbs")
    else:
        my_label2.config(text="kg")
    click_listener()


switch_button = tkinter.Button(text="Switch Conversion", command=switch_weights)
switch_button.grid(column=4, row=1, padx=30)

answer = tkinter.Entry(width=10, justify="center")
answer.insert(END, string="1")
answer.grid(column=2, row=1)


window.mainloop()
