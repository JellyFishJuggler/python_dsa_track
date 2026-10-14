class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        left = 0
        # right = len(matrix[0]) - 1
        m = len(matrix)
        n = len(matrix[0])
        right = m*n - 1

        while left<=right:
            mid = left + (right - left) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1
            
        # O(m*logn)
        # for i in range(len(matrix)):
        #     while left <= right:
        #         mid = left + (right - left) // 2
        #         if matrix[i][mid] == target:
        #             return True
        #         elif matrix[i][mid] > target:
        #             left = mid + 1
        #         else:
        #             right = mid - 1


        
        return False