from heap import del_max


class BHeap:
    def __init__(self, heap: list) -> None:
        self.bh = list(heap)
        self.N = len(heap)

    def __less(self, i: int, j: int) -> bool:
        if (self.bh[i] is None) | (self.bh[j] is None):
            return False
        else:
            return self.bh[i] <= self.bh[j]

    def __exch(self, i: int, j: int) -> None:
        self.bh[i], self.bh[j] = self.bh[j], self.bh[i]

    def __repr__(self) -> str:
        return f'Array: {self.bh}, size: {self.N}'

    def swim(self, k: int) -> None:
        while k > 0:
            j = (k-1)//2

            if self.__less(k, j):
                break
            else:
                self.__exch(k, j)
                k = j

    
    def sink(self, k: int) -> None:
        while (2*k+1 <= self.N-1):
            j = 2*k+1
            if (j < self.N-1):
                if self.__less(j, j+1):
                    j += 1

            if self.__less(k, j):
                self.__exch(k, j)
                k = j
            else:
                break

    def insert(self, num: int) -> None:
        self.bh.append(None)
        self.N += 1
        self.bh[self.N-1] = num
        self.swim(self.N-1)


    def del_max(self) -> None:
        max = self.bh[0]
        self.__exch(0, self.N-1)
        self.bh[self.N-1] = None
        self.N -= 1
        self.sink(0)
        return max


if __name__ == '__main__':
    bh = BHeap([5,4,3,6])
    bh.swim(3)
    print(bh)
    
    bh = BHeap([5,4,3,6])
    bh.swim(1)
    print(bh)

    bh = BHeap([5,4,3,6])
    bh.swim(2)
    print(bh)

    bh = BHeap([5,4,3,2])
    bh.insert(7)
    print(bh)

    bh = BHeap([6, 4, 3, 2])
    bh.insert(5)
    print(bh)

    bh = BHeap([5, 2, 4, 1, 4, 3, 2, 0, 0, 0, 3])
    bh.sink(1)
    print(bh)

    print(bh, bh.del_max())

    bh.insert(10)
    print(bh)

    for i in range(3):
        print('Max is', bh.del_max(), 'Loop delete: ', bh)


    # Протестируем конструктор из неотсортированного списка (только для полного бинарного дерева)

    l = [i for i in range(8)]
    bh = BHeap(l)

    k = int((bh.N-2)//2)
    print(bh, k)
    while k >= 0:
        bh.sink(k)
        print(bh)
        k -= 1

    # Отсортируем массив
    def exch(a: list, i: int, j: int):
        a[i], a[j] = a[j], a[i]
        return a

    while bh.N > 0:
        exch(bh.bh, 0, bh.N-1)
        bh.N -= 1
        bh.sink(0)
    print('Heap sorted array: ', bh)