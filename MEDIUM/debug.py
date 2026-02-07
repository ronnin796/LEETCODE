height = [8, 7, 2, 1]


class Solution:
    def __init__(self):
        pass

    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            new_area = min(height[right], height[left]) * (right - left)
            print(height[right], "*", height[left], "=", new_area)
            if new_area > max_area:
                max_area = new_area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


s = Solution()
s.maxArea(height=height)
