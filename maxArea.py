class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the area between two lines
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            max_area = max(max_area, area)

            # Move the pointer that has the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# Example usage
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
obj = Solution()
print(obj.maxArea(height))  # Output: 49
