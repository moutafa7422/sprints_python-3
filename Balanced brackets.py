def isBalanced(s):
    stack = []
    for c in s:
        if c in "({[":
            stack.append(c)
        else:
            if not stack:
                return "NO"
            if c == ")" and stack[-1] == "(":
                stack.pop()
            elif c == "]" and stack[-1] == "[":
                stack.pop()
            elif c == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return "NO"
    if not stack:
        return "YES"
    else:
        return "NO"


print(isBalanced("{[(]}"))

# def is_balanced(s):
#     stack = []
#     for c in s:
#         if c in ['(', '{', '[']:
#             stack.append(c)
#         elif not stack or {')': '(', '}': '{', ']': '['}[c] != stack.pop():
#             return 'NO'
#     return 'YES' if not stack else 'NO'
#
#
# print(is_balanced("{[(]}"))