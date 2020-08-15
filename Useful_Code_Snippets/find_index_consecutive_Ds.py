'''
    01234
    DIIDD
    The goal is to find the index of D
    In the above example,
    the code should return (0,0) and (3,4)
'''

def find_index_consecutive_Ds(s):
    s += 'Z'
    res = []
    start = 0
    i = 0
    while i < len(s):
        if s[i] != 'D':
            i += 1
            continue
        
        if s[i] == 'D':
            start = i
            while s[i] == 'D':
                i += 1

        res.append((start, i - 1))
    return res

print (find_index_consecutive_Ds('DIIDDID'))
    
