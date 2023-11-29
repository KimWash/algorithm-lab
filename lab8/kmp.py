def initNext(p):
    i, j = 1, 0
    next[0] = -1

    while i < M:
        next[i] = j
        while j >= 0 and p[i] != p[j]:
            j = next[j]
        i += 1
        j += 1


def KMP(p, t, k):
    initNext(p)
    i, j = k, 0
    while i < N and j < M:
        while j >= 0 and t[i] != p[j]:
            compCnt[k] += 1
            j = next[j]
        i += 1
        j += 1
    if j == M:
        return i - M
    else:
        return i


next = [0] * 50
text = 'ababababcababababcaabbabababca' + '\0'
pattern = 'abababca'
M = len(pattern)
N = len(text)
K = 0

compCnt = [0] * 50
print("KMP 알고리즘")
while True:
    pos = KMP(pattern, text, K)
    cnt = sum(compCnt)
    K = pos + 1
    if K <= N - M:
        print(f'패턴이 나타난 위치 : {pos} | 비교횟수: {cnt}')
    else:
        break

print('스트링 탐색 종료')
