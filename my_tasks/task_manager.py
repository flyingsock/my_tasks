class TaskManager:
    tasks: list[str] = []

    @property
    def get_tasks(self) -> list[str]:
        return self.tasks

    def add_task(self, task: str) -> None:
        self.tasks.append(task)

        f = open('tasks.txt', 'w')
        for task in range(len(self.tasks)):
            f.write(f'{str(task + 1)}: ' + self.tasks[task] + '\n')
        f.close()

    def delete_task(self, number):
        self.tasks.pop(number - 1)
        f = open('tasks.txt', 'w')
        for task in range(len(self.tasks)):
            f.write(f'{str(task + 1)}: ' + self.tasks[task] + '\n')
        f.close()