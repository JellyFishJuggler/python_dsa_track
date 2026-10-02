class Solution:

    def fn(self,nums,l,r,k,first):
        ans = -1
        while l<=r:
            mid = l + (r - l) // 2
            if nums[mid] == k:
                ans = mid
                if first:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] > k:
                r = mid - 1
            else:
                l = mid + 1
        return ans


    def searchRange(self, nums: list[int], target: int) -> list[int]:
        
        left = 0
        right = len(nums) - 1
        mid = left + (right - left) // 2

        leftOcc = self.fn(nums,left,right,target,True)
        rightOcc = self.fn(nums,left,right,target,False)

        return [leftOcc,rightOcc]