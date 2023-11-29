def dfs(v):
    # 방문하고 방문 기록 남기기
    visited[v] = True
    print(v, end=' ')

    # 방문 안한 노드 중 가장 첫번째 꺼 골라서 방문하즈아
    for i in range(len(a[v])):
        if a[v][i] is not None and not visited[a[v][i]]:
            dfs(a[v][i])


n = 6
a = [[1, 2, 3, 4, None], [0, 3, None], [0, 4, None], [0, 1, 4, 5, None], [0, 2, 3, 5, None], [3, 4, None]]
for i in range(n ):
    visited = [False] * n
    print('dfs(%d) : ' % i, end='')
    dfs(i)
    print()
