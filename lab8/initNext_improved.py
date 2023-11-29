def initNext(p):
    i, j = 1, 0
    next[0] = -1

    while i < M:
        next[i] = j
        while j >= 0 and p[i] != p[j]:
            j = next[j]
        i += 1
        j += 1


patterns = ['aaaaaaaaa', '00000001', '10100111', 'ababca', 'abababca', 'abcabcabc', 'abcabcacab', 'abracadabra']
print("initNext 개선")
for pattern in patterns:
    M = len(pattern)
    next = [-1] * len(pattern)
    initNext(pattern)
    print(f"'{pattern}' 에 대한 재시작 위치 배열: ", next)
