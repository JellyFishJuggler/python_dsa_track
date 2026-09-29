class Solution:

    # def koko(self,piles,speed,h):

    #     hours = 0
    #     for i in piles:
    #         hours += (i + speed - 1) // speed
    #         if hours > h:
    #             return False
    #     return hours <= h

    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        # pile = max(piles)
        # for i in range(1, pile + 1):
        #     if self.koko(piles,i,h) == True:
        #         return i
        # return pile

        left = 1
        right = max(piles)
        speed = float('inf')


        while left <= right:
            hours = 0
            mid = left + (right - left) // 2
            for i in piles:
                hours += (i + mid - 1) // mid
            
            if hours <= h:
                speed = min(speed, mid)
                right = mid - 1
            else:
                left = mid + 1
        return speed