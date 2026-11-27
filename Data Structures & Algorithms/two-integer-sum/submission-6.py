class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash map : one pass
        prevMap = {}
        for i,n in enumerate(nums):
            complement = target - n
            if complement in prevMap:
                return [prevMap[complement],i]
            prevMap[n] = i     