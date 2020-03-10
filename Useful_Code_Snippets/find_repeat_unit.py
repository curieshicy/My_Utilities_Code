def find_repeat_unit(s1, s2):

    def helper(s):
        mid_idx = len(s) // 2
        i = 1
        while i <= mid_idx:
            repeat = s[:i]
            num_repeats, reminder = divmod(len(s), len(repeat))
            if reminder == 0 and repeat * num_repeats == s:
                return s[:i]
            i+= 1

        return s

    if helper(s1) == helper(s2):
        return helper(s1)

    else:
        return ''

print (find_repeat_unit('ABCABC', 'ABCD'))
print (find_repeat_unit('ABABABC', 'ABAB'))
