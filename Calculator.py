
from tkinter import *

clicks = 0

def click_button():
    global clicks
    clicks += 1
    root.title("Clicks {}".format(clicks))

root = Tk()
root.title("Calculator")
root.geometry("400x300")

entry_place = Entry(justify=RIGHT, width=35)
entry_place.grid(column=0, row=0, columnspan=5, rowspan=2)

btn_plus = Button(text="+", command=click_button)
btn_plus.grid(column=1, row=3, columnspan=1, rowspan=1)



root.mainloop()
