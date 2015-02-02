from priority_queue import *
from string_task import *
from node import *

task1 = StringTask(4,'task1')
task2 = StringTask(17, 'task2')
task3 = StringTask(9, 'task3')
task4 = StringTask(9, 'task4')

my_queue = PriorityQueue([task1,task2,task3,task4])
print(str(my_queue))