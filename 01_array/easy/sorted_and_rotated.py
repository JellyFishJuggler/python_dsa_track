class Solution:
    def check(self, nums: List[int]) -> bool:

        n = len(nums)
        drop = 0 

        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                drop += 1
        return drop <= 1
        