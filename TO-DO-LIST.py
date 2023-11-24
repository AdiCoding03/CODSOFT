import tkinter as tk
from tkinter import Listbox, Scrollbar, Entry, messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task.upper())
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Create the main window
root = tk.Tk()
root.title("TO-DO-LIST")
root.geometry("466x659")

# Set the background image (modify the file path accordingly)
background_image = tk.PhotoImage(file="C:\\Users\\adity\\OneDrive\\Desktop\\to-do-list.gif")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create and pack the listbox to display tasks
listbox_frame = tk.Frame(root)
listbox_frame.place(x=84, y=135)

listbox = Listbox(listbox_frame, selectmode=tk.SINGLE, bg='white', width=55, height=22)
listbox.pack(side=tk.LEFT)

# Create a vertical scrollbar for the listbox
scrollbar = Scrollbar(listbox_frame, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

# Create and pack the entry widget for adding tasks
entry = Entry(root, bg="lightyellow", fg="black", width=61, bd=6, font=("arial", 8))
entry.place(x=60, y=500)

button1 = tk.Button(root, text="Add Task", bg="lightpink", fg="white", command=add_task, width=8, font=("arial", 13, "bold"))
button2 = tk.Button(root, text="Remove Task", bg="lightblue", fg="white", command=remove_task, width=11, font=("arial", 12, "bold"))
button1.place(x=96, y=569)
button2.place(x=263, y=569)

# Run the main loop
root.mainloop()
