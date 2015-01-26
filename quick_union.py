class UF:
    def __init__(self, N):
        self.id = list(range(N))

    def connected(self, p, q):
        # If the root of p is the root of q, then they are connected.
        p_root = self.find_root(p)
        q_root = self.find_root(q)
        return p_root == q_root

    def find_root(self, p):
        i = p
        root = i
        while True:
            if self.id[i] == i:
                root = i
                break
            else:
                i = self.id[i]
        return root
