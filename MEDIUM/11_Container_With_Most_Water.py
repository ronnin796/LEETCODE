height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 9, 6, 7]
max_area = 1
height2 = [1, 1]


class Solution:
    def __init__(self):
        pass

    def maxArea(self, height: List[int]) -> int:
        max_area = 1
        for index1, value1 in enumerate(height):
            for index2, value2 in enumerate(height):
                new_area = self.calculate_area(value1, value2, index2 - index1)
                if new_area > max_area:
                    max_area = new_area
        print(max_area)

    def calculate_area(self, number1, number2, distance):
        lesser_num = min(number1, number2)
        return lesser_num * distance


solution = Solution()
solution.maxArea(height)
