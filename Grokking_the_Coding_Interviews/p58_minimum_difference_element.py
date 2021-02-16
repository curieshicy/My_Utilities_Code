def search_min_diff_element(arr, key):
    if key >= arr[-1]:
        return arr[-1]
        
    if key <= arr[0]:
        return arr[0]
        
    # find the ceiling of the key
    # the smallest number in the array that is greater or equal than key
    l = 0
    h = len(arr) - 1
    while l <= h:
        m = (l + h) // 2
        if arr[m] == key:
            return key
            
        elif arr[m] < key:
            l = m + 1
        else:
            h = m - 1
            
    if abs(arr[l] - key) > abs(arr[l-1] - key):
        return arr[l-1]
    else:
        return arr[l]
        
def search_min_diff_element_educative(arr, key):
    if key >= arr[-1]:
        return arr[-1]
        
    if key <= arr[0]:
        return arr[0]
        
    # find the ceiling of the key
    # the smallest number in the array that is greater or equal than key
    l = 0
    h = len(arr) - 1
    while l <= h:
        m = (l + h) // 2
        if arr[m] == key:
            return key
            
        elif arr[m] < key:
            l = m + 1
        else:
            h = m - 1
            
    if abs(arr[l] - key) > abs(arr[h] - key):
        return arr[h]
    else:
        return arr[l]

def main():
    print(search_min_diff_element_educative([4, 6, 10], 7))
    print(search_min_diff_element_educative([4, 6, 10], 4))
    print(search_min_diff_element_educative([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element_educative([4, 6, 10], 17))
main()
