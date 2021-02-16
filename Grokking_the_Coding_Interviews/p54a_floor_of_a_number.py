def search_floor_of_a_number(arr, key):
    if key > arr[-1]:
        return len(arr) - 1
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
            
    return h

def main():
    print(search_floor_of_a_number([4, 6, 10], 6))
    print(search_floor_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_floor_of_a_number([4, 6, 10], 17))
    print(search_floor_of_a_number([4, 6, 10], -1))

main()
