class Dict:
    def __init__(self):
        self.a = [-1] * M

    def insert(self, v):
        x = self.hash(v)
        u = self.hash2(v)
        while self.a[x] != -1:
            x = self.hash(x + u)
        self.a[x] = v

    def search(self, v):
        x = self.hash(v)
        u = self.hash2(v)
        while self.a[x] != -1:
            if v == self.a[x]:
                return self.a[x]
            else:
                x = self.hash(x + u)
        return -1

    def hash(self, v):
        return v % M

    def hash2(self, v):
        return M - (v % M)


import random, time

N = 10000
M = 10391
key = []
s_key = []
for i in range(N):
    r = random.randint(1, 3 * N)
    key.append(r)
    s_key.append(r)
d = Dict()
for i in range(N):
    d.insert(key[i])
start_time = time.time()
for i in range(N):
    result = d.search(s_key[i])
    if result == -1 or result != s_key[i]:
        print('탐색 오류')
end_time = time.time() - start_time
print('이중 해싱의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
print('탐색 완료')
