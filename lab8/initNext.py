def initNext(p):
    j = 0
    next[0] = -1

    for i in range(1, M):
        next[i] = j
        while j >= 0 and p[i] != p[j]:
            j = next[j]
        j += 1

patterns = ['aaaaaaaaa', '00000001', '10100111', 'ababca', 'abababca', 'abcabcabc', 'abcabcacab', 'abracadabra', ]
print("initNext")
for pattern in patterns:
    M = len(pattern)
    next = [0] * M
    initNext(pattern)
    print(f"'{pattern}' 에 대한 재시작 위치 배열: ", next)