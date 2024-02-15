from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry  # Import DateEntry from tkcalendar
import tkinter.messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do List')
        self.root.geometry('400x500')

        self.label = Label(self.root, text="To-Do List App", font='Arial 18 bold', bg='yellow', fg='black')
        self.label.pack(side=TOP, fill=BOTH)

        self.task_entry = Entry(self.root, font='Arial 12')
        self.task_entry.pack(side=TOP, fill=X, padx=10, pady=5)

        self.priority_label = Label(self.root, text="Priority:", font='Arial 12')
        self.priority_label.pack(side=TOP, padx=10, pady=5)

        self.priority_var = StringVar()
        self.priority_combobox = ttk.Combobox(self.root, textvariable=self.priority_var, values=["High", "Medium", "Low"])
        self.priority_combobox.pack(side=TOP, fill=X, padx=10, pady=5)
        self.priority_combobox.set("Medium")  # Default priority

        self.due_date_label = Label(self.root, text="Due Date:", font='Arial 12')
        self.due_date_label.pack(side=TOP, padx=10, pady=5)

        self.due_date_entry = DateEntry(self.root, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.due_date_entry.pack(side=TOP, fill=X, padx=10, pady=5)

        self.add_button = Button(self.root, text='Add Task', command=self.add_task, font='Arial 12', bg='green', fg='white')
        self.add_button.pack(side=TOP, pady=5)

        self.task_listbox = Listbox(self.root, font='Arial 12', selectbackground='lightblue', selectmode=SINGLE)
        self.task_listbox.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)

        self.complete_button = Button(self.root, text='Mark as Completed', command=self.mark_as_completed, font='Arial 12', bg='blue', fg='white')
        self.complete_button.pack(side=TOP, pady=5)

        self.delete_button = Button(self.root, text='Delete Task', command=self.delete_task, font='Arial 12', bg='red', fg='white')
        self.delete_button.pack(side=TOP, pady=5)

        self.clear_button = Button(self.root, text='Clear All Tasks', command=self.clear_all_tasks, font='Arial 12', bg='orange', fg='white')
        self.clear_button.pack(side=TOP, pady=5)

        self.save_button = Button(self.root, text='Save Tasks', command=self.save_tasks, font='Arial 12', bg='purple', fg='white')
        self.save_button.pack(side=TOP, pady=5)

        # Load saved tasks from a file (if any)
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        priority = self.priority_var.get()
        due_date = self.due_date_entry.get()

        if task and priority and due_date:
            task_with_details = f"{task} - Priority: {priority}, Due Date: {due_date}"
            self.task_listbox.insert(END, task_with_details)
            self.task_entry.delete(0, END)

    def mark_as_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.itemconfig(selected_index, {'bg': 'lightgrey', 'fg': 'grey'})

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)

    def clear_all_tasks(self):
        confirmed = tkinter.messagebox.askyesno("Clear All Tasks", "Are you sure you want to clear all tasks?")
        if confirmed:
            self.task_listbox.delete(0, END)

    def save_tasks(self):
        tasks = self.task_listbox.get(0, END)
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                tasks = [line.strip() for line in file.readlines()]
                self.task_listbox.delete(0, END)
                for task in tasks:
                    self.task_listbox.insert(END, task)
        except FileNotFoundError:
            pass

def main():
    root = Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
