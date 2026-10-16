class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        d = dict()
        n = len(nums)
        count = 0
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in d:
            if d[i] > (n / 2):
                return i 