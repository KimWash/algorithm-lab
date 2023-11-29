class node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Dict:
    def __init__(self):
        self.node = None
        self.height = 0
        self.balance = 0

    def search(self, search_key):
        x = self.node
        while x is not None:
            if x.key == search_key:
                return x.key
            if x.key > search_key:
                x = x.left.node
            else:
                x = x.right.node
        return -1

    def insert(self, v):
        x = self.node
        if x is None:
            self.node = node(v)
            self.node.left = Dict()
            self.node.right = Dict()

        elif x.key > v:
            self.node.left.insert(v)

        else:
            self.node.right.insert(v)

        self.check_balance()

    def check_balance(self):
        self.update_heights(False)
        self.update_balances(False)

        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.rotate_left()
                self.rotate_right()

            else:
                if self.node.right.balance > 0:
                    self.node.right.rotate_right()
                self.rotate_left()

            self.update_heights()
            self.update_balances()

    def rotate_right(self):
        g = self.node
        p = g.left.node
        x = p.right.node
        self.node = p
        p.right.node = g
        g.left.node = x

    def rotate_left(self):
        g = self.node
        p = g.right.node
        x = p.left.node
        self.node = p
        p.left.node = g
        g.right.node = x

    def update_heights(self, recurse=True):
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_heights()
                if self.node.right is not None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height, self.node.right.height) + 1
        else:
            self.height = 0

    def update_balances(self, recurse=True):
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_balances()
                if self.node.right is not None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def check(self, search_key):
        x = self.node
        parent = x
        while x is not None:
            if x.key == search_key:
                print("key : {} , parents : {}".format(x.key, parent.key))
                return x.key
            if x.key > search_key:
                print("key : {} , parents : {}".format(x.key, parent.key))
                parent = x
                x = x.left.node
            else:
                print("key : {} , parents : {}".format(x.key, parent.key))
                parent = x
                x = x.right.node
        return -1


import random, time

import csv


def benchmark():
    with open('benchmark_avl_tree.csv', 'w', newline='') as csvfile:
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
                print('AVL 트리 %s 순서 탐색의 실행 시간 (N = %d) : %0.3f' % (methods[method], N, end_time))
            csvWriter.writerow(row)

def check():
    d = Dict()
    key = int(input('키 : '))
    while key != 999:
        d.insert(key)
        d.check(key)
        key = int(input('키 : '))


# benchmark()
check()
