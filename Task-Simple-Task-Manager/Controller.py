from Model import Model_task
from View import display_tasks, display_message, display_report, get_user_input
import time
import copy

task_list = []
task_list_deleted = []


def add_task():
    """Function for adding a task"""

    print("You have chosen to add a new task")
    task_description = get_user_input("Please enter the task description: ")

    # Use unit time as a unique task id
    unix_time_now = int(time.time())
    new_task = Model_task(unix_time_now, task_description)

    task_list.append(new_task)

    display_message(f"New task: {task_description} is added")
    display_tasks(task_list)


def remove_task():
    """Function for removing a task"""

    print("You have chosen to remove a task.")

    if not task_list:
        display_message("The task list is empty.")
        return

    display_tasks(task_list)

    while True:
        task_number = get_user_input("Remove a task by task number: ")
        if not task_number.isdigit():
            display_message("Please enter a valid digit.")
            continue
        task_number = int(task_number)
        if task_number >= len(task_list):
            display_message("Please enter a valid task number.")
            continue
        task_list_deepcopy = copy.deepcopy(task_list)
        task_list_deleted.append(task_list_deepcopy[task_number])
        del task_list[task_number]
        display_tasks(task_list)
        break


def mark_task_complete():
    """Function for marking a task complete"""

    if not task_list:
        display_message("The task list is empty.")
        return

    print("You have chosen to mark a task complete.")

    display_tasks(task_list)
    while True:
        task_number = get_user_input("Please select a task number to mark complete: ")
        if not task_number.isdigit():
            display_message("Please enter a valid digit.")
            continue
        task_number = int(task_number)
        if task_number >= len(task_list):
            display_message("Please enter a valid task number.")
            continue
        task_list[task_number].set_completed()
        display_tasks(task_list)
        break


def view_tasks():
    """Function for viewing tasks"""

    if not task_list:
        display_message("The task list is empty.")
        return
    display_tasks(task_list)


def create_report():
    """Function for creating a report"""

    if not task_list:
        display_message("The task list is empty.")
        return
    display_report(task_list, task_list_deleted)


def run_task_manager():
    while True:
        display_message(
            """
      Please select a task from the following:
      1 - Add a task
      2 - View tasks
      3 - Remove a task
      4 - Mark a task as complete
      5 - Report
      6 - Exit
    """
        )
        user_input = get_user_input("-> ")
        if user_input not in ("1", "2", "3", "4", "5", "6"):
            display_message("Please enter a digit between 1 and 6.")
            continue
        if user_input == "1":
            add_task()
        elif user_input == "2":
            view_tasks()
        elif user_input == "3":
            remove_task()
        elif user_input == "4":
            mark_task_complete()
        elif user_input == "5":
            create_report()
        else:
            display_message("Exit...")
            break


if __name__ == "__main__":
    run_task_manager()
