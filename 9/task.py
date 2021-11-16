from note import Note
from datetime import datetime

class Task:
    id = 1

    def __init__(self, name, note=None, due_date=None):
        self.name = name
        self.creation_date = datetime.today()
        self.status = "unfinished"
        self.message = Note(note) if note is not None else None
        self.due_date = due_date if due_date is not None else None
        self.id = Task.id
        Task.id += 1

    def getName(self):
        return f'{self.name}'

    def getMessage(self):
        return f'{self.message}'

    def setMessage(self, new_message):
        self.message = Note(new_message)
        return f'{self.message.message}'

    def setStatus(self, new_status):
        valid_status = [
            'unfinished',
            'in process',
            'finished'
        ]
        if new_status.lower() not in valid_status:
            raise NotValidStatus
        self.status= new_status
        return self.status


class NotValidStatus(Exception):
    pass

class TaskNotFound(Exception):
    pass
        