

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums[0]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        psum=0
        #prefix_sum array
        prefix_sum=[]
        #create prefix sum
        for n in self.nums:
            psum+=n
            prefix_sum.append(psum)
        
        return prefix_sum[right] - prefix_sum[left-1] if left>0 else prefix_sum[right]

        


# Your NumArray object will be instantiated and called as such:
nums, ranges = ([[-2, 0, 3, -5, 2, -1]], ([0, 2], [2, 5], [0, 5]))
obj = NumArray(nums)
for rng in ranges:
    param_1 = obj.sumRange(rng[0], rng[1])
    print(param_1)