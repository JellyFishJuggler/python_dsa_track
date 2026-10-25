class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        
        d = dict()

        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         if nums[i] == nums[j] and abs(i-j) <= k:
        #             return True

        for i in range(len(nums)):
            if nums[i] in d:
                if i - d[nums[i]] <= k:
                    return True
            # else:
            d[nums[i]] = i

        return False