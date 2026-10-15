class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # left, length, maxLength = 0
        left = 0
        maxlength = float('-inf')
        maxfreq = 0
        d = dict()

        for right in range(len(s)):
            # d[s[right]] = 1 + d.get(s[right], 0)
            if s[right] in d:
                d[s[right]]  += 1
            else:
                d[s[right]] = 1

            
            #  while window - max(count.values()) > k:
            maxfreq = max(maxfreq, d[s[right]])
            while (right - left  + 1) - maxfreq > k:

                d[s[left]] -= 1
                left += 1
            maxlength = max(maxlength, right - left  + 1)

        
        return maxlength