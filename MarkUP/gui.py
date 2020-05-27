# coding: utf-8
__author__ = "Rafał Karoń <rafalkaron@gmail.com>"

import tkinter as tk

window = tk.Tk()
label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)
button = tk.Button(text="ok")
label.pack()
button.pack()
window.mainloop()