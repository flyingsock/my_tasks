from task_manager import TaskManager
import sys

class UI:

    def __init__(self, task_manager: TaskManager):
        self.task_manager = task_manager

    def check_option(self, answer):
        if answer == 1:
            self.add_option()
        elif answer == 2:
            self.delete_option()
        elif answer == 3:
            self.look_option()
        elif answer == 0:
            self.exit_option()
        else:
            print('?????')
            self.show_menu()

    @staticmethod
    def hello() -> None:
        print('hello, user! welcome to task manager!')

    def show_menu(self):
        print('what do you want?')
        print('1 -- add a task')
        print('2 -- delete a task')
        print('3 -- look my tasks')
        print('0 -- exit')
        answer = int(input())
        self.check_option(answer)

    def add_option(self):
        print('ok, let`s add a task...')
        self.task_manager.add_task(input())
        self.show_menu()

    def look_option(self):

        print('look, here are your tasks...')

        for task in range(1, len(self.task_manager.get_tasks)):
            print('{} -- '.format(task + 1), self.task_manager.get_tasks[task])
        self.show_menu()

    def delete_option(self):

        print('ok, let`s delete a task...')
        print('which task should be deleted?')
        print('enter the task number...')
        deleted = int(input())
        self.task_manager.delete_task(deleted)
        print('task deleted')
        self.show_menu()

    @staticmethod
    def exit_option():
        print('goodbye...')
        sys.exit()

    def run(self):
        self.hello()
        self.show_menu()