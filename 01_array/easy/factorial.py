class Solution:
    def fn(self,n):
        if n < 0:
            return 0
        if n == 1 or n == 0:
            return 1
        
        return self.fn(n-1) * n

    def trailingZeroes(self, n: int) -> int:

        factorial = self.fn(n)
        # a = [int(list(item)) for item in str(factorial)]
        # a = [int(d) for d in str(factorial)]   
        count = 0 
        # for i in a:
        #     if i == 0:
        #         count += 1
        while factorial % 10 == 0:
            count += 1
            factorial //= 10
        return count

        return count  