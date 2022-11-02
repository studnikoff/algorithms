from cmath import sin


def swim(a: list, k: int):
    while (k > 0) & (a[int(k/2)] < a[k]):
        a[int(k/2)], a[k] = a[k], a[int(k/2)]
        k = int(k/2)
        # print(k)
    return a


def sink(a: list, k: int):
    N =  len(a)
    while 2*k+1 <= N-1:
        print(a)
        j = 2*k+1
        if (j < N-1) & (a[j] < a[j+1]):
            j+=1
        if (a[k] >= a[j]):
            break
        else:
            a[k], a[j] = a[j], a[k]
            k = j
    return a

def insert(a: list, num: int):
    a.append(num)
    N = len(a)
    return swim(a, N-1)

def del_max(heap: list):
    max = heap[0]
    N = len(heap)
    heap[N-1], heap[0] = heap[0], heap[N-1]
    heap[N-1] = -1 # prevent loitering
    print(sink(heap, 0))
    return max

if __name__ == '__main__':
     res = swim([5,4,3,6], 3)
     print(res)

     res = insert([5,4,3,2], 1)
     print(res)

     res = insert([5,4,3,2], 7)
     print(res)

     res = insert([6, 4, 3, 2], 5)
     print(res)

     res = sink([5, 2, 4, 1, 3], 1)
     print(res)

     res = sink([5, 2, 4, 1, 4, 3, 2, 0, 0, 0, 3], 1)
     print(res)

     res = del_max([5, 4, 4, 1, 3, 3, 2, 0, 0, 0, 2])
     print(res)

     