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


    def delete(self, element):
        try:
            index = self.heap.index(element)
            
            # swap with last element
            self.heap[index] = self.heap[-1]
            # remove it by popping 
            self.heap.pop()
            if index < self.size():
                self.heapify_up(index)
                self.heapify_down(index)
        except:
            raise ValueError("Key not found in Heap")
        


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
    nums = [20, 8, 7, 15, 19, 4, 17]
    for n in nums:
        heap.insert(n)
    
    print(heap.heap)

    print(heap.get_min())  # Output: 1
    # print(heap.remove_min())  # Output: 1
    # print(heap.get_min())  # Output: 2
    heap.delete(4)
    print(f"Heap after deletion : {heap.heap}")

main()