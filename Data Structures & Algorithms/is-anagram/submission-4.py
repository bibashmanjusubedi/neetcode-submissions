class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       # brute force
        if sorted(s) == sorted(t):
            return True
        else:
            return False

            
            
            