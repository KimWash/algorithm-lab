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
        parent = None
        while x != self.z:
            # 탐색 알고리즘
            if x.key < search_key:
                parent = x
                x = x.right
            elif x.key > search_key:
                parent = x
                x = x.left
            else:
                return (x.key, parent)
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

    def check(self, search_key):
        return self.search(search_key)


key = [2, 1, 7, 8, 6, 3, 5, 4]
s_key = [1, 2, 3, 4, 5, 6, 7, 8]
d = Dict()
for i in range(len(key)):
    d.insert(key[i])
for i in range(len(key)):
    result = d.check(s_key[i])
    if result[0] == -1 or result[0] != s_key[i]:
        print('탐색 오류')
    else:
        if result[1] == None:
            print("key: {} is root".format(s_key[i]))
        else:
            print("key: {}, parents: {}".format(s_key[i], result[1].key))
print('탐색 완료')
