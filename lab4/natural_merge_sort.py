from checkSort import checkSort
import random, time
import csv
def makerun(a, n):
    r = []
    temp_r = [a[1]]
    for i in range(1, n):
        if i == n - 1:
            r.append(temp_r)
            r.append([a[i + 1]])
            break
        if a[i] <= a[i + 1]:
            temp_r.append(a[i + 1])
        else:
            r.append(temp_r)
            temp_r = [a[i + 1]]
    return r


def natural_merge_sort(r: list):
    if len(r) < 2:
        return r

    while len(r) > 1:
        merge_result = []  # 병합 결과를 저장할 리스트 초기화
        i, j = 0, 0  # 각 런의 인덱스 초기화
        while i < len(r[0]) and j < len(r[1]):
            if r[0][i] <= r[1][j]:
                merge_result.append(r[0][i])
                i += 1
            else:
                merge_result.append(r[1][j])
                j += 1

        # 남은 요소들을 병합 결과에 추가
        merge_result.extend(r[0][i:])
        merge_result.extend(r[1][j:])

        r.pop(0)  # 병합한 첫 번째 런 제거
        r.pop(0)  # 병합한 두 번째 런 제거
        r.append(merge_result)  # 병합된 결과를 다시 리스트에 추가
    return r[0]



with open('benchmark_nms.csv', 'w', newline='') as csvfile:
    csvWriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    methods = ["랜덤", "정순", "역순"]
    csvWriter.writerow(['', '5000', '10000', '15000', '20000'])
    for method in range(0, 3):
        row = [methods[method]]
        for N in range(5000, 20001, 5000):
            a = [0]
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
            a = natural_merge_sort(makerun(a, N))
            a.insert(0, 0)
            end_time = time.time() - start_time
            row.append(end_time)
            print('%s 정렬된 데이터를 입력으로 하는 교환 정렬 실행 시간 (N = %d) : %0.3f' % (methods[method], N, end_time))
            checkSort(a, N)
        csvWriter.writerow(row)