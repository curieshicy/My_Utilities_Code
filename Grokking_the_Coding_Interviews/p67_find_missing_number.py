def find_missing_number(arr):
    res = 0
    n = len(arr) + 1
    for i in range(1, n + 1):
        res ^= i
    
    for num in arr:
        res ^= num
        
    return res
    
def main():
    arr = [1, 5, 2, 6, 4] 
    print('Missing number is: ' + str(find_missing_number(arr)))
main()
