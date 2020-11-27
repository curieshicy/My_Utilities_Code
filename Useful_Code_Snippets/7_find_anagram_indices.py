# find anagram indices
# e.g. given w = 'ab' and s = 'abxaba' return [0, 3, 4]
from collections import Counter, defaultdict

def find_anagram_indices_1(w, s):
    res = []
    for i in range(len(s) - len(w) +  1):
        if Counter(s[i : i + len(w)]) == Counter(w):
            res.append(i)
    return res

def find_anagram_indices_2(w, s):
    res = []
    # usual case
    for idx in range(len(s) - len(w) +  1):
        freq = defaultdict(int)
        for char in w:
            freq[char] += 1

        for char in s[idx: idx + len(w)]:
            freq[char] -= 1

        if all(i==0 for i in list(freq.values())):
            res.append(idx)

    return res




# test
w = 'ab'
s = 'abxaba'
print (find_anagram_indices_1(w, s))
print (find_anagram_indices_2(w, s))



