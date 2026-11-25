class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # iteration - 1
        n = len(nums)
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums