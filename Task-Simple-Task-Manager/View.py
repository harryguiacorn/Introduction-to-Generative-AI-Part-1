from prettytable import PrettyTable  # python -m pip install -U prettytable


class View_task:
    def __inint__(self, view):
        self.view = view


def display_tasks(tasks):
    if not tasks:
        display_message("The task list is empty.")
    else:

        print("")
        table = PrettyTable()
        table.field_names = ["Task Number", "Task Description", "Task Completion"]

        for index, value in enumerate(tasks):
            table.add_row([index, value.task_description, value.task_status_completed])
        print(table, end="\n\n")


def filter_incompleted_tasks(tasks):
    list_incompleted_tasks = []
    for index, value in enumerate(tasks):
        if not value.task_status_completed:
            list_incompleted_tasks.append(value)
    return list_incompleted_tasks


def display_report(list_tasks, list_deleted_tasks):
    table_complete = PrettyTable()
    table_complete.field_names = ["Task Number", "Task Description"]
    table_incomplete = PrettyTable()
    table_incomplete.field_names = ["Task Number", "Task Description"]
    table_deleted = PrettyTable()
    table_deleted.field_names = ["Task Number", "Task Description", "Task Completion"]

    show_complete, show_incomplete = False, False

    int_completed_tasks, int_incompleted_tasks = 0, 0

    for index, value in enumerate(list_tasks):
        if value.task_status_completed:
            show_complete = True
            int_completed_tasks += 1
            table_complete.add_row([index, value.task_description])
        else:
            show_incomplete = True
            int_incompleted_tasks += 1
            table_incomplete.add_row([index, value.task_description])

    print("TASK REPORT", end="\n\n")

    if show_complete:
        print("COMPLETED TASKS")
        print(table_complete, end="\n\n")

    if show_incomplete:
        print("INCOMPLETED TASKS")
        print(table_incomplete.get_string(), end="\n\n")

    if list_deleted_tasks:
        print("DELETED TASKS")
        for index, value in enumerate(list_deleted_tasks):
            table_deleted.add_row(
                [index, value.task_description, value.task_status_completed]
            )
        print(table_deleted, end="\n\n")
        # print(deleted_tasks)

    # Print a summary
    print("SUMMARY")
    print(
        f"You have {int_completed_tasks} completed {_get_string_task(int_completed_tasks)}, {int_incompleted_tasks} incompleted {_get_string_task(int_incompleted_tasks)} and {len(list_deleted_tasks)} deleted {_get_string_task(len(list_deleted_tasks))}."
    )


def _get_string_task(num):
    return "task" if num == 1 or num == 0 else "tasks"


def display_message(message):
    print(message, end="\n")


def get_user_input(message):
    return input(message)
