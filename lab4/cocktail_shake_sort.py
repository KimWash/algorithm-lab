from checkSort import checkSort
import random, time
import sys

sys.setrecursionlimit(100000)


def cocktailShakerSort(a, n):
    d, i, k = True, 1, n
    while i <= k:
        if (d):
            for j in range(i, k):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
            k -= 1
        else:
            for j in range(k, 1, -1):
                if a[j] < a[j-1]:
                    a[j], a[j-1] = a[j-1], a[j]
            i += 1
        d = not d
for N in range(5000, 20001, 5000):
    a = [-1]
    for i in range(1, N+1):
        a.append(random.randint(1, N))
    # a = [-1, 6,5,4,3,2,1]
    # N = 6
    start_time = time.time()
    cocktailShakerSort(a, N)
    end_time = time.time() - start_time
    print('랜덤 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
    checkSort(a, N)

for N in range(5000, 20001, 5000):
    a = [-1]
    for i in range(1, N+1):
        a.append(i)
    start_time = time.time()
    cocktailShakerSort(a, N)
    end_time = time.time() - start_time
    print('정순 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
    checkSort(a, N)

for N in range(5000, 20001, 5000):
    a = [-1]
    for i in range(1, N+1):
        a.append(N - i)
    start_time = time.time()
    cocktailShakerSort(a, N)
    end_time = time.time() - start_time
    print('역순 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
    checkSort(a, N)
