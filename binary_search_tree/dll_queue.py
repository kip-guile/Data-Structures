from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        # counter to keep track of the number of elements in our queue
        self.size = 0
        # we'll use our LinkedList implementation to build the queue
        self.storage = DoublyLinkedList()

    def enqueue(self, item):
        self.size += 1
        self.storage.add_to_tail(item)

    def dequeue(self):
        if self.size == 0:
            return
        else:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size
