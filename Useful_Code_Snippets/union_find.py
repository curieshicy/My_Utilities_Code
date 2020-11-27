class DisjointSetUnion:
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]
        self.size = [1 for i in range(size + 1)]
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
		
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return px
			
        if self.size[px] > self.size[py]:
            px, py = py, px
		
		# component y is bigger than component x
        self.parent[px] = py
        self.size[py] += self.size[px]
		
        return py
		
		
dsu = DisjointSetUnion(35)


		
		
