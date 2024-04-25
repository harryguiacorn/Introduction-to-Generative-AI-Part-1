import controller


class App:
    def __init__(self):
        self.controller = controller

    def run(self):
        self.controller.run_task_manager()


if __name__ == "__main__":
    app = App()
    app.run()
