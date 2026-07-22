# Implement a code were node is calculated in the cirular Linked List. Below is an implementation of a Circular Linked List in Python, where each node contains a value and a reference to the next node. The last node points back to the first node, creating a circular structure.
# python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            return "List is empty"
        current = self.head
        result = []
        while True:
            result.append(current.value)
            current = current.next
            if current == self.head:
                break
        return result

    def calculate_nodes(self):
        if not self.head:
            return 0
        count = 1
        current = self.head.next
        while current != self.head:
            count += 1
            current = current.next
        return count
