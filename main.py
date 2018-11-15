# This is a simulated operating systems project for CSC306 - Operating Systems
# At The University of Southern Mississippi
# Written by: Dakota McGuire 11/15/18
#
import random
from _collections import deque
from src import linkedList
import heapq as heap


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


# Main method
def main():

    # Files to output the data to
    ONE_REGISTER_OUTPUT = open("ONE_REG.txt", 'w')  # One register
    FOUR_REGISTER_OUTPUT = open("FOUR_REG.txt", 'w')  # 4 Registers
    INTPUT_DATA = open("INPUT.txt", 'w')  # Input data used
    ONE_TO_FOUR = open("ONE_TO_FOUR_REG.txt", 'w')  # One input register, 4 output registers
    FOUR_TO_ONE = open("FOUR_TO_ONE_REG.txt", 'w')  # Four input registers, one output register

    # Output data
    output_data1 = []
    output_data2 = []
    output_data3 = []
    output_data4 = []

    # Queues to be populated and used
    priority_queue = []
    sorted_queue = linkedList.LinkedList()
    FIFO = deque()
    LIFO = Stack()

    # Input and output registers
    clock_in = 0
    clock_out = 0

    # Data to be used - @ params low - high values
    data_priority = get_random(0, 99)
    data_fifo = get_random(0, 99)
    data_lifo = get_random(0, 99)
    data_sorted = get_random(0, 99)
    priority_num = get_random(1, 3)

#   Prints and formats input data to output file
    format_data('FIFO input data: ', data_fifo, INTPUT_DATA)
    INTPUT_DATA.write("\n")
    INTPUT_DATA.write("\n")

    format_data('LIFO input data: ', data_lifo, INTPUT_DATA)
    INTPUT_DATA.write("\n")
    INTPUT_DATA.write("\n")

    format_data('Sorted input data: ', data_sorted, INTPUT_DATA)
    INTPUT_DATA.write("\n")
    INTPUT_DATA.write("\n")

    format_data('Priority input data: ', data_priority, INTPUT_DATA)
    INTPUT_DATA.write("\n")
    INTPUT_DATA.write("\n")
    count = 0

    # One register input - One register output
    for i in range(9):
        # Adds to queue
        input1 = data_fifo[i]
        FIFO.append(input1)
        clock_in += 1

        # Adds to stack
        input1 = data_lifo[i]
        LIFO.push(input1)
        clock_in += 1

        # Adds to Sorted Queue
        input1 = data_sorted[i]
        sorted_queue.add_sorted(input1)
        clock_in += 1

        # Adds to Priority queue
        input1 = data_priority[i]
        heap.heappush(priority_queue, (priority_num[i], count, input1))
        count += 1
        clock_in += 1

    for i in range(9, 100):
        # FIFO output
        output1 = FIFO.popleft()
        output_data1.append(output1)
        clock_out += 1

        # LIFO output
        output1 = LIFO.pop()
        output_data2.append(output1)
        clock_out += 1

        # Sorted output
        output1 = sorted_queue.pop()
        output_data3.append(output1)
        clock_out += 1

        # Priority Output
        output1 = heap.heappop(priority_queue)[2]
        output_data4.append(output1)
        clock_out += 1

        # FIFO input
        input1 = data_fifo[i]
        FIFO.append(input1)
        clock_in += 1

        # LIFO input
        input1 = data_lifo[i]
        LIFO.push(input1)
        clock_in += 1

        # Sorted input
        input1 = data_sorted[i]
        sorted_queue.add_sorted(input1)
        clock_in += 1

        # Priority Input
        input1 = data_priority[i]
        heap.heappush(priority_queue, (priority_num[i], count, input1))
        count += 1
        clock_in += 1

    for i in range(9):
        # FIFO output
        output1 = FIFO.popleft()
        output_data1.append(output1)
        clock_out += 1

        # LIFO output
        output1 = LIFO.pop()
        output_data2.append(output1)
        clock_out += 1

        # Sorted output
        output1 = sorted_queue.pop()
        output_data3.append(output1)
        clock_out += 1

        # Priority output
        output1 = heap.heappop(priority_queue)[2]
        output_data4.append(output1)
        clock_out += 1


    print(str(clock_in) + " in " + str(clock_out) + " out")
    format_data('FIFO Output Data: ', output_data1, ONE_REGISTER_OUTPUT)
    ONE_REGISTER_OUTPUT.write("\n")
    ONE_REGISTER_OUTPUT.write("\n")

    format_data('LIFO Output Data: ', output_data2, ONE_REGISTER_OUTPUT)
    ONE_REGISTER_OUTPUT.write("\n")
    ONE_REGISTER_OUTPUT.write("\n")

    format_data('Sorted Output Data: ', output_data3, ONE_REGISTER_OUTPUT)
    ONE_REGISTER_OUTPUT.write("\n")
    ONE_REGISTER_OUTPUT.write("\n")

    format_data('Priority Output Data: ', output_data4, ONE_REGISTER_OUTPUT)
    ONE_REGISTER_OUTPUT.write("\n")
    ONE_REGISTER_OUTPUT.write("\n" + str(clock_in) + " in " + str(clock_out) + " out")

    # Clearing output data for next run
    output_data1.clear()
    output_data2.clear()
    output_data3.clear()
    output_data4.clear()

    clock_in = 0
    clock_out = 0
    count = 0

