def make_squares(arr):
    def merge_two_sorted_arrs(arr_1, arr_2):
        len_arr_1 = len(arr_1)
        len_arr_2 = len(arr_2)
        sorted_arr = []
        i = 0
        j = 0
        while i < len_arr_1 and j < len_arr_2:
            if arr_1[i] <= arr_2[j]:
                sorted_arr.append(arr_1[i])
                i += 1
            else:
                sorted_arr.append(arr_2[j])
                j += 1

        while i < len_arr_1:
            sorted_arr.append(arr_1[i])
            i += 1

        while j < len(arr_2):
            sorted_arr.append(arr_2[j])
            j += 1
        return sorted_arr

    squared_arr_negative = []
    squared_arr_non_negative = []
    for num in arr:
        if num < 0:
            squared_arr_negative.append(num**2)
        else:
            squared_arr_non_negative.append(num**2)

    squared_arr_negative.reverse()
    return merge_two_sorted_arrs(squared_arr_negative, squared_arr_non_negative)
    
def make_squares_improved(arr):
    # find the idx of first non-negative number
    non_neg_idx = None
    for idx, num in enumerate(arr):
        if num >=0:
            non_neg_idx = idx
            break
    if idx == len(arr) - 1:
        squares = [i**2 for i in arr]
        squares.reverse()
        return squares
        
    if idx == 0:
        squares = [i**2 for i in arr]
        return squares
        
    # 0 ... non_neg_idx ||| non_neg_idx + 1...len(arr) - 1
    squares = []
    i = non_neg_idx -1
    j = non_neg_idx
    while i >= 0 and j < len(arr):
        if arr[i]**2 <= arr[j]**2:
            squares.append(arr[i]**2)
            i -= 1
        else:
            squares.append(arr[j]**2)
            j += 1
        
    while i >= 0:
        squares.append(arr[i]**2)
        i -= 1
        
    while j < len(arr):
        squares.append(arr[j]**2)
        j += 1
        
    return squares
    
def make_squares_optimal(arr):
    n = len(arr)
    squares = [0 for i in range(n)]
    i = 0
    j = n - 1
    highest_idx = n - 1
    while i <= j:
        left_squared = arr[i]**2
        right_squared = arr[j]**2
        if left_squared >= right_squared:
            squares[highest_idx] = left_squared
            i += 1
        else:
            squares[highest_idx] = right_squared
            j -= 1
        highest_idx -= 1
    return squares
    
    
test_1 = [-2, -1, 0, 2, 3]
test_2 = [-3, -1, 0, 1, 2]

print (make_squares(test_1))
print (make_squares_improved(test_1))
print (make_squares_optimal(test_1))
print (make_squares(test_2))
print (make_squares_improved(test_2))
print (make_squares_optimal(test_2))

















 
