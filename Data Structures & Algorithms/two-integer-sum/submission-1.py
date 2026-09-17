class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementSet = dict()
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in complementSet:
                return [complementSet[complement], i]
            complementSet[nums[i]] = i
        