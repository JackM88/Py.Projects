import tkinter as tk

root = tk.Tk()
root.title("Test Window")
root.geometry("200x200")
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()
root.mainloop()