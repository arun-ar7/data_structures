class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Llist:
    def __init__(self, node=None):
        self.head = node
        self.last = node