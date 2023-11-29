from checkSort import checkSort
import random, time
import sys
import csv
sys.setrecursionlimit(100000)


def merge(a, l, m, r):
    i, j, k, b = l, m + 1, l, [None] * len(a)
    while i <= m and j <= r:
        if a[i] < a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
        k += 1
    # 왼쪽 리스트의 마지막 원소가 오른쪽 리스트의 마지막 원소보다 작아서 i가 중간 지점을 넘게 되면
    # 분할한 오른쪽 리스트의 남은 아이템을 삽입한다.
    # 반대의 경우, 왼쪽 리스트의 남은 아이템들을 삽입한다.
    if i > m:
        for p in range(j, r + 1):
            b[k] = a[p]
            k += 1
    else:
        for p in range(i, m + 1):
            b[k] = a[p]
            k += 1
    for p in range(l, r + 1):
        a[p] = b[p]


def mergeSort(a, l, r):
    if r > l:
        m = (r + l) // 2
        mergeSort(a, l, m)
        mergeSort(a, m + 1, r)
        merge(a, l, m, r)

with open('benchmark_nms.csv', 'w', newline='') as csvfile:
    csvWriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    methods = ["랜덤", "정순", "역순"]
    csvWriter.writerow(['', '5000', '10000', '15000', '20000'])
    for method in range(0, 3):
        row = [methods[method]]
        for N in range(5000, 20001, 5000):
            a = [-1]
            if method == 0:
                for i in range(1, N + 1):
                    a.append(random.randint(1, N))
            elif method == 1:
                for i in range(1, N + 1):
                    a.append(i)
            else:
                for i in range(1, N + 1):
                    a.append(N - i)
            # a = [-1, 6,5,4,3,2,1]
            # N = 6
            start_time = time.time()
            mergeSort(a, 1, N)
            end_time = time.time() - start_time
            row.append(end_time)
            print('%s 정렬된 데이터를 입력으로 하는 교환 정렬 실행 시간 (N = %d) : %0.3f' % (methods[method], N, end_time))
            checkSort(a, N)
        csvWriter.writerow(row)
