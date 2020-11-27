# find number of the smaller elements to the right
# e.g. given [3, 4, 9, 6, 1] ---> [1, 1, 2, 1, 0]
# the first is 1 since there is only one item smaller than 3 to the right (i.e. 1)
# the second is 1 since there is only one item smaller than 4 to the right (i.e. 1)
# the third  is 2 since there is only one item smaller than 9 to the right (i.e. 1 and 6)
# the fourth is 1 since there is only one item smaller than 6 to the right (i.e. 1)
# the fifth is 0 since there is no item smaller than 1 to the right.
import bisect
import time
import random
import numpy as np
import matplotlib.pyplot as plt

def find_number_of_smaller_elements_to_the_right(nums):
    res = []

    for i in range(len(nums)):
        count = 0
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                count += 1
        res.append(count)
    return res


def find_number_of_smaller_elements_to_the_right_1(nums):
    res = []
    seen = []

    for num in reversed(nums):
        i = bisect.bisect_left(seen, num)
        res.append(i)
        bisect.insort(seen, num)
    
    return list(reversed(res))

test = [3, 4, 9, 6, 1]
print (find_number_of_smaller_elements_to_the_right(test))
print (find_number_of_smaller_elements_to_the_right_1(test))


## time on large array
def record_time(N, method):
    test = [i for i in range(N)]
    random.shuffle(test)
    if method == 1:
        start = time.time()
        find_number_of_smaller_elements_to_the_right(test)
        end = time.time()
        return end - start
    
    if method == 2:
        start = time.time()
        find_number_of_smaller_elements_to_the_right_1(test)
        end = time.time()
        return end - start

size_of_list = np.array([10, 100, 1000, 10000])
time_method_1 = np.array([record_time(i, 1) for i in size_of_list])
time_method_2 = np.array([record_time(i, 2) for i in size_of_list])

plt.plot(np.log10(size_of_list), time_method_1, 'bo-', markersize = 12, label = 'my method')
plt.plot(np.log10(size_of_list), time_method_2, 'ro-', markersize = 12, label = 'book method')
plt.xlabel('size of list', fontsize = 12)
plt.ylabel('time consumed', fontsize = 12)
plt.legend(loc = 0)
plt.title('compare different methods on run time', fontsize = 12)
plt.show()

