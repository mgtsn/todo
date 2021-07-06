import tkinter as tk
from subject import *
from task import *

window = tk.Tk()
window.title("To Do")
window.geometry("600x600")
bg_color = "#d794f0"
window.configure(bg=bg_color)

tasks = []

# PLACEHOLDER: make function for user entry for task ############
def get_names(t):
    for task in t:
        tk.Label(window, text=task.name).pack()

def add_task(n):
    t = Task(n)
    tasks.append(t)
    tk.Label(window, text=t.name).pack()

name_entry = tk.Entry(window)
name_entry.pack()
tk.Button(window, text="Add Task", command=lambda: add_task(name_entry.get())).pack()

# tasks = generate_tasks()
get_names(tasks)



######################################################################


window.mainloop()
