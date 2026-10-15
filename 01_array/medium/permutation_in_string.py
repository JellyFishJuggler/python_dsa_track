class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False

        d1 = dict()

        for right in range(n1):
            d1[s1[right]] = 1 + d1.get(s1[right], 0)

        d2 = dict()
        left = 0

        for right in range(n2):

            d2[s2[right]] = 1 + d2.get(s2[right], 0)
            
            if right - left + 1 > n1:
                d2[s2[left]] -= 1

                if d2[s2[left]] == 0:
                    del d2[s2[left]]

                left += 1

            if d1 == d2:
                return True

        return False