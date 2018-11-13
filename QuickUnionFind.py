class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))

    def find(self, p):
        while self.parent[p] != p:
            p = self.parent[p]
        return p

    def union(self, p, q):
        p_id = self.find(p)
        q_id = self.find(q)

        self.parent[p_id] = q_id

    def connected(self, p, q):
        return self.find(p) == self.find(q)
