class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0) # build a frequency array that counts how many times each number appears
        freq = [[] for i in range(len(nums)+1)]  # this list for creating at each index we store all numbers that appear exactly that many times

        for num, cnt in count.items():
            freq[cnt].append(num)

        result = []

        # reverse iteration till k
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    break
            if len(result) == k:
                break

        return result
                    



