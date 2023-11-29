import csv


class node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class Dict:
    x = p = node

    z = node(key=0, left=0, right=0)
    z.left = z
    z.right = z
    head = node(key=0, left=0, right=z)

    def search(self, search_key):
        x = self.head.right
        while x != self.z:
            # 탐색 알고리즘
            if x.key < search_key:
                x = x.right
            elif x.key > search_key:
                x = x.left
            else:
                return x.key
        return -1

    def insert(self, v):
        x = p = self.head
        while x != self.z:
            p = x
            if x.key == v:
                return
            if x.key > v:
                x = x.left
            else:
                x = x.right
        x = node(key=v, left=self.z, right=self.z)
        if p.key > v:
            p.left = x
        else:
            p.right = x


import random, time

import csv


def benchmark():
    with open('benchmark_bst.csv', 'w', newline='') as csvfile:
        csvWriter = csv.writer(csvfile, delimiter=',',
                               quotechar='|', quoting=csv.QUOTE_MINIMAL)
        methods = ["랜덤", "정순", "역순"]
        csvWriter.writerow(['', '5000', '10000', '15000', '20000'])
        for method in range(0, 3):
            row = [methods[method]]
            for N in range(5000, 20001, 5000):
                key = []
                d = Dict()
                if method == 0:
                    for i in range(1, N+1):
                        key.append(random.randint(1, N+1))
                elif method == 1:
                    for i in range(1, N+1):
                        key.append(i)
                else:
                    for i in range(1, N+1):
                        key.append(N - i + 1)
                s_key = key.copy()
                random.shuffle(key)
                for i in range(N):
                    d.insert(key[i])
                start_time = time.time()
                for i in range(N):
                    result = d.search(s_key[i])
                    if result == -1 or result != s_key[i]:
                        print("탐색 오류")
                end_time = time.time() - start_time
                row.append(end_time)
                print('이진 탐색 트리 %s 순서 탐색의 실행 시간 (N = %d) : %0.3f' % (methods[method], N, end_time))
            csvWriter.writerow(row)


def check():
    d = Dict()
    key = int(input('키 : '))
    while key != 999:
        d.insert(key)
        key = int(input('키 : '))


benchmark()
