def find_happy_number(num):
    seen = set()
    
    def sum_of_squared_digits(num):
        summation_squared = 0
        while num:
            num, digit = divmod(num, 10)
            summation_squared += digit**2
        return summation_squared
    
    while num not in seen:
        seen.add(num)
        if num == 1:
            return True
        num = sum_of_squared_digits(num)
        
    return False
    
def main():
    print(find_happy_number(23))
    print(find_happy_number(12))
main()
