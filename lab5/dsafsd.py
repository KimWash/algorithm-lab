import heapq
import sys

input = sys.stdin.readline

class node:
    def __init__(self, key=None, index=None, ):
        self.key = key
        self.index = index

    def __lt__(self, other):
        if self.key < other.key:  # 오름차순
            return True
        elif self.key == other.key:
            return self.key > other.key  # 첫번재 변수가 같으면 두번재 변수로 내림차순
        else:
            return False


N, L = map(int, input().split())
numbers = list(map(int, input().split()))

min_list = []
min_heap = []

for i in range(N):
    while min_heap and min_heap[0].index < i - L + 1:
        # 범위에서 벗어난 노드를 제거
        heapq.heappop(min_heap)

    # 현재 범위에 들어오는 노드를 삽입
    heapq.heappush(min_heap, node(numbers[i], i))

    # 최솟값을 결과 배열에 추가
    min_list.append(min_heap[0].key)

# 결과 출력
print(" ".join(map(str, min_list)))
