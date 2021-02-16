def find_letter_case_string_permutations(str):
    permutations = []
    # follow the same logic of subset
    permutations.append(str)
    for i in range(len(str)):
        if str[i].isalpha():
            n = len(permutations)
            for j in range(n):
                copy_word = permutations[j]
                copy_word = copy_word[:i] + copy_word[i].swapcase() + copy_word[i+1:]
                permutations.append(copy_word)

    return permutations


def main():
    print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))
main()
