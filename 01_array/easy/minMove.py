class Solution:
    def minMoves(self, nums: List[int]) -> int:

        sumi = sum(max(nums) - x for x in nums)
        return sumi
        
        # n = len(nums)
        # maxi = float('-inf')
        # for i in range(n):
        #     maxi = max(maxi, nums[i])
        
        # d = dict()
        # for i in nums:
        #     need = maxi - i
        #     if need in d:
        #         d[i] += 1
        #     elif need == 0:
        #         d[i] = 0
        #     else:
        #         d[i] = 1
    
        # sumi = 0
        # for value in d.values():
        #     sumi += value
        