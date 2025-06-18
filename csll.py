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

    def delete_by_value(self, value):
        if not self.head:
            return None

        # making the dummy node and updating the loop accordingly.
        dummy = Node(-99)
        dummy.next = self.head
        self.head = dummy
        self.tail.next = self.head

        # setting up the logic.
        pre = dummy
        curr = pre.next

        while curr:
            if curr.value == value:

                if curr is  self.tail:
                    self.tail = pre
                    pre.next = self.head
                else:
                    next = curr.next
                    pre.next = next

                curr.next = None    
                self.length -= 1
                self.head = self.head.next
                break

            else:
                pre = curr
                curr = curr.next

            if curr == self.head:
                return "Node with mentioned value didn't found."

        return self.head

    def count_nodes(self):
        if not self.head:
            return 0

        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
            if curr == self.head:
                break
        return count
    
    def split_list(self):
        if not self.head:
            return None,None

        if self.head.next == self.head:
            return "List only has one node."
        

        slow = fast = self.head
        
        while fast :
            if fast.next.next == self.head:
                break
            else:
                slow = slow.next
                fast = fast.next.next

            if fast.next == self.head:
                break
        
        second_head = slow.next
        
        slow.next = self.head

        second_list = CSLinkedList()
        while second_head:
            second_list.append(second_head.value)
            
            if second_head == self.tail:
                break

            second_head = second_head.next
        


        first_list = CSLinkedList()
        curr_one = self.head
        while curr_one:
            first_list.append(curr_one.value)
            if curr_one.next == self.head:
                break
        
            curr_one = curr_one.next

        return first_list, second_list