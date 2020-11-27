# Given a list, get products of other elements
# [1,2,3,4,5] --->> [120, 60, 40, 30, 24]
# [3, 2, 1] --->> [2, 3, 6]
import time

def products_of_other_elements_1(input_list):
    # use division---potential encounter of zero division and fail
    product = 1
    output_list = []
    # find product
    for i in input_list:
        product *= i

    for i in input_list:
        output_list.append(int(product / i))

    return output_list

def products_of_other_elements_2(input_list):

    output_list = []
    for idx, val in enumerate(input_list):
        product = 1
        idx_list = list(range(len(input_list)))
        idx_list.remove(idx)
        for j in idx_list:
            product *= input_list[j]
        output_list.append(product)

    return output_list

def products_of_other_elements_3(input_list):
    # calculate the prefix using DP
    prefix = []
    for i in input_list:
        if not prefix:
            prefix.append(input_list[0])
        else:
            prefix.append(prefix[-1] * i)
    # calculate the suffix using DP
    suffix = []
    reversed_list = input_list[::-1]
    for i in reversed_list:
        if not suffix:
            suffix.append(reversed_list[0])
        else:
            suffix.append(suffix[-1] * i)
    suffix = list(reversed(suffix))

    # calculate the product of prefix and suffix
    output_list = []
    for i in range(len(input_list)):
        if i == 0:
            output_list.append(suffix[i + 1])
        elif i == len(input_list) - 1:
            output_list.append(prefix[i - 1])
        else:
            output_list.append(prefix[i-1] * suffix[i+1])

    return output_list

print (products_of_other_elements_1([1,2,3,4,5]))
#print (products_of_other_elements_1([3,0,1]))

print (products_of_other_elements_2([1,2,3,4,5]))
print (products_of_other_elements_2([3,0,1]))

print (products_of_other_elements_3([1,2,3,4,5]))
print (products_of_other_elements_3([3,0,1]))


## time on large array
def record_time(N, method):
    test = [i for i in range(N)]
    if method == 2:
        start = time.time()
        products_of_other_elements_2(test)
        end = time.time()
        return end - start

    if method == 3:
        start = time.time()
        products_of_other_elements_3(test)
        end = time.time()
        return end - start


import numpy as np
import matplotlib.pyplot as plt
size_of_list = np.array([10, 100, 1000, 10000])
time_method_2 = np.array([record_time(i, 2) for i in size_of_list])
time_method_3 = np.array([record_time(i, 3) for i in size_of_list])

plt.plot(np.log10(size_of_list), time_method_2, 'bo-', markersize = 12, label = 'my method')
plt.plot(np.log10(size_of_list), time_method_3, 'ro-', markersize = 12, label = 'book method')
plt.xlabel('size of list', fontsize = 12)
plt.ylabel('time consumed', fontsize = 12)
plt.legend(loc = 0)
plt.title('compare different methods on run time', fontsize = 12)
plt.show()








