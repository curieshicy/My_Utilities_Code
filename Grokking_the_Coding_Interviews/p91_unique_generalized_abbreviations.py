from collections import deque
def clean_up_word(list_of_chars):
    cleaned_word = []
    queue = deque(list_of_chars)
    while queue:
        char = queue.popleft()
        if char.isalpha():
            cleaned_word.append(char)
        else:
            if cleaned_word and cleaned_word[-1].isnumeric():
                new_number = int(char) + int(cleaned_word.pop())
                cleaned_word.append(str(new_number))
            else:
                cleaned_word.append(char)
                
    return ''.join(cleaned_word)
    
def generate_generalized_abbreviation(word):
    result = []
    result.append(word)
    for i in range(len(word)): # the depth equals to the length of the word
        n = len(result)
        for j in range(n):
            cur_word = list(result[j])
            cur_word[i] = '1'
            result.append(cur_word)
            
    ans = [clean_up_word(list(word)) for word in result]
    return ans

def main():
      print("Generalized abbreviation are: " +
            str(generate_generalized_abbreviation("BAT")))
      print("Generalized abbreviation are: " +
            str(generate_generalized_abbreviation("code")))

main()
