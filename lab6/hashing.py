class Dict:
    def __init__(self):
        self.a = [-1] * M

    def insert(self, v):
        x = self.hash(v)
        # 삽입 알고리즘
        # index `x`에 삽입 시도, 이미 있으면 다음칸으로 넘어가면서 시도
        while self.a[x] != -1:
            # 구간 유지시키기
            x = (x + 1) % M
        self.a[x] = v

    def search(self, v):
        x = self.hash(v)
        # 탐색 알고리즘
        # 해싱 적용한 index가 비어 있지 않은 경우
        while self.a[x] != -1:
            # 값이 같으면 반환
            if v == self.a[x]:
                return self.a[x]
            # 다르면 다시 시도
            else:
                x = (x + 1) % M
        return -1

    def hash(self, v):
        return v % M


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
print('선형 탐사법의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
print('탐색 완료')
