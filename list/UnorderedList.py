import Node

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    # Add new elements in the head of the list
    def add(self, item):
        temp = Node(item)           # Create a node that holds the item
        temp.setNext(self.head)     # new node will now point to previous head
        self.head = temp            # Head will be the new node

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count


