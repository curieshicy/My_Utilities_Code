def vanila_binary_search(arr, target):
    l = 0
    h = len(arr) - 1
    while l <= h:
        mid = (l + h) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            h = mid - 1
    return None

def binary_search_left_most_element(arr, target):
    l = 0
    h = len(arr) - 1
    while l <=h:
        mid = (l + h) // 2
        if arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            h = mid - 1
        else:
            if mid == 0:
                return mid
            if arr[mid - 1] != target:
                return mid
            h = mid - 1
    return None

def binary_search_right_most_element(arr, target):
    l = 0
    h = len(arr) - 1
    while l <=h:
        mid = (l + h) // 2
        if arr[mid] < target:
            l = mid + 1
        elif arr[mid] > target:
            h = mid - 1
        else:
            if mid == len(arr) - 1:
                return mid
            if arr[mid + 1] != target:
                return mid
            l = mid + 1
    return None

def find_smallest_element_in_cyclically_shifted_arr(arr):
    l = 0
    h = len(arr) - 1
    while l < h:
        mid = (l + h) // 2
        if arr[mid] < arr[h]:
            h = mid
        else:
            l = mid + 1
    return l

target = 285
arr = [300, 310, 320, -14, -10, 2, 108, 108, 243, 285, 285, 285]
print (vanila_binary_search(arr, target))
print (binary_search_left_most_element(arr, target))
print (binary_search_right_most_element(arr, target))
print (find_smallest_element_in_cyclically_shifted_arr(arr))

