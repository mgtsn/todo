import tkinter as tk
from subject import *

window = tk.Tk()
window.title("To Do")
window.geometry("600x600")

# PLACEHOLDER: make function for user entry for sub & task ############
subjects = []
tasks = []
for i in range(1, 4):
    subjects.append(Subject(f"Subject {i}"))
    tasks.append(Subject(f"Task {i}"))
######################################################################

window.mainloop()
