import bisect
def search_ceiling_of_a_number(arr, key):
    idx = bisect.bisect_left(arr, key)
    if idx == len(arr):
        return -1
    return idx 

def search_ceiling_of_a_number(arr, key):
    if key > arr[-1]:
        return -1
    if key < arr[0]:
        return 0
        
    l = 0
    h = len(arr) - 1
    while l <= h:
        m = ( l + h) // 2
        if arr[m] == key:
            return m
        elif arr[m] < key:
            l = m + 1
        else:
            h = m - 1
            
    return l

def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))

main()