# This a 4 register input - 4 Register Output
    for i in range(9):
        input1 = data_fifo[i]
        input2 = data_lifo[i]
        input3 = data_sorted[i]
        input4 = data_priority[i]
        # FIFO input
        FIFO.append(input1)
        LIFO.push(input2)
        sorted_queue.add_sorted(input3)
        # Priority Input
        heap.heappush(priority_queue, (priority_num[i], count, input4))
        count += 1
        clock_in += 1

    for i in range(9, 100):
        # Register inputs
        input1 = data_fifo[i]
        input2 = data_lifo[i]
        input3 = data_sorted[i]
        input4 = data_priority[i]

        # FIFO, LIFO, sorted, and priority output to output registers
        output1 = FIFO.popleft()
        output2 = LIFO.pop()
        output3 = sorted_queue.pop()
        output4 = heap.heappop(priority_queue)[2]
        clock_out += 1

        # Stores output data from register
        output_data1.append(output1)
        output_data2.append(output2)
        output_data3.append(output3)
        output_data4.append(output4)

        # FIFO, LIFO, sorted, and priority input from input registers
        FIFO.append(input1)
        LIFO.push(input2)
        sorted_queue.add_sorted(input3)
        heap.heappush(priority_queue, (priority_num[i], count, input4))
        count += 1
        clock_in += 1

    for j in range(9):
        # FIFO, LIFO, sorted, and priority output to output registers
        output1 = FIFO.popleft()
        output2 = LIFO.pop()
        output3 = sorted_queue.pop()
        output4 = heap.heappop(priority_queue)[2]

        # Stores output data from register
        output_data1.append(output1)
        output_data2.append(output2)
        output_data3.append(output3)
        output_data4.append(output4)
        clock_out += 1


    print(str(clock_in) + " in " + str(clock_out) + " out")

    format_data('FIFO output data: ', output_data1, FOUR_REGISTER_OUTPUT)
    FOUR_REGISTER_OUTPUT.write("\n")
    FOUR_REGISTER_OUTPUT.write("\n")

    format_data('LIFO output data: ', output_data2, FOUR_REGISTER_OUTPUT)
    FOUR_REGISTER_OUTPUT.write("\n")
    FOUR_REGISTER_OUTPUT.write("\n")

    format_data('Sorted output data: ', output_data3, FOUR_REGISTER_OUTPUT)
    FOUR_REGISTER_OUTPUT.write("\n")
    FOUR_REGISTER_OUTPUT.write("\n")

    format_data('Priority output data: ', output_data4, FOUR_REGISTER_OUTPUT)
    FOUR_REGISTER_OUTPUT.write("\n")

    FOUR_REGISTER_OUTPUT.write("\n" + str(clock_in) + " in " + str(clock_out) + " out")

    # Clearing output data for next run
    output_data1.clear()
    output_data2.clear()
    output_data3.clear()
    output_data4.clear()

    clock_in = 0
    clock_out = 0
    count = 0

