from checkSort import checkSort
import random, time
import csv

def selectionSort(a, n):
    for i in range(1, n):
        minIdx = i
        for j in range(i + 1, n + 1):
            if (a[minIdx] > a[j]):
                minIdx = j
        temp = a[i]
        a[i] = a[minIdx]
        a[minIdx] = temp
    return a



with open('benchmark_selection.csv', 'w', newline='') as csvfile:
    csvWriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    methods = ["랜덤", "정순", "역순"]
    csvWriter.writerow(['', '5000', '10000', '15000', '20000'])
    for method in range(0, 1):
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
            a = selectionSort(a, N)
            end_time = time.time() - start_time
            row.append(end_time)
            print('%s 정렬된 데이터를 입력으로 하는 교환 정렬 실행 시간 (N = %d) : %0.3f' % (methods[method], N, end_time))
            checkSort(a, N)
        csvWriter.writerow(row)