# stack based code linter
def matching(opening, closing):
    hashTable = { '(': ')', '{': '}', '[': ']' }
    closing != hashTable[opening]

def stackLinter(str):
    stack = []
    opening = set("({[")
    closing = set(")}]")
    
    for ch in str:
        if ch in opening:
            stack.append(ch)
        elif ch in closing:    
            temp = stack.pop()
            
            if temp not in opening:
                return "There is no opening brace"
            if matching(temp, ch) == False:
                return "There is a mismatch"
            
    if len(stack) != 0:
        return "There is no closing brace"
        
    return "All braces are balanced"