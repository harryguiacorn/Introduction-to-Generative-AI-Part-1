class Model_task:
    def __init__(self, task_id, task_description, task_status_completed=False):
        self.task_id = task_id
        self.task_description = task_description
        self.task_status_completed = task_status_completed
        # self.task_list = task_list

    def set_completed(self):
        self.task_status_completed = True
