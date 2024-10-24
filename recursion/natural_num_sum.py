def natural_num_sum(n):
    if n==0:
        return 0
    return n+natural_num_sum(n-1)

print(natural_num_sum(10))