class Solution:
    def totalFruit(self, fruits: list[int]) -> int:

        left = 0
        bucket = dict()
        ans = 0

        for right in range(len(fruits)):

            if fruits[right] in bucket:
                bucket[fruits[right]] += 1
            else:
                bucket[fruits[right]] = 1

            while len(bucket) > 2:
                bucket[fruits[left]] -= 1

                if bucket[fruits[left]] == 0:
                    del bucket[fruits[left]]

                left += 1

            ans = max(ans, right - left + 1)

        return ans