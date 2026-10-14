class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        
        ans = nums[0]
        sumi = 0

        for i in nums:
            if sumi < 0:
                sumi = 0
            
            sumi += i
            ans = max(ans,sumi)
        return ans