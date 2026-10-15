class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        stack = []
        
        for operator in tokens:            

            if operator == '+':
                stack.append(stack.pop() + stack.pop())
            elif  operator == '*':
                stack.append(stack.pop() * stack.pop())
            elif operator == '-':
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif operator == '/':
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(operator))
            
        return stack[-1]