#   One input register, 4 output registers
    for i in range(9):
        #FIFO input
        input1 = data_fifo[i]
        FIFO.append(input1)
        clock_in += 1

        # LIFO input
        input1 = data_lifo[i]
        LIFO.push(input1)
        clock_in += 1

        # Sorted input
        input1 = data_sorted[i]
        sorted_queue.add_sorted(input1)
        clock_in += 1

        # Priority Input
        input1 = data_priority[i]
        heap.heappush(priority_queue, (priority_num[i], count, input1))
        count += 1
        clock_in += 1

    for i in range(9, 100):
        # FIFO, LIFO, sorted, and priority output to output registers
        output1 = FIFO.popleft()
        output2 = LIFO.pop()
        output3 = sorted_queue.pop()
        output4 = heap.heappop(priority_queue)[2]

        # Stores output data from register
        output_data1.append(output1)
        output_data2.append(output2)
        output_data3.append(output3)
        output_data4.append(output4)
        clock_out += 1

        # FIFO input
        input1 = data_fifo[i]
        FIFO.append(input1)
        clock_in += 1

        # LIFO input
        input1 = data_lifo[i]
        LIFO.push(input1)
        clock_in += 1

        # Sorted input
        input1 = data_sorted[i]
        sorted_queue.add_sorted(input1)
        clock_in += 1

        # Priority Input
        input1 = data_priority[i]
        heap.heappush(priority_queue, (priority_num[i], count, input1))
        count += 1
        clock_in += 1

    for i in range(9):
        # FIFO, LIFO, sorted, and priority output to output registers
        output1 = FIFO.popleft()
        output2 = LIFO.pop()
        output3 = sorted_queue.pop()
        output4 = heap.heappop(priority_queue)[2]

        # Stores output data from register
        output_data1.append(output1)
        output_data2.append(output2)
        output_data3.append(output3)
        output_data4.append(output4)
        clock_out += 1

    print(str(clock_in) + " in " + str(clock_out) + " out")

    format_data('FIFO Output Data: ', output_data1, ONE_TO_FOUR)
    ONE_TO_FOUR.write("\n")
    ONE_TO_FOUR.write("\n")

    format_data('LIFO Output Data: ', output_data2, ONE_TO_FOUR)
    ONE_TO_FOUR.write("\n")
    ONE_TO_FOUR.write("\n")

    format_data('Sorted Output Data: ', output_data3, ONE_TO_FOUR)
    ONE_TO_FOUR.write("\n")
    ONE_TO_FOUR.write("\n")

    format_data('Priority Output Data: ', output_data4, ONE_TO_FOUR)
    ONE_TO_FOUR.write("\n")
    ONE_TO_FOUR.write("\n" + str(clock_in) + " in " + str(clock_out) + " out")

    # Clears output data for next run
    output_data1.clear()
    output_data2.clear()
    output_data3.clear()
    output_data4.clear()

    clock_in = 0
    clock_out = 0
    count = 0

    # Four Registers Input, One register output
    for i in range(9):
        # Input registers
        input1 = data_fifo[i]
        input2 = data_lifo[i]
        input3 = data_sorted[i]
        input4 = data_priority[i]

        # FIFO, LIFO, sorted, and priority input from input registers
        FIFO.append(input1)
        LIFO.push(input2)
        sorted_queue.add_sorted(input3)
        heap.heappush(priority_queue, (priority_num[i], count, input4))
        count += 1
        clock_in += 1

    for i in range(9, 100):
        # FIFO output
        output1 = FIFO.popleft()
        output_data1.append(output1)
        clock_out += 1

        # LIFO output
        output1 = LIFO.pop()
        output_data2.append(output1)
        clock_out += 1

        # Sorted output
        output1 = sorted_queue.pop()
        output_data3.append(output1)
        clock_out += 1

        # Priority output
        output1 = heap.heappop(priority_queue)[2]
        output_data4.append(output1)
        clock_out += 1

        # Input registers
        input1 = data_fifo[i]
        input2 = data_lifo[i]
        input3 = data_sorted[i]
        input4 = data_priority[i]

        # FIFO, LIFO, sorted, and priority input from input registers
        FIFO.append(input1)
        LIFO.push(input2)
        sorted_queue.add_sorted(input3)
        heap.heappush(priority_queue, (priority_num[i], count, input4))
        count += 1
        clock_in += 1

    for i in range(9):
        # FIFO output
        output1 = FIFO.popleft()
        output_data1.append(output1)
        clock_out += 1
        # LIFO output
        output1 = LIFO.pop()
        output_data2.append(output1)
        clock_out += 1
        # Sorted output
        output1 = sorted_queue.pop()
        output_data3.append(output1)
        clock_out += 1
        # Priority output
        output1 = heap.heappop(priority_queue)[2]
        output_data4.append(output1)
        clock_out += 1

    print(str(clock_in) + " in " + str(clock_out) + " out")

    format_data('FIFO Output Data: ', output_data1, FOUR_TO_ONE)
    FOUR_TO_ONE.write("\n")
    FOUR_TO_ONE.write("\n")

    format_data('LIFO Output Data: ', output_data2, FOUR_TO_ONE)
    FOUR_TO_ONE.write("\n")
    FOUR_TO_ONE.write("\n")

    format_data('Sorted Output Data: ', output_data3, FOUR_TO_ONE)
    FOUR_TO_ONE.write("\n")
    FOUR_TO_ONE.write("\n")

    format_data('Priority Output Data: ', output_data4, FOUR_TO_ONE)
    FOUR_TO_ONE.write("\n")
    FOUR_TO_ONE.write("\n" + str(clock_in) + " in " + str(clock_out) + " out")


# Formats data to 10x10 and prints to output files
def format_data(name, list, output_file):
    output = name + "\n"
    count = 1
    for i in list:
        if count % 10 == 0:
            output = output + str(i) + " \n"
        else:
            output = output + str(i) + " "
        count += 1
    output_file.write(output)

# Function returns a list of random data from specified parameters
def get_random(start, limit):
    data = []
    for i in range(100):
        data.append(random.randint(start, limit))
    return data


if __name__ == "__main__":
    main()
    pass
