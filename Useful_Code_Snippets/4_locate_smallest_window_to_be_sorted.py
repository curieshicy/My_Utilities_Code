# locate smallest window to be sorted
# e.g. given [3, 7, 5, 6, 9] return (1,3)
import random
import time

def locate_smallest_window_to_be_sorted_1(nums):
    # method 1: compare original list and sorted list, find difference
    # original [3, 7, 5, 6, 9]
    # sorted   [3, 5, 6, 7, 9]
    nums_sorted = sorted(nums) # O(nlogn) time complexity
    min_bound, max_bound = None, None
    for idx in range(len(nums)):
        if nums[idx] != nums_sorted[idx] and min_bound is None:
            min_bound = idx

        elif nums[idx] != nums_sorted[idx]:
            max_bound = idx

    return (min_bound, max_bound)

def locate_smallest_window_to_be_sorted_2(nums):
    mismatch_idx = []
    for idx in range(len(nums)):
        if idx == 0 and nums[idx] > nums[idx + 1]:
            mismatch_idx.append(idx)

        elif idx == len(nums) - 1 and nums[idx] < nums[idx - 1]:
            mismatch_idx.append(idx)

        elif idx > 0 and idx < (len(nums) - 1) and (nums[idx] > min(nums[idx + 1:]) or nums[idx] < max(nums[:idx])):
            mismatch_idx.append(idx)
                
    return (min(mismatch_idx), max(mismatch_idx))

def locate_smallest_window_to_be_sorted_3(nums):
    # try to find a O(n) solution
    min_bound, max_bound = None, None
    max_seen, min_seen = float('-inf'), float('inf')

    for i in range(len(nums)):
        max_seen = max(max_seen, nums[i])
        if nums[i] < max_seen:
            max_bound = i

    for i in range(len(nums)-1, -1, -1):
        min_seen = min(min_seen, nums[i])
        if nums[i] > min_seen:
            min_bound = i

    return (min_bound, max_bound)
# test
test = [3, 7, 5, 6, 9]
print (locate_smallest_window_to_be_sorted_1(test))
print (locate_smallest_window_to_be_sorted_2(test))
print (locate_smallest_window_to_be_sorted_3(test))
## time on large array
def record_time(N, method):
    test = [i for i in range(N)]
    random.shuffle(test)
    if method == 1:
        start = time.time()
        locate_smallest_window_to_be_sorted_1(test)
        end = time.time()
        return end - start
    
    if method == 2:
        start = time.time()
        locate_smallest_window_to_be_sorted_2(test)
        end = time.time()
        return end - start

    if method == 3:
        start = time.time()
        locate_smallest_window_to_be_sorted_3(test)
        end = time.time()
        return end - start


import numpy as np
import matplotlib.pyplot as plt
size_of_list = np.array([10, 100, 1000, 10000])
time_method_1 = np.array([record_time(i, 1) for i in size_of_list])
time_method_2 = np.array([record_time(i, 2) for i in size_of_list])
time_method_3 = np.array([record_time(i, 2) for i in size_of_list])


plt.plot(np.log10(size_of_list), time_method_1, 'bo-', markersize = 12, label = 'method 1 sort')
plt.plot(np.log10(size_of_list), time_method_2, 'ro-', markersize = 12, label = 'method 2 compare before and after')
plt.plot(np.log10(size_of_list), time_method_3, 'go-', markersize = 12, label = 'book method')
plt.xlabel('size of list', fontsize = 12)
plt.ylabel('time consumed', fontsize = 12)
plt.legend(loc = 0)
plt.title('compare different methods on run time', fontsize = 12)
plt.show()



