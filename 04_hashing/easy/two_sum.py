class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        d = dict()
        # ans = list()

        for i in range(len(nums)):
            
            d[nums[i]] = i

        for i in range(len(nums)):

            need = target - nums[i]
            if need in d and d[need] != i:
                return [i,d[need]]
        
        # return ans