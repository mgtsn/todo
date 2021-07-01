import tkinter as tk
from subject import *

window = tk.Tk()
window.title("To Do")
window.geometry("600x600")

s = Subject("Example Subject")
label = tk.Label(text=s.name)
label.grid(column=0, row=0)

window.mainloop()
