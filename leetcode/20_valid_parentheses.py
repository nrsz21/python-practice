def is_valid(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    if len(s) % 2 != 0:
        return False
    for i in s:
        if i in pairs:
            top = stack.pop() if stack else None
            if top != pairs[i]:
                return False

        else:
            stack.append(i)
    return len(stack) == 0



print(is_valid("()"))        # 期待 True
print(is_valid("()[]{}"))    # 期待 True
print(is_valid("(]"))        # 期待 False
print(is_valid("([)]"))      # 期待 False
print(is_valid("{[]}"))      # 期待 True