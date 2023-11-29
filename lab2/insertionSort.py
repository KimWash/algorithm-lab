from checkSort import checkSort
import random, time


def insertionSort(a, n):
    for i in range(2, n + 1):
        v, j = a[i], i
        while a[j - 1] > v:
            a[j] = a[j-1]
            j -= 1
        a[j] = v
    return a


N = 5000
N *= 4
a = [-1]
for i in range(N):
    a.append(N-i)
start_time = time.time()
insertionSort(a, N)
end_time = time.time() - start_time
print('삽입 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
checkSort(a, N)
