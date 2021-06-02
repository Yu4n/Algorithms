stack = []

stack.append(12)
print(stack.pop())
try:
    print(stack.pop())
except IndexError:
    print("stack underflow!")
else:
    print("done!")


queue = []
queue.append('apple')
queue.append('orange')
queue.append('mango')
queue.append('mango')

first_item = queue.pop(0)
print(first_item)
print(queue[0])
