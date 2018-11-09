import random
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
    output_first = open("FIRST.txt", 'w')
    output_fifo = open("FIFO.txt", 'w')
    output_lifo = open("LIFO.txt", 'w')
    output_sorted = open("SORTED.txt", 'w')
    output_prority = open("PRIORITY.txt", 'w')

    output_data1 = []
    output_data2 = []
    output_data3 = []
    output_data4 = []

    priority_queue = linkedList.LinkedList()
    sorted_queue = linkedList.LinkedList()
    FIFO = deque()
    LIFO = Stack()


    clock_in = 0
    clock_out = 0

    data0 = getRandom(0, 99)
    data1 = getRandom(0, 99)
    data2 = getRandom(0, 99)
    data3 = getRandom(0, 99)
    data4 = getRandom(1, 3)

    format_data("First input data: ", data0, output_first)
    output_first.write("\n")

    format_data('FIFO input data: ', data1, output_fifo)
    output_fifo.write("\n")

    format_data('LIFO input data: ', data2, output_lifo)
    output_lifo.write("\n")

    format_data('Sorted input data: ', data3, output_sorted)
    output_sorted.write("\n")

    format_data('Priority input data: ', data4, output_prority)
    output_prority.write("\n")

    for i in range(9):
        input1 = data1[i]

        FIFO.append(input1)
        clock_in += 1
        input1 = data2[i]
        LIFO.push(input1)
        clock_in += 1
        input1 = data3[i]
        priority_queue.add_sorted(input1)
        clock_in += 1
        input1 = data4[i]
        sorted_queue.add_sorted(input1)
        clock_in += 1

    for i in range(10, 100):
        output1 = FIFO.popleft()
        output_data1.append(output1)
        clock_out += 1

        output1 = LIFO.pop()
        output_data2.append(output1)
        clock_out += 1

        output1 = sorted_queue.pop()
        output_data3.append(output1)
        clock_out += 1

        output1 = priority_queue.pop_tail()
        output_data4.append(output1)
        clock_out += 1

        input1 = data1[i]
        FIFO.append(input1)
        clock_in += 1
        input1 = data2[i]
        LIFO.push(input1)
        clock_in += 1

        input1 = data3[i]
        sorted_queue.add_sorted(input1)
        clock_in += 1
        input1 = data4[i]
        priority_queue.add_sorted(input1)
        clock_in += 1

    for i in range(9):
        output1 = FIFO.popleft()
        output_data1.append(output1)
        clock_out += 1

        output1 = LIFO.pop()
        output_data2.append(output1)
        clock_out += 1

        output1 = sorted_queue.pop()
        output_data3.append(output1)
        clock_out += 1

        output1 = priority_queue.pop_tail()
        output_data4.append(output1)
        clock_out += 1

 # TODO: START FIX HERE MAKE SURE 1x4x1 above works and prints

    print(str(clock_in) + " in " + str(clock_out) + " out")
    format_data('One Register output: ', output_data1, output_first)

    output_data1.clear()
    clock_in = 0
    clock_out = 0

    for i in range(10):
        input1 = data1[i]
        input2 = data2[i]
        input3 = data3[i]
        input4 = data4[i]

        priority_queue.add_sorted(input4)
        sorted_queue.add_sorted(input3)
        FIFO.append(input1)
        LIFO.push(input2)

        clock_in += 1
    print(len(FIFO))

    for i in range(11, 100):
        input1 = data1[i]
        input2 = data2[i]
        input3 = data3[i]
        input4 = data4[i]

        output1 = FIFO.popleft()
        output2 = LIFO.pop()
        output3 = sorted_queue.pop()
        output4 = priority_queue.pop_tail()
        clock_out += 1

        output_data1.append(output1)
        output_data2.append(output2)
        output_data3.append(output3)
        output_data4.append(output4)

        FIFO.append(input1)
        LIFO.push(input2)
        sorted_queue.add_sorted(input3)
        priority_queue.add_sorted(input4)
        clock_in += 1
    print(len())
    for j in range(9):
        output1 = FIFO.popleft()
        output2 = LIFO.pop()
        output3 = sorted_queue.pop()
        output4 = priority_queue.pop_tail()

        output_data1.append(output1)
        output_data2.append(output2)
        output_data3.append(output3)
        output_data4.append(output4)
        clock_out += 1

    print(str(clock_in) + " in " + str(clock_out) + " out")

    format_data('FIFO output data: ', output_data1, output_fifo)
    output_fifo.write("\n" + str(clock_in) + " in " + str(clock_out) + " out")

    format_data('LIFO: output data:  ', output_data2, output_lifo)
    output_lifo.write("\n" + str(clock_in) + " in " + str(clock_out) + " out")

    format_data('Sorted output data: ', output_data3, output_sorted)
    output_sorted.write("\n"+str(clock_in) + " in " + str(clock_out) + " out")

    format_data('Priority output data: ', output_data4, output_prority)

    output_prority.write("\n" + str(clock_in) + " in " + str(clock_out) + " out")


def format_data(name, list, outputFile):
    output = name + "\n"
    count = 1
    for i in list:
        if count % 10 == 0:
            output = output + str(i) + " \n"
        else:
            output = output + str(i) + " "
        count += 1
    outputFile.write(output)


def getRandom(start, limit):
    data = []
    for i in range(100):
        data.append(random.randint(start, limit))
    return data


if __name__ == "__main__":
    main()
    pass
