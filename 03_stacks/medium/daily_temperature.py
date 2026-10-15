class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        stack = []
        ans = [0] * len(temperatures)

        for idx, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                stack_temp, stack_idx = stack.pop()
                ans[stack_idx] = idx - stack_idx
            stack.append([val,idx])

        return ans
        
        # for i in range(len(temperatures)):
        #     count = 0
        #     for j in range(i, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             count = j - i
        #             break
        #     stack.append(count)
        
        return stack