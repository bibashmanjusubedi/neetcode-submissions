class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashSet
        seen = []
        for num in nums:
            if num in seen:
                return True
            else:
                seen.append(num)
        return False 
