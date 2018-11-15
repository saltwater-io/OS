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


def main():
    ONE_REGISTER_OUTPUT = open("ONE_REG.txt", 'w')
    FOUR_REGISTER_OUTPUT = open("FOUR_REG.txt", 'w')
    INTPUT_DATA = open("INPUT.txt", 'w')
    ONE_TO_FOUR = open("ONE_TO_FOUR_REG.txt", 'w')
    FOUR_TO_ONE = open("FOUR_TO_ONE_REG.txt", 'w')


    output_data1 = []
    output_data2 = []
    output_data3 = []
    output_data4 = []

    priority_queue = []
    sorted_queue = linkedList.LinkedList()
    FIFO = deque()
    LIFO = Stack()


    clock_in = 0
    clock_out = 0

    data_priority = getRandom(0, 99)
    data_fifo = getRandom(0, 99)
    data_lifo = getRandom(0, 99)
    data_sorted = getRandom(0, 99)
    priority_num = getRandom(1, 3)

    # format_data("First input data: ", data_priority, ONE_REGISTER_OUTPUT)
    # ONE_REGISTER_OUTPUT.write("\n")

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

        input1 = data_fifo[i]
        FIFO.append(input1)
        clock_in += 1

        input1 = data_lifo[i]
        LIFO.push(input1)
        clock_in += 1

        input1 = data_sorted[i]
        sorted_queue.add_sorted(input1)
        clock_in += 1

        input1 = data_priority[i]
        heap.heappush(priority_queue, (priority_num[i], count, input1))
        count += 1
        clock_in += 1

    for i in range(9, 100):
        output1 = FIFO.popleft()
        output_data1.append(output1)
        clock_out += 1

        output1 = LIFO.pop()
        output_data2.append(output1)
        clock_out += 1

        output1 = sorted_queue.pop()
        output_data3.append(output1)
        clock_out += 1

        output1 = heap.heappop(priority_queue)[2]
        output_data4.append(output1)
        clock_out += 1

        input1 = data_fifo[i]
        FIFO.append(input1)
        clock_in += 1

        input1 = data_lifo[i]
        LIFO.push(input1)
        clock_in += 1

        input1 = data_sorted[i]
        sorted_queue.add_sorted(input1)
        clock_in += 1

        input1 = data_priority[i]
        heap.heappush(priority_queue, (priority_num[i], count, input1))
        count += 1
        clock_in += 1


    print()

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

        output1 = heap.heappop(priority_queue)[2]
        output_data4.append(output1)
        clock_out += 1

 # TODO: START FIX HERE MAKE SURE 1x4x1 above works and prints

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

        FIFO.append(input1)
        LIFO.push(input2)
        sorted_queue.add_sorted(input3)
        heap.heappush(priority_queue, (priority_num[i], count, input4))
        count += 1
        clock_in += 1

    for i in range(9, 100):
        input1 = data_fifo[i]
        input2 = data_lifo[i]
        input3 = data_sorted[i]
        input4 = data_priority[i]

        output1 = FIFO.popleft()
        output2 = LIFO.pop()
        output3 = sorted_queue.pop()
        output4 = heap.heappop(priority_queue)[2]
        clock_out += 1

        output_data1.append(output1)
        output_data2.append(output2)
        output_data3.append(output3)
        output_data4.append(output4)

        FIFO.append(input1)
        LIFO.push(input2)
        sorted_queue.add_sorted(input3)
        heap.heappush(priority_queue, (priority_num[i], count, input4))
        count += 1
        clock_in += 1

    for j in range(9):
        output1 = FIFO.popleft()
        output2 = LIFO.pop()
        output3 = sorted_queue.pop()
        output4 = heap.heappop(priority_queue)[2]

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

    output_data1.clear()
    output_data2.clear()
    output_data3.clear()
    output_data4.clear()

    clock_in = 0
    clock_out = 0
    count = 0

#    1 Reg input, 4 reg output
    for i in range(9):

        input1 = data_fifo[i]
        FIFO.append(input1)
        clock_in += 1

        input1 = data_lifo[i]
        LIFO.push(input1)
        clock_in += 1

        input1 = data_sorted[i]
        sorted_queue.add_sorted(input1)
        clock_in += 1

        input1 = data_priority[i]
        heap.heappush(priority_queue, (priority_num[i], count, input1))
        count += 1
        clock_in += 1

    for i in range(9, 100):

        output1 = FIFO.popleft()
        output2 = LIFO.pop()
        output3 = sorted_queue.pop()
        output4 = heap.heappop(priority_queue)[2]

        output_data1.append(output1)
        output_data2.append(output2)
        output_data3.append(output3)
        output_data4.append(output4)
        clock_out += 1

        input1 = data_fifo[i]
        FIFO.append(input1)
        clock_in += 1

        input1 = data_lifo[i]
        LIFO.push(input1)
        clock_in += 1

        input1 = data_sorted[i]
        sorted_queue.add_sorted(input1)
        clock_in += 1

        input1 = data_priority[i]
        heap.heappush(priority_queue, (priority_num[i], count, input1))
        count += 1
        clock_in += 1

    for i in range(9):
        output1 = FIFO.popleft()
        output2 = LIFO.pop()
        output3 = sorted_queue.pop()
        output4 = heap.heappop(priority_queue)[2]

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

    output_data1.clear()
    output_data2.clear()
    output_data3.clear()
    output_data4.clear()

    clock_in = 0
    clock_out = 0
    count = 0

    # Four register Input to One register output
    for i in range(9):
        input1 = data_fifo[i]
        input2 = data_lifo[i]
        input3 = data_sorted[i]
        input4 = data_priority[i]

        FIFO.append(input1)
        LIFO.push(input2)
        sorted_queue.add_sorted(input3)
        heap.heappush(priority_queue, (priority_num[i], count, input4))
        count += 1
        clock_in += 1

    for i in range(9, 100):
        output1 = FIFO.popleft()
        output_data1.append(output1)
        clock_out += 1

        output1 = LIFO.pop()
        output_data2.append(output1)
        clock_out += 1

        output1 = sorted_queue.pop()
        output_data3.append(output1)
        clock_out += 1

        output1 = heap.heappop(priority_queue)[2]
        output_data4.append(output1)
        clock_out += 1

        input1 = data_fifo[i]
        input2 = data_lifo[i]
        input3 = data_sorted[i]
        input4 = data_priority[i]

        FIFO.append(input1)
        LIFO.push(input2)
        sorted_queue.add_sorted(input3)
        heap.heappush(priority_queue, (priority_num[i], count, input4))
        count += 1
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


def getRandom(start, limit):
    data = []
    for i in range(100):
        data.append(random.randint(start, limit))
    return data


if __name__ == "__main__":
    main()
    pass
