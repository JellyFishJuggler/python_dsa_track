class Solution:

    def fn(self,nums,capacity):

        c = 1
        load = 0

        for i in nums:
            if i + load > capacity:
                c += 1
                load = i
            else:
                load += i
        return c

    def splitArray(self, nums: list[int], k: int) -> int:
        
        left = max(nums)
        right = sum(nums)

        while left <= right:
            mid = left + (right - left) // 2
            c = self.fn(nums,mid)
            if c <= k:
                right = mid - 1
            else:
                left = mid + 1
        return left