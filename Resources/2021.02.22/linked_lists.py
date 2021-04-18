from abc import ABC, abstractmethod


class Node:

    def __init__(self, value):
        super().__init__()
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return f'Node({self.value})'


class LinkedList(ABC):

    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def remove(self, item):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    
class SinglyLinkedList(LinkedList):

    def __init__(self):
        super().__init__()
        self.head = None

    def add(self, item):
        node = Node(item)

        if not self.head:
            self.head = node
        else:
            cursor = self.head
            while cursor.next:
                cursor = cursor.next

            cursor.next = node

    def remove(self, item):
        if not self.head:
            raise ValueError("Can't remove item from empty linked list")

        # process the head
        cursor = prev = self.head
        while True:
            if self.head.value != item:
                break

            self.head = self.head.next

        # process inner items
        while cursor:
            if cursor.value == item:
                prev.next = cursor.next
            else:
                prev = cursor

            cursor = cursor.next

    def __iter__(self):
        if not self.head:
            raise StopIteration()

        current = self.head
        while current:
            yield current
            current = current.next


class TailedSinglyLinkedList(LinkedList):

    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None

    def add(self, item):
        node = Node(item)

        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = self.tail = node

    def remove(self, item):
        if not self.head:
            raise ValueError("Can't remove item from empty linked list")

        cursor = prev = self.head
        while True:
            if self.head.value != item:
                break

            self.head = self.head.next

        while cursor:
            if cursor.value == item:
                prev.next = cursor.next
            else:
                prev = cursor

            cursor = cursor.next

    def __iter__(self):
        if not self.head:
            raise StopIteration()

        current = self.head
        while current:
            yield current
            current = current.next


if __name__ == '__main__':
    llist = SinglyLinkedList()
    llist.add(14)
    llist.add(14)
    llist.add(211)
    llist.add(323)
    llist.add(211)
    llist.add(14)
    llist.add(100)
    llist.add(25)
    print('head:', llist.head)

    for item in llist:
        print(item)

    llist.remove(14)
    print('Iterating after removal')
    for item in llist:
        print(item)
