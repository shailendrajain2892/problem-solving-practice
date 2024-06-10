from queue import Queue

def first_n_numbers(total_num,s):
    q = Queue()
    res = []
    for n in s:
        q.put(n)
    count=2
    while count<total_num:
        num = q.get()
        res.append(num)
        for n1 in s:
            num1=str(num)+str(n1)
            q.put(int(num1))
            count+=1

    while(len(res)<total_num and q.qsize()!=0):
        res.append(q.get())
    
    return res


print(first_n_numbers(10,[1,2]))