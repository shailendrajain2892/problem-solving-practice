import math


class MinHeap:
    def __init__(self) -> None:
        self.heap = []
    
    def parent(self, index) -> int:
        return (index-1)//2
    
    def left(self, index) -> int:
        return 2*index+1
    
    def right(self, index) -> int:
        return 2*index+2
    
    def insert(self, val) -> None:
        self.heap.append(val)
        self.heapify_up(len(self.heap)-1)
    
    def heapify_up(self, index):
        while index != 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)
    
    def remove_min(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        return root
    
    def heapify_down(self, index):
        smallest = index
        leftI = self.left(index)
        rightI = self.right(index)
        if leftI < len(self.heap) and  self.heap[leftI] < self.heap[smallest] :
            smallest = leftI
        elif rightI < len(self.heap) and self.heap[rightI] < self.heap[smallest]:
            smallest = rightI
        
        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.heapify_down(smallest)


    def get_min(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]
    
    def size(self):
        return len(self.heap)
    
    def isEmpty(self):
        return len(self.heap) == 0

def main():
    heap = MinHeap()
    heap.insert(3)
    heap.insert(1)
    heap.insert(6)
    heap.insert(5)
    heap.insert(2)
    heap.insert(4)

    print(heap.get_min())  # Output: 1
    print(heap.remove_min())  # Output: 1
    print(heap.get_min())  # Output: 2

main()