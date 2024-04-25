import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import *
import time
import copy


# Task class
class Task:

    def __init__(self, task_id, description, status):
        self.task_id = task_id
        self.description = description
        self.status = status


# Popup for task modification
class ModifyDialog(simpledialog.Dialog):

    def __init__(self, parent, title, task):
        self.task = task  # Current task details
        super().__init__(parent, title)

    def body(self, master):

        tk.Label(master, text="Description:").grid(row=0)
        tk.Label(master, text="Status:").grid(row=1)

        self.description_entry = tk.Entry(master)
        self.status_entry = tk.Entry(master)

        # Set the current task details in the entry fields
        self.description_entry.insert(0, self.task.description)
        self.status_entry.insert(0, self.task.status)

        self.description_entry.grid(row=0, column=1)
        self.status_entry.grid(row=1, column=1)

        return self.description_entry

    def apply(self):
        self.result = (self.description_entry.get(), self.status_entry.get())


# GUI application
class TaskManagerApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Simple Task Manager")
        self.geometry("400x360")
        self.tasks = []
        self.tasks_deleted = []
        self.create_components()

    def create_components(self):

        # create labels for task description and status
        tk.Label(
            self,
            text="Let us know what needs to be done, then click 'Add Task' to keep track!",
        ).grid(row=0, column=0, columnspan=3, padx=5, pady=5)
        tk.Label(self, text="Description:").grid(row=1, padx=0, pady=5, sticky="E")
        tk.Label(self, text="Status:").grid(row=2, padx=0, pady=5, sticky="E")

        # create entry for Description
        self.task_entry = tk.Entry(self)
        self.task_entry.grid(row=1, column=1)

        # create entry for Status
        self.status_entry = tk.Entry(self)
        self.status_entry.grid(row=2, column=1)

        # create Submit button
        self.add_button = tk.Button(self, text="Add Task", command=self.add_task)
        # self.add_button.grid(row=3, columnspan=3)
        self.add_button.grid(row=1, rowspan=2, column=2)

        # tk.Label(self, text="").grid(row=4, column=0, columnspan=3, padx=5, pady=5)
        tk.Label(self, text="Tasks", font="Bold 14").grid(
            row=5, column=0, columnspan=3, padx=5, pady=5
        )

        # Create a frame to contain the Listbox and Scrollbars
        frame = tk.Frame(self)
        frame.grid(row=6, columnspan=3)

        # Task list
        self.task_listbox = tk.Listbox(frame, width=50, height=10)
        self.task_listbox.grid(row=6, column=0)

        # Vertical Scrollbar for Listbox
        v_scrollbar = tk.Scrollbar(
            frame, orient="vertical", command=self.task_listbox.yview
        )
        v_scrollbar.grid(row=6, column=1, sticky="ns")

        # Horizontal Scrollbar for Listbox
        h_scrollbar = tk.Scrollbar(
            frame, orient="horizontal", command=self.task_listbox.xview
        )
        h_scrollbar.grid(row=7, column=0, sticky="ew")

        # Configure the Listbox to update the Scrollbars
        self.task_listbox.config(
            yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set
        )

        # Modify task button
        self.btn_modify = tk.Button(self, text="Modify Task", command=self.modify_task)
        self.btn_modify.grid(row=8, column=0)

        # Remove task button
        self.btn_remove = tk.Button(self, text="Remove Task", command=self.remove_task)
        self.btn_remove.grid(row=8, column=1)

        # Report button
        self.btn_report = tk.Button(
            self, text="Create Report", command=self.create_report
        )
        self.btn_report.grid(row=8, column=2)

    def add_task(self):
        description = self.task_entry.get()
        status = self.status_entry.get()
        if description and status:
            # Use unit time as a unique task id
            unix_time_now = int(time.time())
            task = Task(unix_time_now, description, status)
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
            self.status_entry.delete(0, tk.END)
        else:
            messagebox.showwarning(
                "Warning", "Please enter both description and status."
            )

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, f"{task.description} - {task.status}")

    def remove_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]

            # Make a deep copy to retain task details before deletion
            task_list_deepcopy = copy.deepcopy(self.tasks[task_index])
            self.tasks_deleted.append(task_list_deepcopy)

            del self.tasks[task_index]

            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def modify_task(self):
        try:
            # Parse selected task details
            task_index = self.task_listbox.curselection()[0]
            task = self.tasks[task_index]

            # Open pop up with parsed data
            dialog = ModifyDialog(self, "Modify Task", task)

            if dialog.result:
                new_description, new_status = dialog.result
                if new_description and new_status:
                    # Update task details
                    task.description = new_description
                    task.status = new_status
                    self.update_task_listbox()
                else:
                    messagebox.showwarning(
                        "Warning", "Both description and status must not be empty."
                    )
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to modify.")

    def create_report(self):
        if self.tasks:
            # Create the pop-up window
            popup = tk.Toplevel()
            popup.title("Task Report")

            # Create a canvas and attach vertical and horizontal scrollbars to it
            canvas = tk.Canvas(popup)
            v_scrollbar = tk.Scrollbar(popup, orient="vertical", command=canvas.yview)
            h_scrollbar = tk.Scrollbar(popup, orient="horizontal", command=canvas.xview)
            canvas.configure(
                yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set
            )

            # Grid the canvas and scrollbars
            canvas.grid(row=0, column=0, sticky="nsew")
            v_scrollbar.grid(row=0, column=1, sticky="ns")
            h_scrollbar.grid(row=1, column=0, sticky="ew")

            # Create a frame inside the canvas
            frame = tk.Frame(canvas)
            canvas.create_window((0, 0), width=400, window=frame, anchor="nw")

            # Display completed tasks
            tk.Label(frame, text="Active Tasks:", font=("50")).pack()
            if not self.tasks:
                tk.Label(frame, text="No Active Tasks", wraplength=400).pack()
            else:
                for task in self.tasks:
                    txt = task.description + " - " + task.status
                    tk.Label(frame, text=txt, wraplength=400).pack()

            tk.Label(frame, text="\n---------------------------------\n").pack()

            # Display incomplete tasks
            tk.Label(frame, text="Deleted Tasks:", font=("50")).pack()
            if not self.tasks_deleted:
                tk.Label(frame, text="No Deleted Tasks", wraplength=400).pack()
            else:
                for task in self.tasks_deleted:
                    txt = task.description + " - " + task.status
                    tk.Label(frame, text=txt, wraplength=400).pack()

            tk.Label(frame, text="\n---------------------------------\n").pack()
            tk.Label(frame, text="Summary", font=("50")).pack()
            tk.Label(
                frame,
                text=f"You have {len(self.tasks)} active {self._get_string_task(len(self.tasks))} and {len(self.tasks_deleted)} deleted {self._get_string_task(len(self.tasks_deleted))}.",
                wraplength=400,
            ).pack()
            # Update the scrollregion of the canvas to encompass the frame
            frame.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))

        else:
            messagebox.showwarning("Warning", "Please add a task first.")

    def _get_string_task(self, num):
        return "task" if num == 1 or num == 0 else "tasks"


def main():
    app = TaskManagerApp()
    app.mainloop()


if __name__ == "__main__":
    main()
