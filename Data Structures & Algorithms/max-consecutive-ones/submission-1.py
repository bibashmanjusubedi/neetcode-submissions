class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        reset = count = 0
        for i in nums:
            if i == 1:
                count +=1
            else:
                count = 0
            reset = max(reset,count)
        return reset