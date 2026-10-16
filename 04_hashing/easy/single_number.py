class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        
        a = dict()
        # count = 0

        for i in nums:
            if i in a:
                # count += 1
                a[i] += 1
            else:
                # count = 1
                a[i] = 1
            
        for key in a:
            if a[key] == 1:
                return key