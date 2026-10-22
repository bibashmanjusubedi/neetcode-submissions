class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # initialize rightMax = -1, iterate from Right 
        rightMax = -1
        n = len(arr)
        for i in range(n-1,-1,-1):
            temp = arr[i]
            arr[i] = rightMax
            rightMax = max(rightMax,temp)
        return arr