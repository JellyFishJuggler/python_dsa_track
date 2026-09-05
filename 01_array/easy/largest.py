class Solution:
    def largestElement(self, nums):
        ans = nums[0]
        for i in nums:
            if i > ans:
                ans = i
        return ans