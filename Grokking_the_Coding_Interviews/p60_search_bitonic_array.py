def search_bitonic_array(arr, key):
    # find the index of max
    l = 0
    h = len(arr) - 1
    
    while l < h:
        m = (l + h) // 2
        if arr[m] < arr[m+1]:
            l = m + 1
        else:
            h = m
    
    max_index = l # or h
    
    def binary_search(nums, low, high, target, ascending):
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if ascending == True:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if ascending == True:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1
        
    if max_index == 0:
        return binary_search(arr, 0, len(arr) - 1, key, False)
        
    if max_index == len(arr) - 1:
        return binary_search(arr, 0, len(arr) - 1, key, True)   
        
    idx_1 =  binary_search(arr, 0, max_index, key, True) 
    idx_2 = binary_search(arr, max_index + 1, len(arr) - 1, key, False)
    if idx_1 == -1 and idx_2 == -1:
        return -1
    if idx_1 != -1:
        return idx_1
    if idx_2 != -1:
        return idx_2

def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))
    print(search_bitonic_array([10, 9, 8], 1))
main()
