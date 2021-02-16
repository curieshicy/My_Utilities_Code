def diff_ways_to_evaluate_expression(input):
    result = []
    if '*' not in input and '+' not in input and '-' not in input:
        result.append(int(input))
        
    else:
        for i in range(len(input)):
            if input[i] in ['+', '-', '*']:
                left_part = diff_ways_to_evaluate_expression(input[:i])
                right_part = diff_ways_to_evaluate_expression(input[i+1:])
                for part_1 in left_part:
                    for part_2 in right_part:
                        if input[i] == '*':
                            result.append(part_1 * part_2)
                        elif input[i] == '+':
                            result.append(part_1 + part_2)
                        elif input[i] == '-':
                            result.append(part_1 - part_2)
    
    return result


def main():
    print("Expression evaluations: " + str(diff_ways_to_evaluate_expression("1+2*3")))
    print("Expression evaluations: " + str(diff_ways_to_evaluate_expression("2*3-4-5")))


main()

