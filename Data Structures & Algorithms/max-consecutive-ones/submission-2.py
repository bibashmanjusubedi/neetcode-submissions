class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # brute force
        consecutive = 0
        for i in range(len(nums)):
            count = 0
            for j in range(i,len(nums)):
                if nums[j] == 0: break
                elif nums[j]==1:
                    count +=1
            consecutive = max(consecutive,count)

        return consecutive
            