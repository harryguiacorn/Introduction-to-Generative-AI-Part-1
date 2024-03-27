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


def display_message(message):
    print(message)


def get_user_input(message):
    return input(message)
