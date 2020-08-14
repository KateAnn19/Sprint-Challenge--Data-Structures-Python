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

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        prev = None
        current = self.head
        while current is not None:
        # grab the tail and put into a variable
           temp = current.next_node
           current.next_node = prev
           prev = current
           current = temp
        self.head = prev

        
        # take the prev element and point it to none
        # make prev element the new tail
        # grab the head
        # point the head to the old tail
        # make old tail the new head
        # point old tail to the old head
        # continue until the old head is now the old tail
        pass
