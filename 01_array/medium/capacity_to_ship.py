class Solution:

    def days(self,w,cap) -> int:

        dy = 1
        load = 0

        for i in w:
            if i + load > cap:
                dy += 1
                load = i
            else:
                load += i
        return dy

    def shipWithinDays(self, w: list[int], days: int) -> int:
        
        left = max(w)
        right = sum(w)

        while left <= right:

            mid = left + (right - left) // 2
            dy = self.days(w,mid)
            if dy <= days:
                # ans = dy
                right = mid - 1
            else:
                left = mid + 1    
        return left        
        # mid = left + (right - left) // 2
        # capacity = mid

        # for capacity in range(left,right+1):

        #     sumi = 0
        #     d = 1
        #     for i in w:
        #         if i + sumi > capacity:
        #             d += 1
        #             sumi = i
        #         else:
        #             sumi += i
        #     if d <= days:
        #         return capacity


