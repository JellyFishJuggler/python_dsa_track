class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        matching  = {
            ')' : '(',
            ']': '[',
            '}':'{'
        }

        for bracket in s:
            if bracket == '(' or bracket == '{' or bracket == '[':
                stack.append(bracket)
            else:
                if stack and stack[-1] == matching[bracket]:
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False