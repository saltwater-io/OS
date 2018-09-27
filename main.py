import os
import random

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

    pQueue = deque()
    sortedQueue = deque()
    queue = deque()
    stack = Stack()
    data1 = getRandom()
    data2 = getRandom()
    data3 = getRandom()
    data4 = getRandom()
    dataDiff = []
    for i in range(100):
            dataDiff.append(random.randint(1, 3))
    dataDiff = sorted(dataDiff)
    for data in dataDiff:
        pQueue.append(data)
    pQueue.reverse()

    print("Priority: ")
    printValues(pQueue)

    print("Sorted: ")
    printValues(sorted())
    pass

def printValues(queue):
    printout = ''
    while queue:
        printout = printout + " " + queue.popleft()
    print(printout)


def getRandom():
    data = []
    for i in range (100):
            data.append(random.randint(0, 100))
    return data

def appendValues():
    pass
def pushValues():
    pass
if __name__ == "__main__":
    main()