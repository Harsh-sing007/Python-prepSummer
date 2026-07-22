# some_dict={'zope':'zzz','python':'program'}
# another_dict={'java':'program','pearl':'ship'}

# print("intersects"),filter(another_dict.keys(),some_dict.keys())
# from collections import deque

# def search(lines, pattern, history=5):
#     previous_lines = deque(maxlen=history)
#     for line in lines:
#         if pattern in line:
#             yield line, previous_lines
#         previous_lines.append(line)
# import heapq

# class priorityQueue:
#     def __init__(self):
#         self._queue = []
#         self._index = 0

#     def push(self, item, priority):
#         heapq.heappush(self._queue, (-priority, self._index, item))
#         self._index += 1

#     def pop(self):
#         return heapq.heappop(self._queue)[-1]
def display(*args):
    print("The entered values are:")
    for value in args:
        print(value)

 n = int(input("Enter the number of variables: "))

values = []
for i in range(n):
    x = input(f"Enter value {i + 1}: ")
    values.append(x)

display(*values)