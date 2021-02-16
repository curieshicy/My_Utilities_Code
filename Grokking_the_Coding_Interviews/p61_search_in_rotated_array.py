def search_rotated_array(arr, key):
    l = 0
    h = len(arr) - 1
    while  l <= h:
        m = (l + h) // 2
        if arr[m] == key:
            return m
            
        if arr[m] < arr[h]:
            if arr[m] < key <= arr[h]:
                l = m + 1
            else:
                h = m - 1
                
        if arr[m] > arr[h]:
            if arr[l] <= key < arr[m]:
                h = m - 1
            else:
                l = m + 1
    return -1


def main():
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 8))


main()
