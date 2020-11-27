def bracket_match(text):
    if not text:
        return 0
    
    n = len(text)
    stack = [text[0]]
    for i in range(1, n):
        if stack and stack[-1] == '(' and text[i] == ')':
            stack.pop()
        else:
            stack.append(text[i])
    
    return len(stack)
    
test1 = ')'
test2 = '()()()()()'
test3 = '())('
print (bracket_match(test1))
print (bracket_match(test2))
print (bracket_match(test3))
