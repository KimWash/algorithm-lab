import random


def twoSum(a, n, t):
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            if a[i] + a[j] == t:
                print(str(i + 1) + " 번째와 " + str(j + 1) + " 번째 원소")
            j += 1
        i += 1


N = int(input('리스트의 원소 개수 : '))
A = []
for i in range(N):
    A.append(random.randint(1, N * 2))
print('리스트 : ', A)
T = int(input('목표값 입력 : '))
print('두 수의 합이 %d인 원소 쌍' % T)
twoSum(A, N, T)
