def search_rotated_with_duplicates(arr, key):
    l = 0
    h = len(arr) - 1
    while l <= h:
        m = (l + h) // 2
        if arr[m] == key:
            return m
            
        if arr[l] == arr[m] and arr[m] == arr[h]:
            l += 1
            h -= 1
        
        elif arr[m] <= arr[h]:
            if arr[m] < key <= arr[h]:
                l = m + 1
            else:
                h = m - 1
        else:
            if arr[l] <= key < arr[m]:
                h = m - 1
            else:
                l = m + 1
                
    return -1
        
def main():
    print (search_rotated_with_duplicates([3, 7, 3, 3, 3], 7))
    
main()
