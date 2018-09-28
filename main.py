import os
import random
from queue import PriorityQueue
from anytree import NodeMixin
from _collections import deque

class Node(NodeMixin):
    position = ''
    value = ''
    path = []
    # Prebuilt constructor for the nodes at the each state
    def __init__(self, pos, val, path, parent=None):
        super(Node, self).__init__()
        self.position = pos
        self.value = val
        self.path = path
        self.parent = parent


# Generic stack: code taken from http://interactivepython.org/courselib/static/pythonds/BasicDS/ImplementingaStackinPython.html
# Im using this stack as opposed to the precompiled imported one because this code is much cleaner
class Stack:
    def __init__(self):  # initial constructor
        self.items = []

    def isEmpty(self):  # is stack empty?
        return self.items == []

    def push(self, item):  # Pushes item onto stack
        self.items.append(item)

    def pop(self):  # Pops item off stack
        return self.items.pop()

    def peek(self):  # Peeks at the last value added to stack
        return self.items[len(self.items) - 1]

    def size(self):  # Returns size of stack
        return len(self.items)


def main():
    pQueue = PriorityQueue()
    sortedQueue = deque()
    FIFO = deque()
    LIFO = Stack()
    data1 = getRandom()
    data2 = getRandom()
    data3 = getRandom()
    data4 = getRandom()
    dataDiff = []
    for i in range(100):
        dataDiff.append(random.randint(1, 3))
        sortedQueue.append(data1[i])
        FIFO.append(data2[i])
        LIFO.push(data3[i])

    for data in dataDiff:
        pQueue.put(data)
    # print("Priority: ")
    # printPriorityValues(pQueue)

    print("Sorted: ")
    sortedQueue = sorted(sortedQueue)
    printValues(sortedQueue)
    print("FIFO Queue: ")
    printValues(FIFO)
    print("LIFO Queue: ")
    printStackValues(FIFO)
    i = 0
    while i < 100:
        pass

def printValues(queue):
    printout = ''
    while queue:
        printout = printout + " " + str(queue.pop())
    print(printout)


def getRandom():
    data = []
    for i in range (100):
            data.append(random.randint(0, 100))
    return data

def printPriorityValues(pQueue):
    printout = ''
    while pQueue.not_empty:
        printout = printout + " " + str(pQueue.get())
    print(printout)

def printStackValues(stack):
    printout = ''
    while stack:
        printout = printout + " " + str(stack.pop())
    print(printout)

def sortQueue(queue):
    return sorted(queue)

def sortQueue(queue):
    return sorted(queue)

if __name__ == "__main__":
    main()
    pass
