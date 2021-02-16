def count_rotations(arr):
    l = 0
    h = len(arr) - 1
    while l <= h:
        m = (l + h) // 2
        if m < h and arr[m] > arr[m + 1]:
            return m + 1
        if m > l and arr[m - 1] > arr[m]:
            return m
        
        if arr[m] < arr[h]:
            h = m
        if arr[l] < arr[m]:
            l = m + 1
    return 0

def main():
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))

main()

