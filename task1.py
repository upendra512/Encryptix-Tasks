# TO-DO LIST

import tkinter as tk
from tkinter import messagebox

tasks = {}

def add_task():
    task_id = task_id_entry.get()
    task_description = task_desc_entry.get()
    if task_id and task_description:
        tasks[task_id] = {'description': task_description, 'status': 'Pending'}
        update_task_listbox()
        task_id_entry.delete(0, tk.END)
        task_desc_entry.delete(0, tk.END)
        print(f"Task {task_id} added successfully.")
    else:
        messagebox.showwarning("Input Error", "Please enter both Task ID and Description.")

def view_tasks():
    if tasks:
        print("\nTo-Do List:")
        for task_id, details in tasks.items():
            print(f"Task ID: {task_id}, Description: {details['description']}, Status: {details['status']}")
    else:
        print("\nNo tasks found.")

def update_task():
    task_id = task_id_entry.get()
    task_description = task_desc_entry.get()
    status = status_var.get()
    if task_id in tasks:
        if task_description:
            tasks[task_id]['description'] = task_description
        if status:
            tasks[task_id]['status'] = status
        update_task_listbox()
        task_id_entry.delete(0, tk.END)
        task_desc_entry.delete(0, tk.END)
        print(f"Task {task_id} updated successfully.")
    else:
        messagebox.showwarning("Input Error", "Task ID not found.")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        selected_task = task_listbox.get(selected_task_index)
        task_id = selected_task.split(",")[0].split(": ")[1]
        del tasks[task_id]
        update_task_listbox()
        print(f"Task {task_id} deleted successfully.")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def update_task_listbox():
    task_listbox.delete(0, tk.END)
    for task_id, details in tasks.items():
        task_listbox.insert(tk.END, f"Task ID: {task_id}, Description: {details['description']}, Status: {details['status']}")

root = tk.Tk()
root.title("To-Do List")

# Task ID
tk.Label(root, text="Task ID:").pack()
task_id_entry = tk.Entry(root)
task_id_entry.pack()

# Task Description
tk.Label(root, text="Task Description:").pack()
task_desc_entry = tk.Entry(root)
task_desc_entry.pack()

# Task Status
tk.Label(root, text="Task Status:").pack()
status_var = tk.StringVar(value="Pending")
tk.Radiobutton(root, text="Pending", variable=status_var, value="Pending").pack()
tk.Radiobutton(root, text="Completed", variable=status_var, value="Completed").pack()

# Buttons
tk.Button(root, text="Add Task", command=add_task).pack()
tk.Button(root, text="Update Task", command=update_task).pack()
tk.Button(root, text="Delete Task", command=delete_task).pack()

# Task Listbox
task_listbox = tk.Listbox(root)
task_listbox.pack()

root.mainloop()
