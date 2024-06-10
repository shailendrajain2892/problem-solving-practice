from queue import Queue

class Stack:
    def __init__(self) -> None:
        self.q1 = Queue()
        self.q2 = Queue()

    def insert(self, number):
        self.q2.put(number)
        while not self.q1.empty():
            q1_element = self.q1.get()
            self.q2.put(q1_element)
        
        self.q1, self.q2 = self.q2, self.q1
        
    
    def pop(self):
        return self.q1.get()
    
    def top(self):
        return self.q1.queue[0]
    
    def empty(self):
        return self.q1.empty()
    

    


    
nums = [2,3,1,5,7]
st = Stack()
for n in nums:
    st.insert(n)
print(st.pop())
        