class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # two pointer -2
        i = 0
        n = len(nums) # count of elements
        active = len(nums) -1 # last index
        while i < n:
            if nums[i] == val:
                nums[i]= nums[active]
                n = n - 1
                active = active - 1
            else:
                i = i +1
        return n           
