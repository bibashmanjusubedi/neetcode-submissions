class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # simple add operation on Python List with O(n) time complexity, and O(n) space complexity
        ans = nums + nums
        return ans