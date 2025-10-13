from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stores indices
        max_area = 0
        
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        
        while stack:
            h = heights[stack.pop()]
            w = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, h * w)
        
        return max_area

# Example usage
if __name__ == "__main__":
    sol = Solution()
    heights = [2,1,5,6,2,3]
    print("Largest rectangle area:", sol.largestRectangleArea(heights))
    # Output: 10

    heights2 = [2,4]
    print("Largest rectangle area:", sol.largestRectangleArea(heights2))
    # Output: 4
