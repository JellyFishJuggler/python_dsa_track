class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        
        left = 0
        c = 0
        zc = 0

        maxi = 0

        for right in range(len(nums)):

            c += 1
            if nums[right] == 0:
                zc += 1
            while zc > k:
                c -= 1
                if nums[left] == 0:
                    zc -= 1 
                left += 1
            maxi = max(maxi, right - left + 1)
        
        return maxis