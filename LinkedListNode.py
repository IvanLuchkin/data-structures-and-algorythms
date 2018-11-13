class LinkedListNode:
    def __init__(self, item):
        self.item = item
        self.next = None


node1 = LinkedListNode(1)
node2 = LinkedListNode(2)
node2.next = node1

node3 = LinkedListNode(3)
node3.next = node1


class LinkedList:
    def __init__(self):
        self.head = None

    def add_head(self, item):
        old_head = self.head
        self.head = LinkedListNode(item)
        self.next = self.head

    def remove_head(self):
        if self.head is None:
            raise IndexError("Linked list is empty")

        self.head = self.head.next

