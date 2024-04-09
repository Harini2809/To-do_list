import tkinter as tk

# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        list_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
        status_label.config(text="Task added successfully!")
    else:
        status_label.config(text="Please enter a task!")

# Function to remove a task from the list
def remove_task():
    try:
        index = list_tasks.curselection()[0]
        list_tasks.delete(index)
        del tasks[index]
        status_label.config(text="Task removed successfully!")
    except IndexError:
        status_label.config(text="No task selected!")

# Function to display all tasks
def display_tasks():
    list_tasks.delete(0, tk.END)
    for task in tasks:
        list_tasks.insert(tk.END, task)

# Create the main application window
root = tk.Tk()
root.title("To-Do List")

# Create GUI elements
label_task = tk.Label(root, text="Enter Task:")
label_task.grid(row=0, column=0, padx=5, pady=5)

entry_task = tk.Entry(root, width=40)
entry_task.grid(row=0, column=1, padx=5, pady=5)

button_add = tk.Button(root, text="Add Task", command=add_task)
button_add.grid(row=0, column=2, padx=5, pady=5)

button_remove = tk.Button(root, text="Remove Task", command=remove_task)
button_remove.grid(row=1, column=0, padx=5, pady=5)

button_display = tk.Button(root, text="Display Tasks", command=display_tasks)
button_display.grid(row=1, column=1, padx=5, pady=5)

list_tasks = tk.Listbox(root, width=50)
list_tasks.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

status_label = tk.Label(root, text="", fg="blue")
status_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()
