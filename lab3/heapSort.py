from checkSort import checkSort
import random, time
import sys

sys.setrecursionlimit(100000)


# h부터 m 까지 heapify
def heapify(a, h, m):
    v, j = a[h], 2 * h
    # 자식 노드 중 본인보다 큰 노드 찾기
    while (j <= m):
        # 더 값이 큰 값을 선택
        if j < m and a[j] < a[j + 1]: j += 1
        # 부모보다 더 큰 값을 찾으면 break
        if v >= a[j]:
            break
        else:
            a[j // 2] = a[j]
        j *= 2
    # break 됐거나 더 큰게 없어서 단말까지 온 경우 교환
    a[j//2] = v



def heapSort(a, n):
    # h 를 1씩 감소시키면서 힙 조건 만족하게 조작
    for i in range(n // 2, 0, -1):
        heapify(a, i, n)
    for i in range(n - 1, 0, -1):
        a[1], a[i + 1] = a[i + 1], a[1]
        heapify(a, 1, i)

for N in range(5000, 20001, 5000):
    a = [-1]
    for i in range(1, N+1):
        a.append(random.randint(1, N))
    start_time = time.time()
    heapSort(a, N)
    end_time = time.time() - start_time
    print('랜덤 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
    checkSort(a, N)

for N in range(5000, 20001, 5000):
    a = [-1]
    for i in range(1, N+1):
        a.append(i)
    start_time = time.time()
    heapSort(a, N)
    end_time = time.time() - start_time
    print('정순 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
    checkSort(a, N)

for N in range(5000, 20001, 5000):
    a = [-1]
    for i in range(1, N+1):
        a.append(N - i)
    start_time = time.time()
    heapSort(a, N)
    end_time = time.time() - start_time
    print('역순 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
    checkSort(a, N)
