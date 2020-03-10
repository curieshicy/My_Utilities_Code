bool_list = [True, True, False, True, False, True, 'x', False, True]

def find_longest_subarray(num):
    global_max = local_max = 0
    bool_val = num[0]

    for i in range(1, len(num)):
        if num[i] == 'x':
            local_max = 0
            i += 1

        elif num[i] != bool_val:
            local_max += 1
            bool_val = num[i]

        elif num[i] == bool_val:
            local_max = 0

        global_max = max(global_max, local_max)

        print (bool_val, i, local_max, global_max)

    return global_max + 2

print (find_longest_subarray(bool_list))
