class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        d = dict()

        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
            for k,v in d.items():
                if v == 2:
                    return k
                
        