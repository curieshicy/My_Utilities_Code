def find_range(arr, key):
    
    lower_idx = -1
    upper_idx = -1
    
    l = 0
    h = len(arr) - 1
    while l <= h:
        m = (l + h) // 2
        if arr[m] == key:
            if m == 0:
                lower_idx = m
                break
            if arr[m] != arr[m-1]:
                lower_idx = m
                break
            h = m - 1
            
        elif arr[m] < key:
            l = m + 1
        else:
            h = m - 1
    
    l = 0
    h = len(arr) - 1
    while l <= h:
        m = (l + h) // 2
        if arr[m] == key:
            if m == len(arr) - 1:
                upper_idx = m
                break
            if arr[m] != arr[m+1]:
                upper_idx = m
                break
            l = m + 1
            
        elif arr[m] < key:
            l = m + 1
        else:
            h = m - 1
    
    return [lower_idx, upper_idx]

def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))
main()
