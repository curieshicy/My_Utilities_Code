# given ['code', 'edoc', 'da', 'd']
# find unique pairs of indices such that the concatenation of two words is a palindrome
# return [(0, 1), (1, 0), (2, 3)]

def generate_palindrome_pairs_1(input_list):

    def is_palindrome(s):
        if s == s[::-1]:
            return True
            
    res = []
    for i in range(len(input_list)):
        for j in range(len(input_list)):
            if is_palindrome(input_list[i] + input_list[j]) and i!=j:
                res.append((i,j))

    return res


def generate_palindrome_pairs_2(input_list):

    def is_palindrome(s):
        if s == s[::-1]:
            return True

    # build a word dictionary
    d = {}
    for idx, val in enumerate(input_list):
        d[val] = idx

    res = []

    for idx, word in enumerate(input_list):
        for char_i in range(len(word)):
            prefix, suffix = word[:char_i], word[char_i:]
            reversed_prefix, reversed_suffix = prefix[::-1], suffix[::-1]

            # condition 1
            if reversed_prefix in input_list and is_palindrome(suffix):
                if idx != d[reversed_prefix]:
                    res.append((idx, d[reversed_prefix]))

            # condition 2
            if reversed_suffix in input_list and is_palindrome(prefix):
                if idx != d[reversed_suffix]:
                    res.append((d[reversed_suffix], idx))

    return res





# test
input_list = ['code', 'edoc', 'da', 'd']
print (generate_palindrome_pairs_1(input_list))
print (generate_palindrome_pairs_2(input_list))
