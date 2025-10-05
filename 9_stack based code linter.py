# stack based code linter
def linter(code):
    stack = [] 
    opening = set("({[")
    close_to_open = {')': '(', '}': '{', ']': '['}
    open_to_close = {'(': ')', '{': '}', '[': ']'}

    for i, ch in enumerate(code):
        if ch in opening:
            stack.append((ch, i))
        elif ch in close_to_open:
            if not stack:
                return f"{ch} doesn't have an opening brace at index {i}"
            top, top_idx = stack.pop()
            if top != close_to_open[ch]:
                expected = open_to_close[top]
                return (f"{ch} has a mismatched opening brace at index {i}; "
                        f"expected {expected} to close {top} opened at index {top_idx}")

    if stack:
        top, top_idx = stack[-1]
        return f"{top} at index {top_idx} doesn't have a closing brace"

    return "All braces are matched"


# test cases
print(linter("if (a > b) { return a; }"))
print(linter("if (a > b) { return a; "))   
