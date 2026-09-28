class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        flg = False
        mid = left + (right - left) // 2

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:
                flg = True
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        # if flg == True:
        #     return mid
        # else:
        #     return left
        return left