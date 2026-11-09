class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        sumi = float('-inf')

        ans = list()

        n = len(nums)

        for i in range(n):
            for j in range(i,n):
                for k in range(j,n):
                    if i != j and j != k and k != i:
                        sumi = nums[i] + nums[j] + nums[k]
                        if sumi == 0:
                            ans.append([nums[i], nums[j], nums[k]])

            s = set(tuple(sorted(row)) for row in ans)
            l = [list(x) for x in s]

        return l