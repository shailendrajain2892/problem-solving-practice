from queue import Queue

q = Queue()
n=[2,1,5,7,9]
for i in n:
    q.put(i)
print(q.get())

