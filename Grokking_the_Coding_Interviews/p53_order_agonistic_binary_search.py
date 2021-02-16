def binary_search(arr, key):
    l = 0
    h = len(arr) - 1
    is_increase = True
    if arr[l] > arr[h]:
        is_increase = False
    
    while l <= h:
        m = (l + h) // 2
        if arr[m] == key:
            return m
        elif arr[m] < key:
            if is_increase:
                l = m + 1
            else:
                h = m - 1
        else:
            if is_increase:
                h = m -1
            else:
                l = m + 1
    return -1

def main():
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))

main()
