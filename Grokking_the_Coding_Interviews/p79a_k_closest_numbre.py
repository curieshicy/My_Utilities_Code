import bisect
from collections import deque
def find_closest_elements(arr, K, X):
    idx_of_x = bisect.bisect_left(arr, X)
    if idx_of_x == len(arr):
        return arr[-K:]
    left = idx_of_x
    right = idx_of_x + 1
    res = deque()
    for _ in range(K):
        if left >= 0 and right < len(arr):
            if abs(arr[left] - X) < abs(arr[right] - X):
                res.appendleft(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1
                
        elif left >= 0:
            res.appendleft(arr[left])
            left -= 1
            
        elif right < len(arr):
            res.append(arr[right])
            right += 1
        
    return res

def main():
    print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))
main()
