def shortest_window_sort(arr):
    
    window_left_idx = None
    window_right_idx = None
    
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            window_left_idx = i
            break
            
    for i in range(n-2, -1, -1):
        if arr[i] > arr[i + 1]:
            window_right_idx = i
            break
            
    if window_left_idx == None and window_right_idx == None:
        return 0
        
        
    min_window_val = min(arr[window_left_idx:window_right_idx + 1])
    max_window_val = max(arr[window_left_idx:window_right_idx + 1])
    
    # extend the window to the left
    left_most_idx = window_left_idx
    right_most_idx = window_right_idx
    
    for i in range(window_left_idx, -1, -1):
        if arr[i] > min_window_val:
            left_most_idx = i
            
    for i in range(window_right_idx + 1, n):
        if arr[i] < max_window_val:
            right_most_idx = i
            
    return right_most_idx - left_most_idx + 1 
    
test_1 = [1, 2, 5, 3, 7, 10, 9, 12]
test_2 = [1, 3, 2, 0, -1, 7, 10]
test_3 = [1, 2, 3]
test_4 = [3, 2, 1]

print (shortest_window_sort(test_1))
print (shortest_window_sort(test_2))
print (shortest_window_sort(test_3))
print (shortest_window_sort(test_4))

