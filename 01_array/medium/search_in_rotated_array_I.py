class Solution:
    # def fn(self, nums):
    #     j = 0
    #     pivot = 0

    #     for i in range(len(nums) - 1):
    #         if nums[i] > nums[i + 1]:
    #             pivot = 1 + i
    #             break

    #     l_nums = nums[:pivot]
    #     r_nums = nums[pivot:]

    #     return l_nums, r_nums, pivot

# O(logn)

    def search(self, nums: list[int], target: int) -> int:

        left = 0
        n = len(nums)
        right = n - 1


        while (left <= right):
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] < nums[right]:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] >= target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1


# O(n + 2logn)

        # l_num, r_num, pivot = self.fn(nums)

        # l_left, l_right = 0, len(l_num) - 1
        # r_left, r_right = 0, len(r_num) - 1

        # idx1, idx2 = -1, -1

        # while l_left <= l_right:
        #     m1 = l_left + (l_right - l_left) // 2

        #     if l_num[m1] == target:
        #         idx1 = m1
        #         break
        #     elif l_num[m1] < target:
        #         l_left = m1 + 1
        #     else:
        #         l_right = m1 - 1

        # while r_left <= r_right:
        #     m2 = r_left + (r_right - r_left) // 2

        #     if r_num[m2] == target:
        #         idx2 = m2
        #         break
        #     elif r_num[m2] > target:
        #         r_right = m2 - 1
        #     else:
        #         r_left = m2 + 1

        # if idx1 != -1:
        #     return idx1

        # if idx2 != -1:
        #     return idx2 + pivot

        # return -1
