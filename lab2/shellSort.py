from checkSort import checkSort
import random, time

# def makeSubList(a, n, h):
#     sublists = []
#     for i in range(1, n/h):
#         sublist = [-1]
#         for j in range(1, n, h):
#             sublist.append(a[j])
#         sublists.append(sublist)
#     return sublists
#
# def shellSort(a, n):
#     h = 1
#     while h < n:
#         h = 3 * h + 1
#     while h > 0:
#         # 서브 리스트 만들기
#         sublists = makeSubList(a, n, h)
#         # 서브 리스트 삽입 정렬 하기
#
#         # 서브 리스트 병합 하기
#         h = int(h/3)
#     return a

def shellSort2(a,n):
    h = 1
    while h < n:
        h = 3 * h + 1
    while h > 0:
        for i in range(h+1, n+1):
            v,j = a[i], i
            while j > h and a[j-h] > v:
                a[j] = a[j-h]
                j -= h
            a[j] = v
        h = int(h/3)
    return a

N = 5000
N *= 4
# a = [, 3, 5, 2, 1, 6, 4, 9, 8]
# N = len(a) - 1
a = [None]
for i in range(N):
    a.append(N-i)
start_time = time.time()
a = shellSort2(a, N)
end_time = time.time() - start_time
print('쉘 정렬의 실행 시간 (N = %d) : %0.3f' % (N, end_time))
checkSort(a, N)
