
def flip(arr, k):
    # reverse the first k elements
    start = 0
    end = k - 1
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
        
def pancake_sort(arr):
    for i in range(len(arr) - 1, -1, -1):
        largest_index = nums[:i + 1].index(max(nums[:i + 1]))
        flip(arr, largest_index + 1)
        flip(arr, i + 1)
        
    return arr
    
nums = [100, 20, 215, 1,5,4,3,2,8,9,10,15]
print (pancake_sort(nums))
