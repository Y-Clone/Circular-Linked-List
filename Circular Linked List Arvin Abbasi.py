class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def length(self):
        if self.is_empty():
            return 0
        length = 1
        current = self.head.next
        while current != self.head:
            length += 1
            current = current.next
        return length

    def insert_first(self, key, data):
        new_node = Node(key, data)
        if self.is_empty():
            self.head = new_node
            self.head.next = self.head
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node

    def delete_first(self):
        if self.is_empty():
            return None
        temp = self.head
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            self.head = self.head.next
            current.next = self.head
        return temp

    def print_list(self):
        if self.is_empty():
            print("\n[ ]")
            return
        current = self.head
        print("\n[", end=" ")
        while True:
            print(f"({current.key},{current.data})", end=" ")
            current = current.next
            if current == self.head:
                break
        print("]")
