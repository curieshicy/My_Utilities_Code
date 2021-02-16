def search_next_letter(letters, key):
    
    if key >= letters[-1]:
        return letters[0]
        
    if key < letters[0]:
        return letters[0]
    
    l = 0
    h = len(letters) - 1
    while l <= h:
        m = (l + h) // 2
        if letters[m] == key:
            return letters[m + 1]
        
        elif letters[m] < key:
            l = m + 1
            
        else:
            h = m - 1
    return letters[l]
        

def main():
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'h'))

main()
