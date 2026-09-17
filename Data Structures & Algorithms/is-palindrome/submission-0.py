class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = [c.lower() for c in s if c.isalnum()]
        reversedSentence = list(reversed(sentence))
        if sentence == reversedSentence:
            return True
        else:
            return False