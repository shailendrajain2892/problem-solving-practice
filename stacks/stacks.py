class Stacks:
    def __init__(self) -> None:
        self.stack=[]
        self.top=-1
        self.size=0

    def push(self, n):
        print(f"inserting {n}")
        self.stack.append(n)
        self.top+=1

    def Spop(self):
        value =  self.stack[self.top]
        self.stack.remove(self.stack[self.top])
        self.top-=1
        return value

    def peek(self):
        return self.stack[self.top]

    def isEmpty(self):
        return True if self.top==-1 else False

    def Ssize(self):
        return self.top+1


st = Stacks()
numbers = [3,9,1,12,8,2]
for n in numbers:
    st.push(n)
for _ in numbers:
    print(st.Spop())
    print(st.Ssize())
    print(st.isEmpty())
print(st.isEmpty())