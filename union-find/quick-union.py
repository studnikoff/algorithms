class QuickUnion:
    def __init__(self, N: int) -> None:
        self.id_list = [i for i in range(N)]

    def root(self, p: int):
        while p != self.id_list[p]:
            self.id_list[p] = self.id_list[self.id_list[p]] # Path compression improvement
            p = self.id_list[p]
        return p

    def connected(self, p: int, q: int) -> bool:
        pr = self.root(p)
        qr = self.root(q)
        return pr == qr

    def union(self, p: int, q: int) -> None:
        if self.connected(p, q) is False:
            pr = self.root(p)
            qr = self.root(q)

            self.id_list[pr] = qr
        else:
            pass

    def __repr__(self):
        return ', '.join([f'{i}:{self.id_list[i]}' for i in range(len(self.id_list))])