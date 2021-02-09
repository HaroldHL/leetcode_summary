def isValid(s):
    dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
    stack = ['?']
    for c in s:
        if c in dic: stack.append(c)
        elif dic[stack.pop()] != c: return False 
    return len(stack) == 1
#即若遇到左括号入栈，遇到右括号时将对应栈顶左括号出栈，则遍历完所有括号后 stack 仍然为空
# 如果 c 是左括号，则入栈 pushpush；
# 否则通过哈希表判断括号对应关系，若 stack 栈顶出栈括号 stack.pop() 与当前遍历括号 c 不对应，则提前返回 false

print(isValid("(){}"))
print(isValid("(){}("))
