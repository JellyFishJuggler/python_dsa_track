class Solution:

    def sumi(self,mid,nums):

        divisor_sum = 0
        for num in nums:
            divisor_sum += (num + mid - 1) // mid
        return divisor_sum


    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        
        left = 1
        right = max(nums)

        while left <= right:
            mid = left + (right - left) // 2
            div_sum = self.sumi(mid,nums)

            if div_sum > threshold:
                left = mid + 1
            else:
                right = mid - 1
        
        return left