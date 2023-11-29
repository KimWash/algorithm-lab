def binarySearch(a, key, left, right):
    if (left <= right):
        mid = int((left + right) / 2)
        if (key < a[mid]):
            return binarySearch(a, key, left, mid - 1)
        elif (key > a[mid]):
            return binarySearch(a, key, mid + 1, right)
        else: return mid
    else:
        return -1


listToFind = [1, 3, 7, 9, 10, 23, 24, 28, 30, 50, 70, 80, 100]
print(binarySearch(listToFind, 24, 0, len(listToFind)))
