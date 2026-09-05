class Solution:
    def secondLargestElement(self, nums):

        first = nums[0]
        second = -1

        if len(nums) < 2:
            return second
        
        for i in nums:
            if i > first:
                second = first 
                first = i
            elif first > i and second < i:
                second = i        
        return second