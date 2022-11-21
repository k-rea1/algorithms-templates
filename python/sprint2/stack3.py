def is_correct_bracket_seq(seq):
    stack = []

    for s in seq:
        if s in ['(', '[', '{']:
            stack.append(s)
        elif s in [')', ']', '}'] and len(stack) > 0:
            if s == ')' and stack[-1] == '(':
                stack.pop()
            elif s == ']' and stack[-1] == '[':
                stack.pop()
            elif s == '}' and stack[-1] == '{':
                stack.pop()
            else:
                break
    
    return len(stack) == 0
    
    


seq = input()
print (is_correct_bracket_seq(seq))