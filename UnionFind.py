class UnionFind:  # Disjoint Sets
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))

    def find(self, i):
        return self.parent[i]

    def union(self, i, j):
        parent_i = self.parent[i]
        parent_j = self.parent[j]

        for index in range(self.n):
            if self.parent[index] == parent_j:
                self.parent[index] = parent_i

    def connected(self, i, j):
        return self.parent[i] == self.parent[
