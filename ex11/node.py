class Node:
    def __init__(self, task, next = None):
        self._task = task
        self._next = next
    
    def get_priority(self):
        return self._task.get_priority()

    def set_priority(self, new_priority):
        self._task.set_priority(new_priority)

    def get_task(self):
        return self._task

    def get_next(self):
        return self._next

    def set_next(self, next):
        self._next = next

    def has_next(self):
        return True if self._next else False
