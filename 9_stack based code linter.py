# stack based code linter
# leetcode 20
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch in pairs.values():        
                stack.append(ch)
            elif ch in pairs:               
                if not stack:               
                    return False
                if stack.pop() != pairs[ch]:
                    return False
                
        return not stack  
