from checkSort import checkSort
import random, time

def bubbleSort(a, n):
    for i in range(n, 1, -1):
        for j in range(1, i):
            if (a[j] > a[j+1]):
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    return a

for N in range(5000, 20001, 5000):
    a = [-1]
    for i in range(1, N+1):
        a.append(random.randint(1, N))
    # a = [-1, 6,5,4,3,2,1]
    # N = 6
    start_time = time.time()
    bubbleSort(a, N)
    end_time = time.time() - start_time
    print('랜덤 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
    checkSort(a, N)

for N in range(5000, 20001, 5000):
    a = [-1]
    for i in range(1, N+1):
        a.append(i)
    start_time = time.time()
    bubbleSort(a, N)
    end_time = time.time() - start_time
    print('정순 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
    checkSort(a, N)

for N in range(5000, 20001, 5000):
    a = [-1]
    for i in range(1, N+1):
        a.append(N - i)
    start_time = time.time()
    bubbleSort(a, N)
    end_time = time.time() - start_time
    print('역순 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
    checkSort(a, N)
