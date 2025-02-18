class Solution:
    def trap(self, height: List[int]) -> int:
        leftheight = [0]* len(height)
        rightheight = [0]*len(height)
        result = 0

        leftheight[0] = height[0]
        for i in range(1, len(height)):
            leftheight[i] = max(leftheight[i-1],height[i])

        rightheight[-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            rightheight[i] = max(rightheight[i+1],height[i])
        
        for i in range(len(height)):
            result += min(leftheight[i] ,rightheight[i]) - height[i]
        return result