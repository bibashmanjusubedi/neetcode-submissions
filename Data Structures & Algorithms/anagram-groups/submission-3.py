class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorting
        res = {}
        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS not in res:
                res[sortedS] = []
            res[sortedS].append(s)
        return list(res.values())
    