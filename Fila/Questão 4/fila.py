class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def queue(self, elem):
        node = Node(elem)
        if self.tail is None:
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        if self.head is None:
            self.head = node

        self._size = self._size + 1

    def dequeue(self):
        if self._size > 0:
            elem = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size = self._size - 1
            return elem
        raise IndexError("Fila vazia")



    def __len__(self):
        return self._size


