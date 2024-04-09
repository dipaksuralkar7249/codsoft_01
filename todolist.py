import tkinter as tk
from tkinter import messagebox


class ToDoListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=0, column=2, padx=5, pady=5)

        self.task_listbox = tk.Listbox(root, width=40, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index]
        except IndexError:
            messagebox.showwarning("Warning", "No task selected.")


def main():
    root = tk.Tk()
    todo_list_gui = ToDoListGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
