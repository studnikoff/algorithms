import random


def shuffle(a: list) -> list:
    N = len(a)

    i=1
    while i < N:
        r = random.randint(0, i)
        a[r], a[i] = a[i], a[r]
        i+=1
    return a

if __name__ == '__main__':
    print(shuffle([0,1,2,3,4,5]))