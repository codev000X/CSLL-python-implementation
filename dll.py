class Node:
    def __init__(self , value ):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return self.value
    

class DLL :
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self , value):
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def __str__(self):
        temp = self.head
        result = ""

        while temp is not None:
            result += str(temp.value)
            
            if temp.next is not None:
                result += " <-> "
            temp = temp.next

        return result

    def prepend(self ,value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    def traverse(self):
        if self.head is None:
            print("List is empty.")
            return
    
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next

    def reverse(self):
        if self.tail is None:
            print("List is empty.")
            return

        curr = self.tail
        while curr:
            print(curr.value)
            curr = curr.prev

    def search(self,value):
        if self.head is None :
            return False
        
        curr = self.head
        index = 0
        while curr:
            if curr.value == value:
                return index

            curr = curr.next
            index+=1
        return False