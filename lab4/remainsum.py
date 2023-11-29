import sys

input = sys.stdin.readline
N, M = map(int, input().split())
a = list(map(int, input().split()))

count = 0
cumsum = 0
remainder_count = [0] * M

for num in a:
    cumsum += num
    remainder = cumsum % M
    count += remainder_count[remainder]
    if remainder == 0:
        count += 1
    remainder_count[remainder] += 1

print(count)