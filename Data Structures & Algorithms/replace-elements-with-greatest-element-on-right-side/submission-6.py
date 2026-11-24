class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Brute Force
        ans = [0] * len(arr)
        for i in range(len(arr)):
            rightMax = -1
            for  j in range(i+1,len(arr)):
                rightMax = max(rightMax,arr[j])

            ans[i] = rightMax
        return ans