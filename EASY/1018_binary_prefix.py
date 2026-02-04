from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        binary_prefix = 0
        result = []
        for num in nums:
            binary_prefix = ((binary_prefix << 1) + num) % 5
            result.append(binary_prefix == 0)

        return result
