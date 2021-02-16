def calculate_bitwise_complement(n):
    '''
        8 --> 1000
        7 --> 0111
    '''
    binary = bin(n)[2:]
    new_binary = ''
    for ch in binary:
        if ch == '1':
            new_binary += '0'
        else:
            new_binary += '1'
    return int(new_binary, 2)
    
def calculate_bitwise_complement(n):
    '''
        8 --> 1000
    '''
    bit_count, num = 0, n
    while num:
        bit_count += 1
        num = num >> 1
    
    all_bits_set = 2**bit_count - 1
    
    return n ^ all_bits_set
    
    

def main():
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))

main()
