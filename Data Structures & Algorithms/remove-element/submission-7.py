class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # two pointer -2
        i = 0
        n = len(nums)
        active = len(nums) -1
        while i < n:
            if nums[i] == val:
                nums[i]= nums[active]
                n = n - 1
                active = active - 1
            else:
                i = i +1
        return n           
