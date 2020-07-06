# leetcode 547
class Solution:
    def findCircleNum(self, M):
        count = 0
        seen = set()
        for person in range(len(M)):
            if person not in seen:
                count += 1
                self.dfs(person, M, seen)
        return count
        
    
    def dfs(self, node, M, seen):
        for person, is_friend in enumerate(M[node]):
            if is_friend and person not in seen:
                seen.add(person)
                self.dfs(person, M, seen)

