import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database setup
conn = sqlite3.connect("todo.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT)''')
conn.commit()

def add_task():
    task = task_entry.get()
    if task:
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        conn.commit()
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task = task_list.curselection()[0]
        task_text = task_list.get(selected_task)
        cursor.execute("DELETE FROM tasks WHERE task=?", (task_text,))
        conn.commit()
        task_list.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def load_tasks():
    cursor.execute("SELECT task FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        task_list.insert(tk.END, task[0])

# GUI setup
root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

task_list = tk.Listbox(root, width=50)
task_list.pack(pady=10)

load_tasks()
root.mainloop()

conn.close()
