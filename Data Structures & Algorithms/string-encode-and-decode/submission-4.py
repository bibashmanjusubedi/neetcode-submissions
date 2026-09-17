class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for i in strs:
            encoded.append(f"{len(i)}#{i}")
        return "".join(encoded)


    
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        decoded = []
        i = 0
        while i < len(s):
            # Find the delimiter position
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            # Extract the length
            length = int(s[i:j])
            # Extract the string
            decoded.append(s[j+1 : j+1+length])
            # Move to next segment
            i = j + 1 + length
        return decoded
        