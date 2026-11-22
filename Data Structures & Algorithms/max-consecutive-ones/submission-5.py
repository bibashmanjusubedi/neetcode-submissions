class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # iteration -2,after brute force
        consecutive = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                consecutive = max(count,consecutive)
                count = 0
            elif nums[i]==1:
                count = count + 1
                consecutive = max(count,consecutive)

        return consecutive