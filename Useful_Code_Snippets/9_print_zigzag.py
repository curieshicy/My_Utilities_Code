# s = 'thisisazigzag', k = 4
# print
# t      a     g
#  h    s z   a
#   i  i   i z
#    s      g

def print_zigzag(s, k):

    # 'initialize an empty list with k rows and len(s) columns'
    empty = [[' '] * len(s) for i in range(k)]

    col_idx = range(len(s))
    
    k_repeat_length = 2*k - 2 # 0, 1, 2, 3, 2, 1
    repeat = list(range(k)) + list(range(k))[::-1][1:-1]
    num_repeats = int(len(s) / k) + 1
    row_idx = repeat * num_repeats
    row_idx = row_idx[:len(s)]

    for i, j in zip(row_idx, col_idx):
        empty[i][j] = s[j]

    # pretty print
    for row in empty:
        print (''.join(row))


# test
s = 'thisisazigzag'
k = 4
print_zigzag(s, k)

