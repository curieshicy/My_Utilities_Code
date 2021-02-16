from collections import deque, defaultdict
def find_order(words):
    if not words:
        return ""
    if len(words) == 1:
        return words[0][0]
        
    indegrees = defaultdict(int)
    graph = defaultdict(list)
    num_words = len(words)
    edges = set()
    for i in range(1, num_words):
        min_length = min(len(words[i-1]), len(words[i]))
        for j in range(min_length):
            if words[i-1][j] == words[i][j]:
                continue
            edges.add((words[i-1][j], words[i][j]))
            break
    all_chars = set()
    for u, v in edges:
        all_chars.add(u)
        all_chars.add(v)
        indegrees[v] += 1
        graph[u].append(v)
        
    queue = deque()
    for char in all_chars:
        if indegrees[char] == 0:
            queue.append(char)
    
    ans = ''
    while queue:
        node = queue.popleft()
        ans += node
        for neighbor in graph[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)
                
    if len(ans) != len(indegrees):
        return ''

    return ans


def main():
    print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
    print("Character order: " + find_order(["cab", "aaa", "aab"]))
    print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))


main()
