def find_single_number(arr):
    single_num = 0
    for num in arr:
        single_num ^= num
        
    return single_num

def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))

main()
