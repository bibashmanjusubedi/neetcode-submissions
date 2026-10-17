class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for i in strs:
            encoded.append(f"#{i}#")
        return "".join(encoded)


    def decode(self, s: str) -> List[str]:
        decoded = s.split("#")
        decodedNew = []
        for i in decoded:
            if i !="#" and i!="":
                decodedNew.append(i)
        return decodedNew