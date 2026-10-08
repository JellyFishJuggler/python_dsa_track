class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:

        l = 0
        w = 0
        ms = float('-inf')
        # avg = float('-inf')
        avg = 0


        for r in range(len(nums)):
            w += nums[r]

            if r - l + 1 == k:
                # avg = max(avg, w/len(nums))
                ms = max(ms, w)

                w -= nums[l]
                l = l + 1
        
        avg = ms/k
        return avg