# 227. Basic Calculator II
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = '+'
        n = len(s)

        for i, char in enumerate(s):
            
            if char.isdigit():
                num = num * 10 + int(char)

            if char in '+-*/' or i == n - 1:
                
                if char == ' ' and i != n - 1:
                    continue
                
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(int(stack.pop() / num))

                if i != n - 1:
                    op = char
                    num = 0

        return sum(stack)

solution = Solution()
print(solution.calculate(" 3+5 / 2 "))  # Output: 5
print(solution.calculate("14-3/2"))      # Output: 13
