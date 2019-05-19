def merge(left, right, A):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        A[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        A[k] = right[j]
        k += 1
        j += 1
    return A
def merge_sort(arr):
    if len(arr) < 2: return
    mid = len(arr) >> 1
    left = arr[: mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, arr)

arr = [3,7,1,4,5,9,2,3]
merge_sort(arr)
print(arr)
