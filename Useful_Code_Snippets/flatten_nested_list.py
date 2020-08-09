# flatten nested list
def flatten_nested_list(nested_list):
    def flatten(nested_l, res):
        for element in nested_l:
            if type(element) == int:
                res.append(element)
            else:
                flatten(element, res)
        return res

    return flatten(nested_list, [])

print (flatten_nested_list([1,[4,[6]]]))
print (flatten_nested_list([[1,1],2,[1,1]]))
    
