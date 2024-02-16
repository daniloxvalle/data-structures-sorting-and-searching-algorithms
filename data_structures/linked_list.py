class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0  # _size is a private variable

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    # Show the data in the list
    def show(self):
        if self.is_empty():
            print("Linked list is empty")
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    # Return the data at the beginning of the list
    def peek(self):
        if self.is_empty():
            raise ValueError("Linked list is empty")
        return self.head.data

    # Add the data to the end of the list
    def append(self, data):
        new_node = Node(data)
        # First insertion
        if not self.head:
            self.head = new_node
        else:
            pointer = self.head
            # Go to the last node
            while pointer.next:
                pointer = pointer.next
            # Insert the new node
            pointer.next = new_node
        self._size += 1

    # Return the data at the index
    def get(self, index):
        if index > self._size - 1:
            raise ValueError("Index out of range")
        pointer = self.head
        # Go to the index node
        for _ in range(index):
            pointer = pointer.next
        return pointer.data

    def __getitem__(self, index):
        return self.get(index)

    # Set the data at the index
    def set(self, index, data):
        if index > self._size - 1:
            raise ValueError("Index out of range")
        pointer = self.head
        # Go to the index node
        for _ in range(index):
            pointer = pointer.next
        pointer.data = data

    def __setitem__(self, index, data):
        self.set(index, data)

    # Return the index of the first occurrence of the data
    def index(self, data):
        pointer = self.head
        index = 0
        while pointer:
            if pointer.data == data:
                return index
            pointer = pointer.next
            index += 1
        raise ValueError(f"{data} not found")

    # Insert the data at the index
    def insert(self, index, data):
        if index > self._size:
            raise ValueError("Index out of range")
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            pointer = self.head
            # Go to the index node
            for _ in range(index - 1):
                pointer = pointer.next
            # Insert the new node
            new_node.next = pointer.next
            pointer.next = new_node
        self._size += 1

    # Remove the first occurrence of the data
    def remove(self, data):
        if self.is_empty():
            raise ValueError("Linked list is empty")

        if self.head.data == data:
            self.head = self.head.next
            self._size -= 1
            return True

        pointer = self.head
        while pointer.next:
            if pointer.next.data == data:
                pointer.next = pointer.next.next
                self._size -= 1
                return True
            pointer = pointer.next
        return False


llist = LinkedList()
llist.append(4)
llist.append(8)
llist.append(15)
llist.append(21)

llist.show()
print("length:", len(llist))
print("get: ", llist[2])
llist[1] = 10
print("index: ", llist.index(10))
llist.show()
llist.remove(10)
llist.show()
