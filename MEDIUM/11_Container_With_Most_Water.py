height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
max_area = 1
height2 = [1, 1]


class Solution:
    def __init__(self):
        pass

    def maxArea(self, height: List[int]) -> int:
        max_area = 1
        for i in range(len(height) // 2):
            for j in range(i, len(height)):
                new_area = min(height[i], height[j]) * (j - i)
                if new_area > max_area:
                    max_area = new_area
        return max_area


solution = Solution()
print(solution.maxArea(height))
