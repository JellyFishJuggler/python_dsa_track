class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        count = 0

        # for i in range(len(jewels)):
        #     for j in range(len(stones)):
        #         if jewels[i] == stones[j]:
        #             count += 1
        
        # d = dict()
        d = set(jewels)
        # for i in jewels:
        #     d[i] = True
        for i in stones:
            if i in d:
                count += 1
        return count