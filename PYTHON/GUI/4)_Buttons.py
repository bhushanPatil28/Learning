import tkinter as tk 

window = tk.Tk() 

button = tk.Button(
    text = "Click me!",
    width = 25,
    height = 5,
    bg ="blue",
    fg = "yellow"
)
button.pack()

entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack()


window.mainloop()