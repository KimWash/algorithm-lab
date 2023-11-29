def bfs(start_node):
    visited = [False] * n
    q.put(start_node)
    visited[start_node] = True

    while not q.empty():
        node = q.get()
        print(node, end=' ')

        for adj in a[node]:
            if adj is not None and not visited[adj]:
                q.put(adj)
                visited[adj] = True


import queue

q = queue.Queue()
n = 6
a = [[1, 2, 3, 4, None], [0, 3, None], [0, 4, None], [0, 1, 4, 5, None], [0, 2, 3, 5, None], [3, 4, None]]
for i in range(n):
    visited = [False] * n
    print('bfs(%d) : ' % i, end='')
    bfs(i)
    print()
