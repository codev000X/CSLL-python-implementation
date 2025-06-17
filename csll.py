class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class CSLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
                                       
        if not self.head:                       # If the CSLL is empty.
            self.head = self.tail =new_node
            new_node.next = new_node
        else:                                   # If the CSLL has at least one node.
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node

        self.length += 1

