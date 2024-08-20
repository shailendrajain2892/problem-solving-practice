class maxHeap:
    def __init__(self) -> None:
        self.heap = []

    def left(self, index) -> int:
        return 2 * index + 1
    
    def right(self, index) -> int:
        return 2 * index + 2
    
    def parent(self, index) -> int:
        return ( index - 1 ) // 2
    
    def insert(self, element) -> None: # TC: O(logn)
        self.heap.append(element)
        self.heapify_up(len(self.heap)-1)
    
    def heapify_up(self, index) -> None:
        while index!=0 and self.heap[self.parent(index)] < self.heap[index]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)
    
    def remove_max(self): # TC : O(logn)
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root
    
    def heapify_down(self, index):
        greatest = index
        left = self.left(index)
        right = self.right(index)

        if left < len(self.heap) and self.heap[left] > self.heap[greatest]:
            greatest = left
        elif right < len(self.heap) and self.heap[right] > self.heap[greatest]:
            greatest = right

        if greatest != index:
            self.heap[greatest], self.heap[index] = self.heap[index], self.heap[greatest]
            self.heapify_down(greatest)

    def getMax(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]
    
    def size(self):
        return len(self.heap)
    
    def isEmpty(self):
        return len(self.heap) == 0

def main():
    heap = maxHeap()
    heap.insert(40)
    heap.insert(20)
    heap.insert(10)
    heap.insert(5)
    heap.insert(6)
    heap.insert(7)
    heap.insert(8)

    heap.insert(44)
    print(heap.heap)

    print(heap.getMax())
    print(heap.remove_max())
    print(heap.heap)
    print(heap.getMax())

    print(heap.size())
    print(heap.isEmpty())


main()