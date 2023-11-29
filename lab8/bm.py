def index(c):
    if ord(c) == 32:
        return 0
    else:
        return ord(c) - 64


def initSkip(p):
    for i in range(NUM):
        skip[i] = M
    for i in range(M):
        skip[index(p[i])] = M - i - 1


def BM(p, t, k):
    i, j = k + M - 1, M - 1
    initSkip(p)
    if i >= N: return N
    while j >= 0:
        while t[i] != p[j]:
            # 널문자 만나면 처리
            if t[i] == '\0': return N
            compCnt[k] += 1
            s = skip[index(t[i])]
            if M - j > s:
                i += M - j
            else:
                i += s
            if i >= N: return N
            j = M - 1
        i -= 1
        j -= 1
    return i + 1


NUM = 27
skip = [0] * NUM
text = 'VISION QUESTION ONION CAPTION GRADUATION EDUCATION' + '\0'
pattern = 'ATION'
M = len(pattern)
N = len(text)
K = 0

compCnt = [0] * N
print("보이어 무어 알고리즘")
while True:
    pos = BM(pattern, text, K)
    cnt = sum(compCnt)
    K = pos + 1
    if K <= N - M:
        print(f'패턴이 나타난 위치 : {pos} | 비교횟수: {cnt}')
    else:
        break
print('스트링 탐색 종료')
