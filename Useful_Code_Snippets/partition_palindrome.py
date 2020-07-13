
def partition(s):
    
    def dfs(string, path, res):
        if not string:
            res.append(path)

        for i in range(1, len(string) + 1):
            if string[:i] == string[:i][::-1]:
                dfs(string[i:], path + [string[:i]], res)

        return res


    return dfs(s, [], [])


print(partition('abba'))
