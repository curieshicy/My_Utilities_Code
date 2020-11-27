from itertools import permutations, combinations
import time

with open('words_alpha.txt') as file:
    all_words = file.readlines()

# in total 235886 words
cleaned_words = {}
for word in all_words:
    cleaned_word = word[:-2][:-1].lower()
    cleaned_words[cleaned_word] = cleaned_words.get(cleaned_word, 0 ) + 1
    
word_wheel = ['u', 'c', 'g', 'i', 'm', 'n', 'o', 't']
# must include 'p'

def find_words(word_length, must_include_letter):
    length_without_must_include = word_length - 1
    combi = list(combinations(word_wheel, length_without_must_include))
    valid_words = []
    for each_combi in combi:
        temp = list(each_combi)
        temp.append(must_include_letter)
        permuts = list(permutations(temp))
        for permut in permuts:
            word_form = ''.join(list(permut))
            if word_form in cleaned_words:
                valid_words.append(word_form)
    return valid_words
    
start = time.time()
for i in range(4, 10):
    print('below are the words with a total length of {}'.format(i))
    print (find_words(i, 'p'))

end = time.time()
print ('it takes {} seconds to find all words'.format(end - start) )
    

