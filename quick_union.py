class UF:
    def __init__(self, N):
        self.id = list(range(N))

    def connected(self, p, q):
        # If the root of p is the root of q, then they are connected.
        p_root = self.find_root(p)
        q_root = self.find_root(q)
        return p_root == q_root

    def find_root(self, i):
        root = i
        while True:
            if self.id[i] == i:
                root = i
                break
            else:
                i = self.id[i]
        return root

    def union(self, p, q):
        """ Set the root of p (position in the array) to the root of q """
        p_root = self.find_root(p)
        q_root = self.find_root(q)
        self.id[p_root] = q_root


test = UF(5)
print(test.id)
test.union(1,3)
test.union(1, 2)
print(test.connected(1,3))
print(test.connected(1,2))
print(test.connected(1,4))
print(test.id)
