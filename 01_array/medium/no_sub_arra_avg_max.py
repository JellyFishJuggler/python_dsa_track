class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        
        l = 0
        w = 0
        
        # s = 0
        # mx = float('-inf')
        avgi = 0
        c = 0

        for r in range(len(arr)):
            w += arr[r]

            if r - l + 1 == k:
                avgi = w / k
                if threshold <= avgi:
                    # mx = max(mx,w)
                    c += 1
                w -= arr[l]
                l += 1
        return c
