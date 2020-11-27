def in_place_reverse(arr, start, end):
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def reverse_words(arr):
    in_place_reverse(arr, 0, len(arr) - 1)
    start = 0
    end = None
    i = 0
    while i < len(arr):
        if arr[i] != ' ':
            i += 1
        else:
            end = i - 1
            in_place_reverse(arr, start, end)
            start = i + 1
            i += 1
            
    in_place_reverse(arr, start, len(arr) - 1)
    
    return arr
            
arr = ['p', 'e', 'r', 'f', 'e', 'c', 't', ' ',
       'm', 'a', 'k', 'e', 's', ' ',
       'p', 'r', 'a', 'c', 't', 'i', 'c', 'e']
       
print (reverse_words(arr))
