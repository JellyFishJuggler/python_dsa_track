class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        length = 0
        maxlength = 0

        ss = set()

        for right in range(len(s)):
            if s[right] not in ss:
                ss.add(s[right])
                maxlength = max(maxlength, right - left + 1)
            else:
                while s[right] in ss:
                    ss.remove(s[left])
                    left += 1
                ss.add(s[right])

        
        # d = dict()

        # for right in range(len(s)):
            
        #     if s[right] in d:
        #         d[s[right]] += 1
        #     else:
        #         d[s[right]] = 1
            
        #     while d[s[right]] != 1:
        #         d[s[right]] -= 1
        #     left = left + 1

        #     maxlength = max(maxlength, right - left + 1)
    
        return maxlength
