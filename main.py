import tkinter as tk
from subject import *

window = tk.Tk()
window.title("To Do")
window.geometry("600x600")
bg_color = "#d794f0"
window.configure(bg=bg_color)

# PLACEHOLDER: make function for user entry for sub & task ############
subjects = []
tasks = []
for i in range(1, 4):
    subjects.append(Subject(f"Subject {i}"))
    tasks.append(Subject(f"Task {i}"))

names = []
for s in subjects:
    names.append(tk.Label(window, text=s.name).pack())
######################################################################

window.mainloop()
