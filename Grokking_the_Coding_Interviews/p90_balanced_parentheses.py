from collections import deque
def generate_valid_parentheses(num):
    def dfs(num_left_paren, num_right_paren, path, res):
        if len(path) == 2 * num:
            res.append(path)
            return
            
        if num_left_paren < num:
            dfs(num_left_paren + 1, num_right_paren, path + '(', res)
            
        if num_left_paren > num_right_paren:
            dfs(num_left_paren, num_right_paren + 1, path + ')', res)
        
        return res
    
    return dfs(0, 0, '', [])
    
    
def generate_valid_parentheses(num):
    result = []
    result.append('(')
    
    for _ in range(2 * num - 1):
        new_result = []
        for paren in result:
            num_left_paren = paren.count('(')
            num_right_paren = paren.count(')')
            if num_left_paren < num:
                new_result.append(paren + '(')
            if num_left_paren > num_right_paren:
                new_result.append(paren + ')')
        result = new_result
        
    return result


def generate_valid_parentheses(num):
    result = []
    queue = deque([(0, 0, '')])
    while queue:
        num_left_paren, num_right_paren, res = queue.popleft()
        if num_left_paren == num and num_right_paren == num:
            result.append(res)
        
        else:
            if num_left_paren < num:
                queue.append((num_left_paren + 1, num_right_paren, res + '('))
                
            if num_right_paren < num_left_paren:
                queue.append((num_left_paren, num_right_paren + 1, res + ')'))
            
    return result

def main():
    print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))


main()
