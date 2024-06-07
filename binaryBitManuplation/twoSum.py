import sys


def twoSum(a, b):
    while b != 0 : 
        #calculate carry by doing and operation betwwen two numbers
        carry = a & b
        #add two numbers using xor
        a = a ^ b 
        #update b by movin carry to left shift by 1 
        b = carry << 1

    return a 

a = int(sys.argv[1])
b = int(sys.argv[2])
print(twoSum(a,b))