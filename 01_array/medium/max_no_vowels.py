class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        l = 0
        v = 0
        mv = float('-inf')

        vowels = ['a','e','i','o','u']

        for r in range(len(s)):
            if s[r] in vowels:
                v += 1
            if r - l + 1 == k:
                mv = max(v,mv)
                if s[l] in vowels:
                    v -= 1
                l += 1
            # if s[r] not in vowels:
            #     v -= 1 
        return mv