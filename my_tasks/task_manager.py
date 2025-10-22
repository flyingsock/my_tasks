class TaskManager:
    tasks: list[str] = []

    @property
    def get_tasks(self) -> list[str]:
        return self.tasks

    def add_task(self, task: str) -> None:
        self.tasks.append(task)
