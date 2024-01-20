import tkinter as tk 

window = tk.Tk() 

label = tk.Label(
    text="Hello! TTTTKinter", 
    foreground="white",
    background="black")
label.pack()

label2 = tk.Label(
    text="Hello, I am using hexadecimal colors",
    background="#34A2FE"
)
label2.pack()

# shorthand for it
label3 = tk.Label(text="I was made with shorthand", fg="red", bg="yellow")
label3.pack()

# changing width and height of label 
label4 = tk.Label(
    text="I am 35 width and 10 height long",
    fg="white",
    bg="black",
    width=35,
    height=10
)
label4.pack()

window.mainloop()