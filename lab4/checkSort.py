import random, time
import sys

def checkSort(a, n):
    isSorted = True
    for i in range(1, n):
        if (a[i] > a[i + 1]):
            isSorted = False
        if (not isSorted):
            print(a[i], a[i+1], "정렬 안됨")
            break
    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")

