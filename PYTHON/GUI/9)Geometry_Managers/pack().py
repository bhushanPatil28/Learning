import tkinter as tk 

# window = tk.Tk()

# frame1 = tk.Frame(master=window, width=500, height=500, bg="red")
# frame1.pack()

# frame2 = tk.Frame(master=window, width=250, height=250, bg="yellow")
# frame2.pack()

# frame3 = tk.Frame(master=window, width=125, height=125, bg="blue")
# frame3.pack()

# window.mainloop()

window = tk.Tk()

frame1 = tk.Frame(master=window, height=100, bg="red")
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master=window, height=50, bg="yellow")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(master=window, height=25, bg="blue")
frame3.pack(fill=tk.X)

window.mainloop()