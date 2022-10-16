class NotSortedArray(Exception):
    pass

def binary_search(l: list, val: int) -> int:
    # l -- уже отсортированный
    # необходимы уникальные значения
    for i in range(1, len(l)-1):
        if l[i+1] >= l[i]:
            pass
        else:
            raise NotSortedArray("Your input list is not sorted. Sort first")
    
    lo = 0
    hi = len(l)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if val < l[mid]:
            hi = mid - 1
        elif val > l[mid]:
            lo = mid + 1
        else:
            return mid
    return -1


def insert_sort(l: list):
    pass

def three_sum(l: list):
    l = sorted(l) # задача до реализации алгоритма с сортировкой, ключевой вклад в сложность
    
    res = list()
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            vi, vj = l[i], l[j]
            if vj > vi:
                key_sum = -(vi+vj)

                vz = binary_search(l, key_sum)
                if vz != -1:
                    res.append((vi, vj, l[vz]))
                else:
                    pass
    return res

