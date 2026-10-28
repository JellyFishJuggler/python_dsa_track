class Solution:
    def findMin(self, nums: list[int]) -> int:
        
        n = len(nums)
        left = 0
        right = n -1

        minEle = float('inf')

        while left <= right:
            mid = left + (right - left) // 2
            if nums[left] <= nums[mid]:
                minEle = min(minEle, nums[left])
                left = mid + 1
            # elif nums[right] >= nums[mid]:
            #     minEle = min(minEle, nums[right])
            #     right = mid - 1  
            else:
                minEle = min(minEle, nums[mid])     
                left = mid + 1   
        return minEle