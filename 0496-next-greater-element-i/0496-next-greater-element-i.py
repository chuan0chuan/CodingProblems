class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        stack =[]
        for i in range(len(nums2)):
            while len(stack) > 0 and nums2[i] > nums2[stack[-1]]:
                if nums2[stack[-1]] in nums1:
                    index = nums1.index(nums2[stack[-1]])
                    result[index] = nums2[i]
                    #solved under while conditoion for stack[-1]
                stack.pop()
            #not solved for new i, so append to stack
            stack.append(i)
        return result