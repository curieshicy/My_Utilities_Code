'''
    arr = ['x', 'y', 'z']
    text = 'x y y z y z y x'
       l              ^
       r                  ^
    find the smallest substring in text that contains all words in arr
    return '' if such a substring doesn't exist
'''
from collections import defaultdict
def get_shortest_unique_substring(arr, text):
    d1 = defaultdict(int)
    for ch in arr:
        d1[ch] += 1
    length = len(arr)
    
    l = 0
    r = 0
    n = len(text)
    d2 = defaultdict(int)
    cur_len = 0
    ans = [None, None, float('inf')] # l_idx, r_idx, length
    while r < n:
        if text[r] not in d1:
            r += 1
        else:
            d2[text[r]] += 1
            if d2[text[r]] <= d1[text[r]]:
                cur_len += 1
            r += 1
        
        while l <= r and cur_len == length:
            if r - l + 1 < ans[2]:
                ans = [l, r, r - l + 1]
                
            if text[l] not in d1:
                l += 1
            else:
                d2[text[l]] -= 1
                
                if d2[text[l]] < d1[text[l]]:
                    cur_len -= 1
                l += 1
    if ans[0] == None or ans[1] == None:
        return ''
    return text[ans[0]:ans[1]]

arr = ['x', 'y', 'z']
text = 'axyyzyzyxb'
print (get_shortest_unique_substring(arr, text))
        
            
            
            
            
            
            
            
            
            
            
                
            
        
        
    
