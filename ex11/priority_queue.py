from node import *

class PriorityQueue:

    def __init__(self, tasks = []):
        self._head = None
        self._size = 0
        self._curr_node = self._head
        for task in tasks:
            self.enque(task)

    def enque(self, task):
        if not task: return

        self._size += 1
        if not self._head:
            self._change_head(Node(task))
            return
        
        curr_node = self._head
        prev_node = None
        target_priority = task.get_priority()
        
        while curr_node:
            curr_priority = curr_node.get_priority()
            if curr_priority >= target_priority:
                prev_node = curr_node
            else:
                break
            curr_node = curr_node.get_next()
        ### while loop end ###
        
        new_task = Node(task, curr_node)
        if prev_node:
            prev_node.set_next(new_task)
        else:
            self._change_head(new_task)

    def peek(self):
        if self._head:
            task = self._head.get_task()
        else:
            task = None
        return task

    def deque(self):
        task = self._head
        if task:
            self._size -= 1
            next_node = self._head.get_next()
            task = task.get_task()
            self._change_head(next_node)
        return task

    def get_head(self):
        return self._head

    def _change_head(self, node):
        if self._curr_node == self._head:
            self._curr_node = node
        self._head = node

    def change_priority(self, old, new):
        curr_node = self._head
        prev_node = None
        while curr_node:
            curr_priority = curr_node.get_priority()
            if curr_priority == old:
                if prev_node:
                    prev_node.set_next(curr_node.get_next())
                else:
                    self._change_head(curr_node.get_next())
                curr_node.set_priority(new)
                self._size -= 1
                self.enque( curr_node.get_task() )
                return
            else:
                prev_node = curr_node
            curr_node = curr_node.get_next()

    def __len__(self):
        return self._size

    def __iter__(self):
        return self

    def __next__(self):
        if not self._curr_node:
            self._curr_node = self._head
            raise StopIteration
        else:
            task = self._curr_node.get_task()
            self._curr_node = self._curr_node.get_next()
            return task
    
    def __str__(self):
        LIST_OPEN = '['
        LIST_CLOSE = ']'
        out_str = LIST_OPEN
        my_queue = PriorityQueueIterator(self)
        for task in my_queue:
            if not task: break
            out_str += str(task) if out_str == LIST_OPEN else ', ' + str(task)
        out_str += LIST_CLOSE
        return out_str

    def __add__(self,other):
        my_queue = PriorityQueueIterator(self)
        other_queue = PriorityQueueIterator(other)
        out_queue = PriorityQueue()
        for task in my_queue:
            out_queue.enque(task)
        for task in other_queue:
            out_queue.enque(task)

        return out_queue

    def __eq__(self, other):
        is_eq = True
        my_queue = PriorityQueueIterator(self)
        other_queue = PriorityQueueIterator(other)
        for other_task in other_queue:
            my_task = next(my_queue)
            if my_task != other_task:
                is_eq = False
                break

        return is_eq


class PriorityQueueIterator:
    def __init__(self, queue):
        self._queue = queue
        self._curr_node = self._queue.get_head()

    def __iter__(self):
        return self

    def __next__(self):
        if not self._curr_node:
            raise StopIteration
        else:
            task = self._curr_node.get_task()
            self._curr_node = self._curr_node.get_next()
            return task

    def has_next(self):
        has_next = False
        if self._curr_node:
            has_next = self._curr_node.has_next()
        return has_next