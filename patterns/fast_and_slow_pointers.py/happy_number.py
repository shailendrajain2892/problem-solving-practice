class Solution:
    # def isHappy(self, n: int) -> bool:
        # resL = []
        # res = 0
        # while True:
        #     for i in str(n):
        #         res+=(int(i)*int(i))
        #     if res == 1:
        #         return True
        #     elif res in resL:
        #         return False
        #     resL.append(res)
        #     n = res
        #     res=0

    def isHappy(self, n: int) -> bool:
        #2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 > 42 -> 20
        slow = self.squared(n) # 4->16->37->58->89->145->42->20
        fast = self.squared(self.squared(n)) # 16->58->145->20->16->58->145->20

        while slow!=fast and fast!=1:
            slow = self.squared(slow)
            fast = self.squared(self.squared(fast))

        return fast==1

    def squared(self, n):
        result = 0
        while n>0:
            last = n%10
            result += last * last
            n = n//10
        return result
    
print(Solution().isHappy(2))