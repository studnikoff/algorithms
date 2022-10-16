
class QuickFind:
    def __init__(self, N: int) -> None:
        self.id_list = [i for i in range(N)]

    def connected(self, p: int, q: int) -> bool:
        return self.id_list[p] == self.id_list[q]

    def union(self, p: int, q: int) -> None:
        """ union method implementation

        This method is not efficient. Initializing demand 
        for loop 

        Args:
            p (int): _description_
            q (int): _description_
        """        
        if self.connected(p, q) is True:
            pass
        else:
            pid = self.id_list[p]
            qid = self.id_list[q]
            for i in range(len(self.id_list)):
                if self.id_list[i] == qid:
                    self.id_list[i] = pid
                else:
                    pass

    def __repr__(self):
        return ', '.join([f'{i}:{self.id_list[i]}' for i in range(len(self.id_list))])