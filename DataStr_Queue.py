#######################
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.head = Node('head')
        self.tail = self.head
        self.size = 0

    def __str__(self) -> str:
        counter = []
        tmp = self.head.next
        while tmp:
            counter.append(str(tmp.val))
            tmp = tmp.next
        return "->".join(counter)

    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def push(self, element):
        node = Node(element)
        if self.head.next is None:
            self.head.next = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise "QUEUE IS EMPTY"
        element = self.head.next.val
        self.head.next = self.head.next.next
        self.size -= 1
        return element

queue = Queue()

queue.push(7)
queue.push(5)
print(queue, queue.get_size())
queue.pop()
print(queue, queue.get_size())