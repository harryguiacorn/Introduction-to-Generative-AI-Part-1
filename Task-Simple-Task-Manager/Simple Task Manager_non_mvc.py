import time
from prettytable import PrettyTable  # python -m pip install -U prettytable

task_status_active = 1

list_tasks = []


class Task:
    def __init__(self):
        self.task_id = None
        self.task_description = None
        self.task_status_completed = False


def create_tasks_in_table(list_tasks):
    """Populate task numbers, descriptions and completion into a table"""
    if list_tasks is None or not len(list_tasks):
        return "The task list is empty."
    table = PrettyTable()

    # Table header
    table.field_names = ["Task Number", "Task Description", "Task Completion"]

    # Populate task numbers and descriptions
    for index, value in enumerate(list_tasks):
        # print(f"{index}, value.task_id, value.task_description")
        table.add_row([index, value.task_description, value.task_status_completed])
    return table


def check_list_task_validity(list_tasks):
    """
    Check if the list is not initiated or no items
    @list_tasks list: list contains tasks
    """
    if list_tasks is None or len(list_tasks) == 0:
        print("The list is empty.")
        return False
    return True


def check_input_isnumeric_isdigit(input: str):
    """Check if the input is numeric or digit
    @input str: user string input"""
    # print(input, type(input), input.isnumeric(), input.isdigit())

    if not input.isnumeric() or not input.isdigit():
        print(f"You entered {input} but it's invalid. Please enter a valid digit.")
        return False
    return True


def task_add():
    """Function for adding a task"""

    print("You have chosen to add a new task")
    input_add_a_task = input("Please enter the task description: ")
    # dict_tasks[len(dict_tasks)] = input_add_a_task
    task_new = Task()
    unix_time_now = int(time.time())

    # Use unit time as a unique task id
    task_new.task_id = unix_time_now
    task_new.task_description = input_add_a_task
    list_tasks.append(task_new)
    print(f"New task: {task_new.task_description} is added")

    # Update table view
    table = create_tasks_in_table(list_tasks)
    print(table)


def task_remove(input_select_a_task):
    """Function for removing a task"""

    print("You have chosen to remove a task.")
    if not check_list_task_validity(list_tasks):
        return

    # Display tasks in table
    table = create_tasks_in_table(list_tasks)
    print(table)

    input_remove_a_task = input("Remove a task by task number: ")

    if not check_list_task_validity(list_tasks):
        return
    if not check_input_isnumeric_isdigit(input_remove_a_task):
        run_task_by_digit(input_select_a_task)
        return
    if int(input_remove_a_task) > len(list_tasks) - 1:
        print("Please enter a valid digit.")
        run_task_by_digit(input_select_a_task)
        return

    # Remove a task by its listing index
    del list_tasks[int(input_remove_a_task)]

    # Display tasks in table
    table = create_tasks_in_table(list_tasks)
    print(table)


def task_mark_complete():
    """Function for marking a task complete"""

    if not check_list_task_validity(list_tasks):
        return

    print("You have chosen to mark a task complete.")

    # Display tasks in table
    table = create_tasks_in_table(list_tasks)
    print(table)

    input_set_a_task_complete = input("Please select a task number to make complete: ")

    if not check_input_isnumeric_isdigit(input_set_a_task_complete):
        return

    if int(input_set_a_task_complete) > len(list_tasks) - 1:
        print("Please enter a valid digit.")
        return
    list_tasks[int(input_set_a_task_complete)].task_status_completed = True

    # Display tasks in table
    table = create_tasks_in_table(list_tasks)
    print(table)


def task_view():
    """Function for viewing tasks"""

    print("You have chosen to view the list", check_list_task_validity(list_tasks))
    if not check_list_task_validity(list_tasks):
        # print("The list is empty.")
        # continue
        return

    table = create_tasks_in_table(list_tasks)
    print(table)


def run_task_by_digit(input_select_a_task):
    """Switch case for user input"""
    match input_select_a_task:
        case "1":
            task_add()
        case "2":
            task_view()
        case "3":
            task_remove(input_select_a_task)
        case "4":
            task_mark_complete()
        case "5":
            print("Exit...")
            exit()
        case _:
            print("Please enter a digit between 1 and 5.")


def run_task_manager():
    while task_status_active == 1:
        try:
            input_select_a_task = input(
                "Please select a task from the following:\n"
                + "1 - Add a task\n"
                + "2 - View tasks\n"
                + "3 - Remove a task\n"
                + "4 - Mark a task as complete\n"
                + "5 - Exit\n"
                + "->"
            )
        except ValueError:
            print("ValueError: Please enter a digit between 1 and 5.")
            continue

        run_task_by_digit(input_select_a_task)


if __name__ == "__main__":
    run_task_manager()
