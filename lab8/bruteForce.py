def bruteForce(p, t, k):
    i = k
    j = 0

    while j < M and i < N:
        compCnt[k] += 1
        if t[i] != p[j]:
            i = i - j + 1
            j = 0
        else:
            i += 1
            j += 1

    if j == M:
        return i - M
    else:
        return i


text = 'ababababcababababcaabbabababca' + '\0'
pattern = 'abababca'
compCnt = [0] * len(text)
M = len(pattern)
N = len(text)
K = 0
print("직선적 알고리즘")
while True:
    pos = bruteForce(pattern, text, K)
    cnt = sum(compCnt)
    K = pos + M
    if K < N:
        print(f'패턴이 나타난 위치 : {pos}\t| 비교횟수: {cnt}')
    else:
        break
print('스트링 탐색 종료')
