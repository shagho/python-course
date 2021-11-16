import sys

from task import Task, TaskNotFound, NotValidStatus
from task_container import TaskContainer


class Menu:

    def __init__(self):
        self.task_container = TaskContainer()
        self.choices = {
            1: self.add_new_task,
            2: self.change_task,
            3: self.delete_task,
            4: self.search_task,
            5: self.search_task_by_word,
            6: self.edit_task_status,
            7: self.edit_task_note,
            8: self.show_finished_tasks,
            9: self.show_unfinished_tasks_with_due_date,
            10: self.show_all_tasks,
            11: self.show_task_note,
            12: self.quit
        }
        
    def run(self):
        while True:
            self.display_menu()
            choice = int(input("choice an option: "))
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{} is not a valid choice, Try again.".format(choice))

    def _get_task(self,id):
        task = self.task_container.tasks.get(id)
        return task

    def add_new_task(self):
        task_name = input("Task name: ")
        message = input("Add a message: ")
        due_date = input("Due date: ")
        task = self.task_container.new_task(task_name, message, due_date)
        return task

    def change_task(self):
        id = int(input("Task ID: "))
        new_task_name = input("Edited task: ")
        changed_task = self.task_container.edit_task(id, new_task_name)
        return changed_task

    def delete_task(self):
        id = int(input("Task ID: "))
        self.task_container.del_task(id)

    def search_task(self):
        id = int(input("Task ID: "))
        task_name = self.task_container.search_by_id(id)
        print(task_name)
        return task_name

    def search_task_by_word(self):
        word = input("Type word to be matched: ")
        matches = self.task_container.search_by_word(word)
        for match in matches:
            print(match)
        return matches

    def edit_task_status(self):
        id = int(input("Task ID: "))
        print("""
        Available status:
        Unfinished
        In process
        Finished
        """)
        new_status = input("Type new status: ")
        changed_status = self.task_container.change_task_status(id, new_status)

    def edit_task_note(self):
        id = int(input("Task ID: "))
        new_note = input("new note: ")
        self.task_container.edit_note(id, new_note)

    def show_finished_tasks(self):
        finished = []
        for id, task in self.task_container.tasks.items():
            if task.status == "finished":
                finished.append(task.name)

        for task_name in finished:
            print(task_name)
        return finished

    def show_unfinished_tasks_with_due_date(self):
        unfinished_due_date = []
        for id, task in self.task_container.tasks.items():
            if task.status == "unfinished":
                unfinished_due_date.append((task.name, task.due_date))

        for task, due_date in unfinished_due_date:
            print(task, "-", due_date)
        
        return unfinished_due_date

    def show_all_tasks(self):
        for id, task in self.task_container.tasks.items():
            print(task.id, "-", task.name)

    def show_task_note(self):
        id = int(input("Task ID: "))
        task = self._get_task(id)
        print(task.getMessage())
        return task.getMessage()

    def quit(self):
        sys.exit(0)

    def display_menu(self):
        print("""
        1: Add new task
        2: Edit a task
        3: Delete a task
        4: Search a task by id
        5: search a task by a word
        6: Edit a task status
        7: Edit a task note
        8: show all finished tasks
        9: show all unfinished tasks
        10: show all tasks
        11: show note to a task
        12: Quit
        """)