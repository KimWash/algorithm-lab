import sys
input = sys.stdin.readline

# N(표의 크기, N x N), M(합을 구해야 하는 횟수) 입력 받기
# print("N(표의 크기)과 M(합을 몇번 구할지)을 공백으로 구분해 입력해주세요.\n")
N, M = map(int, input().split())
# print()
# print(N, M)

# N x N 의 표 입력 받기
# print(str(N) + " x " + str(N) + "의 테이블을 공백과 개행으로 구분해 입력해주세요.\n")
a = []
for _ in range(N):
    b = list(map(int, input().split()))
    a.append(b)
# print(a)

# 네 개의 정수 x1, y1, x2, y2 로 이루어진 M개 행 입력 받기
# print("x1, y1, x2, y2를 공백으로 구분해 " + str(M) + "개 입력해주세요.\n")
coordinates = []
for _ in range(M):
    coordinates.append(list(map(int, input().split())))


    # print(coordinates)
    #
    # # M 개 행 계산하기
    # for k in range(len(coordinates)):
    #     cumsum = 0
    #     coordinate = coordinates[k]
    #     # x1부터 x2까지
    #     for i in range(coordinate[0], coordinate[2]+1):
    #         for j in range(coordinate[1], coordinate[3]+1):
    #             # print("x1: {}, y1: {}, x2: {}, y2: {}, i: {}, j: {}".format(coordinate[0], coordinate[1],
    #             #                                                             coordinate[2],
    #             #                                                             coordinate[3], i, j))
    #             cumsum += a[i-1][j-1]
    #
    #     print(cumsum)

# M개 행에 대해 매번 누적합을 계산하는 것이 아닌, (0,0) 에서 (i,j)까지의 누적합을 계산한 것을 모아두고 조합한다.
cumsum = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        cumsum[i][j] = a[i - 1][j - 1] + cumsum[i - 1][j] + cumsum[i][j - 1] - cumsum[i - 1][j - 1]

for k in range(M):
    [x1, y1, x2, y2] = coordinates[k]
    sum = cumsum[x2][y2] - (cumsum[x1 - 1][y2] + cumsum[x2][y1 - 1] - cumsum[x1 - 1][y1 - 1])
    print(sum)