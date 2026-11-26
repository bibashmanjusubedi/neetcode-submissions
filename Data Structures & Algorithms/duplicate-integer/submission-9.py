class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hash set length
        return len(set(nums)) < len(nums)
