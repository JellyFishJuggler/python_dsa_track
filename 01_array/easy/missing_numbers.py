class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        
        ans = 0

        for i in range(len(nums)+1):

            if i not in nums:
                ans = i
        
        return ans