class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        sumi = 0 #prefix sum
        
        d = {0:1}   #storing the prefix sum and its frequency in a dictionary   
        
        for i in nums:
            sumi += i

            if sumi - k in d:
                count += d[sumi - k]
            if sumi in d:
                d[sumi] += 1
            else:
                d[sumi] = 1
                       
        return count
            
        
