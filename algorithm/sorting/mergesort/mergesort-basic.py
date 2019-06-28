# This is written after refering the CLRS book and hints from the site http://en.literateprograms.org/Merge_sort_(Python)

def merge(left, right):
    result, m, n, i, j = [], len(left), len(right), 0, 0
    while i < m and j < n:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def mergeSort(list):
    n = len(list)
    if n <= 1: return list
    mid = n >> 1
    left = mergeSort(list[:mid])
    right = mergeSort(list[mid:])
    return merge(left, right)

arr = [7,2,3,7,2,3,4,12,1,3,4,4,2,2,1,1,2,30,15,17,13,23,27]
print(arr)
print(mergeSort(arr))