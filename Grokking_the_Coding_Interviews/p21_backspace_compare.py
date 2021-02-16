def backspace_compare(str1, str2):
    def clean_up_string(s):
        stack = []
        for ch in s:
            if ch != '#':
                stack.append(ch)
            else:
                stack.pop()
        return ''.join(stack)
        
    return clean_up_string(str1) == clean_up_string(str2)
    
    

test1 = ['xy#z', 'xzz#']
test2 = ['xy#z', 'xyz#']
test3 = ['xp#', 'xyz##']
test4 = ['xywrrmp', 'xywrrmu#p']

print (backspace_compare(*test1))
print (backspace_compare(*test2))
print (backspace_compare(*test3))
print (backspace_compare(*test4))
