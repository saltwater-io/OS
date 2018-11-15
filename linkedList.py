class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next  # reference to next node in DLL
        self.prev = prev  # reference to previous node in DLL
        self.data = data


# LinkedList code taken from: https://www.geeksforgeeks.org/doubly-linked-list/


class LinkedList:

    # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None
        self.tail = None

    # Given a reference to the head of a list and an
    # integer, inserts a new node on the front of list
    def push(self, new_data):
        # 1. Allocates node
        # 2. Put the data in it
        new_node = Node(new_data)

        # 3. Make next of new node as head and
        # previous as None (already None)
        new_node.next = self.head

        # 4. change prev of head node to new_node
        if self.head is not None:
            self.head.prev = new_node

            # 5. move the head to point to the new node
        self.head = new_node

    def print_list(self, node):
        while (node is not None):
            print(node.data),
            last = node
            node = node.next

        # Given a reference to the head of DLL and integer,
        # appends a new node at the end

    def append(self, new_data):

        # 1. Allocates node
        # 2. Put in the data
        new_node = Node(new_data)

        # 3. This new node is going to be the last node,
        # so make next of it as None
        new_node.next = None

        # 4. If the Linked List is empty, then make the
        # new node as head
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

            # 5. Else traverse till the last node
        last = self.head
        while (last.next is not None):
            last = last.next

        # 6. Change the next of last node
        last.next = new_node

        # 7. Make last node as previous of new node
        new_node.prev = last
        return

    def insert_after(self, prev_node, new_node):

        # 1. check if the given prev_node is NULL
        if prev_node is None:
            print("This node doesn't exist in DLL")
            return

        # 2. allocate node  & 3. put in the data

        # 4. Make next of new node as next of prev_node
        new_node.next = prev_node.next

        # 5. Make the next of prev_node as new_node
        prev_node.next = new_node

        # 6. Make prev_node as previous of new_node
        new_node.prev = prev_node

        # 7. Change previous of new_node's next node */
        if new_node.next is not None:
            new_node.next.prev = new_node

    def add_sorted(self, s_data):
        new_node = Node(data=s_data)

        if not self.head:
            self.head = new_node
        elif self.head and not self.tail:
            if new_node.data > self.head.data:  # Data > head data
                self.tail = self.head
                self.head = new_node
                self.head.next = self.tail
                self.tail.prev = self.head
            else:
                self.head.next = new_node
                self.tail = new_node
                self.tail.prev = self.head
        else:
            last = self.head
            while last.data > new_node.data and last.next:
                last = last.next
            self.insert_after(last, new_node)


    def add_priority(self, data):
        new_node = Node(data=data)
        if not self.tail:
            self.tail = new_node
        elif self.tail and not self.head:
            if new_node.data >= self.tail.data:
                self.head = new_node
                self.head.next = self.tail
                self.tail.prev = self.head
            else:
                self.head = self.tail
                self.head.next = new_node
                self.tail = new_node
                self.tail.prev = self.head
        else:
            last = self.tail
            while last.data < new_node.data:
                last = last.prev
            self.insert_after(last.next, new_node=new_node)


    def pop(self):
        if not self.head:
            print("List empty")
            return False
        dead_boi = self.head
        if self.head.next:
            self.head = self.head.next
        self.head.prev = None
        return dead_boi.data

    def pop_tail(self):
        if not self.tail:
            print("Tail not found! ")
            return
        dead_boi = self.tail
        if self.tail.prev:
            self.tail = self.tail.prev
        else:
            self.tail = None
        return dead_boi.data
