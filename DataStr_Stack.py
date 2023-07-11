class Node:
    """linked list"""
    def __init__(self, value):
        self.val = value
        self.next = None
    
class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        """string representation of the stack"""
        current = self.head.next
        out = [] * self.size
        while current:
            out.append(str(current.val))
            current = current.next
        return "->".join(out)
    
    def get_size(self):
        """return the current size of stack"""
        return self.size
    
    def is_empty(self):
        """check is the stack empty"""
        return self.size == 0

    def push(self, element):
        """add a new element to the top of the stack"""
        node = Node(element)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        """delete an element from the top of stack and return it"""
        if self.is_empty():
            raise "STACK IS EMPTY"
        element = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return element.val


stack = Stack()
stack.push(7)
stack.push(5)
print(stack, stack.get_size())
stack.pop()
print(stack, stack.get_size())