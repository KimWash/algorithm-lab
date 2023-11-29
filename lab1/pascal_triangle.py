def pascalTriangle(h):
    res = []
    pre = [1]
    res.append(pre)
    i = 1
    while (i < h):
        cur = [1]
        j = 0
        while (j < len(pre) - 1):
            cur.append(pre[j] + pre[j + 1])
            j += 1
        cur.append(1)
        res.append(cur)
        pre = cur
        i += 1
    return res


H = int(input('높이 입력 : '))
result = pascalTriangle(H)
for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end=' ')
    print()
