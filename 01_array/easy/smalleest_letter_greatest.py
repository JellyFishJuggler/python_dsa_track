class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        
        left = 0
        right = len(letters) - 1

        ans = letters[0]

        while left <= right:

            mid = left + (right - left) // 2
            track = letters[mid]

            if letters[mid] > target:
                ans = min(letters[mid],track)
                right = mid - 1
            else:
                left = mid + 1
        
        return ans