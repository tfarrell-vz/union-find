class UF:
    def __init__(self, N):
        self.id = list(range(0,N))

    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]

        for i, root in enumerate(self.id):
            if root == pid:
                self.id[i] = qid

    def connected(self, p, q):
        return self.id[p] == self.id[q]


