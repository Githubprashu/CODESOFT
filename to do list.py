import tkinter as tk
from tkinter import messagebox
task_list=[]
def add_item():
    task_name=title_entry.get()
    task_details=description_entry.get()
    if task_name and task_details:
        new_task = {
            'id':len(task_list) + 1,
            'title':task_name,
            'description':task_details,
            'completed':False
        }
        task_list.append(new_task)
        refresh_task_display()
        title_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter both title and description.")

def remove_item():
    selected= tasks_listbox.curselection()
    if selected:
        task_id=tasks_listbox.get(selected[0]).split(' ')[0]
        task_id=int(task_id)
        global task_list
        task_list=[task for task in task_list if task['id'] != task_id]
        refresh_task_display()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")
def refresh_task_display():
    tasks_listbox.delete(0, tk.END)
    for task in task_list:
        status="Completed" if task['completed'] else "Pending"
        tasks_listbox.insert(tk.END,f"{task['id']} {task['title']}-{task['description']} ({status})")
window =tk.Tk()
window.title("Task Manager")
input_frame=tk.Frame(window)
input_frame.pack(pady=10)

title_entry=tk.Entry(input_frame, width=30)
title_entry.grid(row=0,column=1,padx=10)
description_entry=tk.Entry(input_frame,width=30)
description_entry.grid(row=1,column=1,padx=10)

title_label=tk.Label(input_frame,text="Title")
title_label.grid(row=0,column=0)
description_label=tk.Label(input_frame, text="Description")
description_label.grid(row=1,column=0)

add_button=tk.Button(input_frame,text="Add Task",command=add_item)
add_button.grid(row=2,column=1,pady=10)

tasks_listbox=tk.Listbox(window,width=50,height=10)
tasks_listbox.pack(pady=10)

delete_button=tk.Button(window,text="Delete Task",command=remove_item)
delete_button.pack(pady=10)

window.mainloop()



