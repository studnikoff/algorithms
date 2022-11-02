from __future__ import annotations

class Quicksort:
    def __init__(self, N: int) -> None:
        pass

    def merge(a: list, b: list) -> list:
        pass


def merge(a: list, b: list) -> list:
    N_a = len(a)
    N_b = len(b)

    res = [None for i in range(N_a+N_b)]
    i = 0
    j = 0
    k = 0
    while k <= N_a+N_b-1:
        if i >= N_a:
            res[k] = b[j]
            j+=1
        elif j >= N_b:
            res[k] = a[i]
            i += 1
        elif a[i] <= b[j]:
            res[k] = a[i]
            i += 1
        elif a[i] > b[j]:
            res[k] = b[j]
            j += 1
        else:
            break
        print(res, i, j)
        k += 1

    return res

if __name__ == '__main__':
    a = [1,1,2,3,4]
    b = [1, 5, 7]

    res = merge(a,b)
    print('First', res)

    print('Second', merge([1,3,5,7], [2,2,3,4,7,8]))