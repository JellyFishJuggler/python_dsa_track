class Solution:
    def prefix(self, nums, start, end):

        mul = [1] * len(nums)
        multiply = 1
        while start < end:
            mul[start] = multiply
            multiply *= nums[start]
            # mul.append(multiply)
            start += 1
        return mul

    def suffix(self, nums, start, end):
        
        mul = [1] * len(nums)
        multiply = 1
        while end >= start:
            mul[end] = multiply
            multiply *= nums[end]
            # mul.append(multiply)
            end -= 1
        return mul

    def productExceptSelf(self, nums: list[int]) -> list[int]:

        ans = list()
        prefix_list = self.prefix(nums, 0, len(nums))
        suffix_list = self.suffix(nums,0, len(nums)-1)

        for i in range(len(nums)):
            ans.append(prefix_list[i] * suffix_list[i])
        
        return ans