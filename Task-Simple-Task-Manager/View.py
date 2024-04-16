from prettytable import PrettyTable  # python -m pip install -U prettytable


class View_task:
    def __inint__(self, view):
        self.view = view


def display_tasks(tasks):
    table = PrettyTable()
    table.field_names = ["Task Number", "Task Description", "Task Completion"]

    for index, value in enumerate(tasks):
        table.add_row([index, value.task_description, value.task_status_completed])
    print(table)


def display_report(tasks, deleted_tasks):
    table_complete = PrettyTable()
    table_complete.field_names = ["Task Number", "Task Description"]
    table_incomplete = PrettyTable()
    table_incomplete.field_names = ["Task Number", "Task Description"]
    table_deleted = PrettyTable()
    table_deleted.field_names = ["Task Number", "Task Description", "Task Completion"]

    show_complete = False
    show_incomplete = False

    for index, value in enumerate(tasks):
        if value.task_status_completed:
            show_complete = True
            table_complete.add_row([index, value.task_description])
        else:
            show_incomplete = True
            table_incomplete.add_row([index, value.task_description])

    if show_complete:
        print("------------ Completed Tasks ------------")
        print(table_complete, end="\n")
    if show_incomplete:
        print("------------ Incompleted Tasks ------------")
        print(table_incomplete, end="\n")
    if deleted_tasks:
        print("------------ Deleted Tasks ------------")
        for index, value in enumerate(deleted_tasks):
            table_deleted.add_row(
                [index, value.task_description, value.task_status_completed]
            )
        print(table_deleted, end="\n")
        # print(deleted_tasks)


def display_message(message):
    print(message)


def get_user_input(message):
    return input(message)
