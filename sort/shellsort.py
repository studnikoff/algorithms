

def shell_sort(a: list) -> list:
    print('Input massive: ', a)
    h = 1
    N = len(a)

    while h <= N/3:
        h = 3*h + 1
    print(h)

    while h >= 1:
        i = h
        print('Offset: ', i)
        while i < N: 
            # Далее сортировка
            j=i
            print('Group head index: ', j)
            while j >= h:
                if a[j] < a[j-h]:
                    a[j-h], a[j] = a[j], a[j-h]
                j-=h
            i+=1
            print('Massive changing result: ', a)
        h = int((h-1)/3)
        
    return a

def shell_sort2(a: list) -> list:
    N = len(a)

    h = 1
    while h <= N/3:
        h = 3*h+1
    
    while h >= 1:
        j = h
        while j < N:
            i = j
            while (i >= h) and (a[i] < a[i-h]):
                a[i], a[i-h] = a[i-h], a[i]
                i -= h
            j+=1
        h = int((h-1)/3)
    return a



if __name__ == '__main__':
    print(shell_sort2([3,5,7,0,4,2]))
    print(shell_sort2([0,0,0,1,1,2,-1]))