class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        
        #selection sort
        for i in range(len(nums)):
            min = i
            for j in range(i+1,len(nums)):
                if nums[j] < nums[min]: 
                    min = j
            
            nums[i],nums[min] = nums[min],nums[i]
        # return nums
    
        #bubble sort
        for i in range(len(nums)):
            for j in range(0,len(nums) - i - 1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]

                
        
        return nums
    
    