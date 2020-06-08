"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.insert(len(self.storage) + 1, value)

    def pop(self):
        if len(self.storage) == 0:
            return
        self.size -= 1
        return self.storage.pop()


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class Stack_LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, value):
        new_node = Node(value)
        self.size += 1
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current.get_next()
            # by the end of this loop, we are at the end of the linked list
            current.set_next(new_node)

    def pop(self):
        if not self.head:
            return
        else:
            self.size -= 1
            current = self.head
            while current.get_next() is not None:
                prev = current
                current.get_next()
            prev.set_next(None)
            return prev
