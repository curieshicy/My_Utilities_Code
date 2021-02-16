def find_single_numbers(nums):
    n1xn2 = 0
    for num in nums:
        n1xn2 ^= num
        
    right_most_one_bit = 1
    while right_most_one_bit & n1xn2 == 0:
        right_most_one_bit = right_most_one_bit << 1
    
    num1, num2 = 0, 0
    for num in nums:
        if num & right_most_one_bit == 0:
            num1 ^= num
        else:
            num2 ^= num
            
    return [num1, num2]

def main():
    print('Single numbers are:' + str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
    print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))

main()
