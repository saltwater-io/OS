import os
import random
from queue import PriorityQueue
from anytree import NodeMixin
from _collections import deque
from src import linkedList


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
    output_first = open("src\\output\\FIRST.txt", 'w')
    output_fifo = open("src\\output\\FIFO.txt", 'w')
    output_lifo = open("src\\output\\LIFO.txt", 'w')
    output_sorted = open("src\\output\\SORTED.txt", 'w')
    output_prority = open("src\\output\\PRIORITY.txt", 'w')

    output_data1 = []
    output_data2 = []
    output_data3 = []
    output_data4 = []

    priority_queue = linkedList.LinkedList()
    sorted_queue = linkedList.LinkedList()
    FIFO = deque()
    LIFO = Stack()

    input1 = 0
    input2 = 0
    input3 = 0
    input4 = 0

    output1 = 0
    output2 = 0
    output3 = 0
    output4 = 0

    clock_in = 0
    clock_out = 0
    # iclock_two = 0
    # oclock_two = 0
    # iclock_three = 0
    # oclock_three = 0
    # iclock_three = 0
    # oclock_three = 0
    # iclock_four = 0
    # oclock_four = 0

    data1 = getRandom(100)
    data2 = getRandom(100)
    data3 = getRandom(100)
    data4 = getRandom(3)

    for i in range(10):
        FIFO.append(data2[i])
        clock_in += 1

    for i in range(10, 100):
        iclock_one = data1[i]
        output_data1.__add__(FIFO.popleft())
        clock_out += 1

        FIFO.append(iclock_one)
        clock_in += 1

    for i in range(1, 10):
        output_data1.__add__(FIFO.popleft())
        clock_out += 1

    print(str(clock_in) + " in " + str(clock_out) + " out")
    format_data('One Register: ', output_data1, output_first)

    output_data1.clear()
    clock_in = 0
    clock_out = 0

    for i in range(10):
        priority_queue.append(data4[i])
        sorted_queue.add_sorted(data1[i])
        FIFO.append(data2[i])
        LIFO.push(data3[i])
        clock_in += 1

    for i in range(10, 100):
        iclock_one = data1[i]
        iclock_two = data2[i]
        iclock_three = data3[i]
        iclock_four = data4[i]

        output_data1.__add__(FIFO.popleft())
        output_data2.__add__(LIFO.pop())
        output_data3.__add__(sorted_queue.pop())
        output_data4.__add__(priority_queue.pop())
        clock_out += 1

        FIFO.append(iclock_one)
        LIFO.push(iclock_two)
        sorted_queue.add_sorted(iclock_three)
        priority_queue.add_sorted(iclock_four)
        clock_in += 1

    for j in range(10):
        output_data1.__add__(FIFO.popleft())
        output_data2.__add__(LIFO.pop())
        output_data3.__add__(sorted_queue.pop())
        output_data4.__add__(priority_queue.pop())
        clock_out += 1

    print(str(clock_in) + " in " + str(clock_out) + " out")

    format_data('FIFO: ', output_data1, output_fifo)
    output_fifo.write(str(clock_in) + " in " + str(clock_out) + " out")

    format_data('LIFO: ', output_data2, output_lifo)
    output_lifo.write(str(clock_in) + " in " + str(clock_out) + " out")

    format_data('Sorted: ', output_data1, output_sorted)
    output_sorted.write(str(clock_in) + " in " + str(clock_out) + " out")

    format_data('Priority: ', output_data2, output_prority)
    output_prority.write(str(clock_in) + " in " + str(clock_out) + " out")



def format_data(name, list, outputFile):
    output = name + "\n"
    count = 0
    for i in list:
        if count % 9 == 0:
            output = output + str(i) + " \n"
        else:
            output = output + str(i) + " "
        count += 1
    outputFile.write(output)


def getRandom(limit):
    data = []
    for i in range(100):
        data.append(random.randint(0, limit))
    return data





if __name__ == "__main__":
    main()
    pass
