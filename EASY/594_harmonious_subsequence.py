class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        longest = 0
        for key in count:
            if key + 1 in count:
                longest = max(longest, count[key] + count[key + 1])

        return longest
