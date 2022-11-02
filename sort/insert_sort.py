def insert_sort(a: list):
    N = len(a)

    i = 1
    while i < N:
        j = i
        while (j >= 1) and (a[j-1] > a[j]):
            a[j-1], a[j] = a[j], a[j-1]
            j -= 1
        i+=1
    return a

if __name__ == '__main__':
    print(insert_sort([3,5,7,0,4,2]))
    print(insert_sort([0,0,0,1,1,2,-1]))