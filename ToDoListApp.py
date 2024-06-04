import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
import json


class TodoListApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("To Do List")
        self.geometry("500x500")
        style = Style(theme="flatly")
        style.configure("Custom.TEntry", foreground="gray")

        # Create input field for adding tasks
        self.task_input = tk.Entry(self)
        self.task_input.pack(pady=10)

        ttk.Button(self, text="Add Task", command=self.add_task).pack(pady=5)


        self.task_list = tk.Listbox(self)
        self.task_list.pack(fill=tk.BOTH, expand=True, padx=10,pady=10)

        ttk.Button(self, text="Done", style="success.TButton", command=self.mark_done).pack(side=tk.LEFT, pady=10, padx=10)
        ttk.Button(self, text="Delete", style="danger.TButton", command=self.delete_task).pack(side=tk.RIGHT, padx=10, pady=10)
        ttk.Button(self, text="View Stats", style="info.TButton", command=self.view_stats).pack(side=tk.BOTTOM, pady=10)

        self.load_tasks()




    def add_task(self):
        task = self.task_input.get()
        if task != "Enter your todo here...":
            self.task_list.insert(tk.END, task)
            self.task_list.itemconfig(tk.END, fg="orange")
            self.task_input.delete(0, tk.END)
            self.save_tasks()
    def mark_done(self):
        task_index = self.task_list.curselection()
        if task_index:
            self.task_list.itemconfig(task_index, fg="green")
            self.save_tasks()
    
    def delete_task(self):
        task_index = self.task_list.curselection()
        if task_index:
            self.task_list.delete(task_index)
            self.save_tasks()

    def load_tasks(self):
        try:
            with open("ToDoListApp.json", "r") as f:
                data = json.load(f)
                for task in data:
                    self.task_list.insert(tk.END, task["text"])
                    self.task_list.itemconfig(tk.END, fg=task["color"])
        except FileNotFoundError:
            pass
    
    def save_tasks(self):
        data = []
        for i in range(self.task_list.size()):
            text = self.task_list.get(i)
            color = self.task_list.itemcget(i, "fg")
            data.append({"text": text, "color": color})
        with open("ToDoListApp.json", "w") as f:
            json.dump(data, f)
            
    def view_stats(self):
        done_count = 0
        total_count = self.task_list.size()
        for i in range(total_count):
            if self.task_list.itemcget(i, "fg") == "green":
                done_count += 1
        messagebox.showinfo("Task Statistics", f"Total tasks: {total_count}\nCompleted tasks: {done_count}")




if __name__ == '__main__':
    app = TodoListApp()
    app.mainloop()