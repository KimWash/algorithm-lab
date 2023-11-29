import csv


class node:
    def __init__(self, key=None):
        self.key = key


class Dict:
    def __init__(self):
        self.a = []

    def search(self, search_key, n):
        # 탐색 알고리즘
        left, right = 0, n - 1
        while left <= right:
            # 중간 구하기
            mid = left + (right - left) // 2
            # 오른쪽 영역으로 이동
            if self.a[mid].key < search_key:
                left = mid + 1
            # 왼쪽 영역
            elif self.a[mid].key > search_key:
                right = mid - 1
            else:
                return mid
        return -1

    def insert(self, v):
        self.a.append(node(v))


import random, time

def benchmark():
    with open('benchmark__tree.csv', 'w', newline='') as csvfile:
        csvWriter = csv.writer(csvfile, delimiter=',',
                               quotechar='|', quoting=csv.QUOTE_MINIMAL)
        methods = ["랜덤", "정순", "역순"]
        csvWriter.writerow(['', '5000', '10000', '15000', '20000'])
        for method in range(0, 3):
            row = [methods[method]]
            for N in range(5000, 20001, 5000):
                s_key = list(range(1, N + 1))
                d = Dict()
                if method == 0:
                    for i in range(1, N + 1):
                        d.insert(random.randint(1, N))
                elif method == 1:
                    for i in range(1, N + 1):
                        d.insert(i)
                else:
                    for i in range(1, N + 1):
                        d.insert(N - i)
                start_time = time.time()
                for i in range(N):
                    result = d.search(s_key[i])
                    if result == -1 or result != s_key[i]:
                        print("탐색 오류")
                end_time = time.time() - start_time
                row.append(end_time)
                print('AVL 트리 탐색의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
            csvWriter.writerow(row)