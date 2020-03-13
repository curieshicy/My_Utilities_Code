def count_letters(s):
    count = 1
    d = {}
    for i in range(len(s) - 1):
        if s[i + 1] == s[i]:
            count += 1
        else:
            d[s[i]] = count
            count = 1
    d[s[-1]] = d.get(s[-1], 0) + count    
    return d

def count_dups(s):
    ans = []
    count = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            ans.append(count)
            count = 1
    ans.append(count)
    return ans
s = list('aabbb')
print (count_letters(s))
print (count_dups(s))
