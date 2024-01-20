import tkinter as tk 
import tkinter.ttk as ttk

# from tkinter import * 
# from tkinter.ttk import * 

window = tk.Tk()
label = tk.Label(text="I am normal")
label.pack()
txt = ttk.Label(text="I am abnormal")
txt.pack()

window.mainloop()

