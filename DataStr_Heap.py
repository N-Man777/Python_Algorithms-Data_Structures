class Heap:
    def __init__(self) -> None:
        self.size = 0
        self.heap = []
    
    def insert(self, element):
        self.heap.append(element)
        self.size += 1
        tmp = self.size - 1
        while tmp > 0:
            par_idx = abs(tmp - 1) // 2
            if self.heap[tmp] < self.heap[par_idx]:
                self.heap[tmp], self.heap[par_idx] = self.heap[par_idx], self.heap[tmp]
                tmp = par_idx
            else:
                return
    
    def get_min(self):
        if self.size == 0:
            raise "HEAP IS EMPTY"
        else:
            mn = self.heap[0]
            self.size -= 1
            self.heap[0] = self.heap.pop()
            tmp = 0
            while True:
                left_child_idx = 2*tmp + 1
                right_child_idx = 2*tmp + 2
                idx = tmp
                if left_child_idx > self.size:
                    return mn
                idx = left_child_idx if self.heap[left_child_idx] < self.heap[tmp] else idx
                if right_child_idx < self.size:
                    idx = right_child_idx if self.heap[right_child_idx] < self.heap[idx] else idx
                if idx == tmp:
                    return mn
                else:
                    self.heap[tmp], self.heap[idx] = self.heap[idx], self.heap[tmp]
                    tmp = idx
    
    def get_heap(self):
        return self.heap

