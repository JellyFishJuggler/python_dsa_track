class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        
        left = 0
        sumi = 0
        ans = float('inf')

        for right in range(len(nums)):
            sumi += nums[right]

            while sumi >= target:
                ans = min(ans, right-left+1)
                sumi -= nums[left]
                left += 1
        if ans == float('inf'):
            return 0
        return ans