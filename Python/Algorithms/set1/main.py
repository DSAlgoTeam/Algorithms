from ll_stack_queue import Stack
from ll_stack_queue import Queue
'''
from list_stack_queue import Stack
from list_stack_queue import Queue
'''

stack = Stack()
queue = Queue()


print(stack.isEmpty())


print(str(stack))
print(str(queue))


stack.push(2)
stack.push(3)
stack.push(3)


queue.push(2)
queue.push(3)
queue.push(2)
queue.push(3)


print(str(stack))
print(stack.isEmpty())


print(str(queue))
print(queue.isEmpty())


stack.pop()
print(stack.top())

queue.pop()
print(queue.top())

stack.pop()
print(str(stack))

queue.pop()
print(str(queue))

stack.pop()
print(str(stack))

queue.pop()
print(str(queue))

stack.push(2)
stack.push(3)
print(str(stack))