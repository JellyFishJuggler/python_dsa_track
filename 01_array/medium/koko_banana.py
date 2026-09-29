class Solution:
    # linear searching
    def koko(self,piles,speed,h):

        hours = 0
        for i in piles:
            hours += (i + speed - 1) // speed
            if hours > h:
                return False
        return hours <= h

    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        pile = max(piles)
        for i in range(1, pile + 1):
            if self.koko(piles,i,h) == True:
                return i
        return pile