def countPairs2(nums: list[int], target: int) -> int:
    # Tim Sort and Two Pointers
    nums.sort()
    left, right = 0, len(nums) - 1
    count = 0

    while left < right:
        if nums[left] + nums[right] < target:
            count += (right - left)
            left += 1
        else:
            right -= 1
    return count

nums = [-6, 2, 5, -2, -7, -1, 3]
print(countPairs2(nums,-2))
