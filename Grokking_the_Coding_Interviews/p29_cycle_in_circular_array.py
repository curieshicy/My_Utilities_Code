def is_loop_exist_from_current_idx(arr, idx):
    seen = set()
    while idx not in seen:
        seen.add(idx)
        next_idx = (idx + arr[idx]) % len(arr)
        if arr[next_idx] * arr[idx] < 0:
            return False
        if next_idx == idx:
            return False
        idx = next_idx
    return True

def circular_array_loop_exists(arr):
    for idx in range(len(arr)):
        if is_loop_exist_from_current_idx(arr, idx):
            return True
    return False
    
def main():
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))

main()
