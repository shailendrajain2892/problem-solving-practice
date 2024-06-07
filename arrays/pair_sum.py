def get_pair_sum(numbers, target):
    result = {}
    for idx, num in enumerate(numbers):
        diff = target-num
        if diff not in result:
            result[num] = idx
        else:
            return num, diff

numbers = [2, 7, 8, 4, 3]
target = 12
print(get_pair_sum(numbers, target))
