import sys
import random, time
from checkSort import checkSort

sys.setrecursionlimit(100000)


def partition(a, l, r):
    v = a[r]
    i = l - 1
    j = r

    while True:
        while True:
            i += 1
            if a[i] >= v: break
        while True:
            j -= 1
            if a[j] <= v: break
        if i >= j: break
        a[i], a[j] = a[j], a[i]
    a[i], a[r] = a[r], a[i]
    return i


def quickSort(a, l, r):
    if (r > l):
        i = partition(a, l, r)
        quickSort(a, l, i - 1)
        quickSort(a, i + 1, r)


for N in range(5000, 20001, 5000):
    a = [-1]
    for i in range(1, N+1):
        a.append(random.randint(1, N))
    start_time = time.time()
    quickSort(a, 1, N)
    end_time = time.time() - start_time
    print('랜덤 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
    checkSort(a, N)

for N in range(5000, 20001, 5000):
    a = [-1]
    for i in range(1, N+1):
        a.append(i)
    start_time = time.time()
    quickSort(a, 1, N)
    end_time = time.time() - start_time
    print('정순 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
    checkSort(a, N)

for N in range(5000, 20001, 5000):
    a = [-1]
    for i in range(1, N+1):
        a.append(N - i)
    start_time = time.time()
    quickSort(a, 1, N)
    end_time = time.time() - start_time
    print('역순 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
    checkSort(a, N)
