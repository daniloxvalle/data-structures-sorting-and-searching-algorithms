class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.head.data

    def push(self, data):
        # Create a new node
        new_node = Node(data)
        # New node points to the current head
        new_node.next = self.head
        # Stack head points to the new node
        self.head = new_node
        # Increase the size of the stack
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        # Get the data of the current head
        data = self.head.data
        # Move the head to the next node
        self.head = self.head.next
        # Decrease the size of the stack
        self.size -= 1
        return data

    def show(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


stack: Stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(9)

stack.show()
print(stack.peek())
print(stack.is_empty())
print(len(stack))
print(stack.pop())
print(stack.pop())
print(stack.pop())
stack.show()
