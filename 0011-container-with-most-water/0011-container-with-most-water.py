class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width  =right - left 
            current = min(height[left],height[right])* width
            area = max(area,current)

            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        return area 