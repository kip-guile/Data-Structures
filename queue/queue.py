"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.size += 1
#         self.storage.insert(0, value)

#     def dequeue(self):
#         if len(self.storage) == 0:
#             return
#         self.storage -= 1
#         return self.storage.pop()


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


class Queue:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def enqueue(self, value):
        new_node = Node(value)
        self.size += 1
        if not self.head:
            self.head = new_node
        else:
            old_head = self.head
            new_head = self.head
            new_head.set_next(old_head)

    def dequeue(self):
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
