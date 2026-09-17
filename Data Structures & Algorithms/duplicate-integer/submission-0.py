class Solution:
    def hasDuplicate(self, nums: List[int]) ->bool:
        non_repeated = []
        for num in nums:
            if num in non_repeated:
                return True
            non_repeated.append(num)
        return False
        