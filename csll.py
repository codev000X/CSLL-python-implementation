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

    def __str__(self):

        if not self.head:
            return "The list is empty."
        
        curr = self.head
        result = ''

        while curr:
            result += str(curr.value)
            curr = curr.next

            if curr == self.head:
                break

            result += " -> "
        return result

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

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.length += 1
