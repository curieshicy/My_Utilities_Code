from collections import deque
def nested_list_weight_sum_I(nested_list): # BFS
    queue = deque(nested_list)
    stack = []
    depth = 1
    while queue:
        for _ in range(len(queue)):
            cur_element = queue.popleft()
            if type(cur_element) == list:
                for element in cur_element:
                    queue.append(element)
            else:
                stack.append((cur_element, depth))
        depth += 1

    ans = 0
    max_depth = stack[-1][1]
    for val, depth in stack:
        ans += val * (max_depth - depth + 1)
    return ans

def nested_list_weight_sum_Ia(nested_list): # DFS
    def dfs(arr, stack, depth):
        for cur_element in arr:
            if type(cur_element) == list:
                dfs(cur_element, stack, depth + 1)
            else:
                stack.append((cur_element, depth))
        return stack

    stack = dfs(nested_list, [], 1)
    ans = 0
    max_depth = stack[-1][1]
    for val, depth in stack:
        ans += val * (max_depth - depth + 1)
    return ans    

def nested_list_weight_sum_II(nested_list):
    queue = deque(nested_list)
    stack = []
    depth = 1
    while queue:
        for _ in range(len(queue)):
            cur_element = queue.popleft()
            if type(cur_element) == list:
                for element in cur_element:
                    queue.append(element)
            else:
                stack.append((cur_element, depth))
        depth += 1

    ans = 0
    for val, depth in stack:
        ans += val * depth
    return ans

def unpack_nested_list(nested_list):
    def dfs(arr, stack):
        for cur_element in arr:
            if type(cur_element) == list:
                dfs(cur_element, stack)
            else:
                stack.append(cur_element)
        return stack

    return dfs(nested_list, [])

if __name__ == '__main__':
    arr_1 = [[1,1],2,[1,1]]
    arr_2 = [1,[4,[6]]]
    print (nested_list_weight_sum_I(arr_1))
    print (nested_list_weight_sum_I(arr_2))
    print (nested_list_weight_sum_Ia(arr_1))
    print (nested_list_weight_sum_Ia(arr_2))
    print (nested_list_weight_sum_II(arr_1))
    print (nested_list_weight_sum_II(arr_2))
    print (unpack_nested_list(arr_1))
    print (unpack_nested_list(arr_2))                         




    
