def find_max_in_bitonic_array(arr):
    l = 0
    h = len(arr) - 1
    while l <= h:
        m = (l + h) // 2
        if m == 0 or m == len(arr) - 1:
            return arr[m]
            
        if arr[m-1] < arr[m] and arr[m] > arr[m + 1]:
            return arr[m]
            
        if arr[m - 1] < arr[m] < arr[m + 1]:
            l = m + 1
        
        if arr[m - 1] > arr[m] > arr[m + 1]:
            h = m - 1
        
    return -1

def find_max_in_bitonic_array(arr):
    l = 0
    h = len(arr) - 1
    while l < h:
        m = (l + h) // 2
        if arr[m] < arr[m + 1]:
            l = m + 1
        else:
            h = m
    return arr[l]


def main():
    print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
    print(find_max_in_bitonic_array([3, 8, 3, 1]))
    print(find_max_in_bitonic_array([1, 3, 8, 12]))
    print(find_max_in_bitonic_array([10, 9, 8]))


main()
