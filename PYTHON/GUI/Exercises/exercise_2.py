import tkinter as tk
window = tk.Tk()

ent = tk.Entry(bg="Grey", fg="yellow", width=40)
ent.pack()

ent.insert(0, "Enter your name")

window.mainloop()

print(inp)