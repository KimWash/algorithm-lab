import csv


class node:
    def __init__(self, key=None):
        self.key = key


class Dict:
    def __init__(self):
        self.a = []

    def search(self, search_key, n):
        # 탐색 알고리즘
        # for i in range(0, n):
        #     if self.a[i].key == search_key: return i
        # return -1
        i = 0
        while i < n and self.a[i].key != search_key:
            i += 1
        if i == n: return -1
        else: return i

    def insert(self, v):
        self.a.append(node(v))


import random, time

with open('benchmark.csv', 'w', newline='') as csvfile:
    csvWriter = csv.writer(csvfile, delimiter=',',
                           quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csvWriter.writerow(['5000', '10000', '15000', '20000'])
    if (True):
        row = []
        for N in range(5000, 20001, 5000):
            key = list(range(1, N + 1))
            s_key = list(range(1, N + 1))
            random.shuffle(key)
            d = Dict()
            for i in range(N):
                d.insert(key[i])
            start_time = time.time()

            for i in range(N):
                result = d.search(s_key[i], N)
                if result == -1 or key[result] != s_key[i]:
                    print('탐색 오류')
            end_time = time.time() - start_time
            row.append(end_time)
            print('순차 탐색 실행 시간 (N = %d) : %0.3f' % (N, end_time))

        csvWriter.writerow(row)
