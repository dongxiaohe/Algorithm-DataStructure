def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)

arr = [7,2,3,7,2,3,4,12,1,3,4,4,2,2,1,1,2,30,15,17,13,23,27]
quicksort(arr)

def quicksort_new(array):
    n = len(array)
    if n == 0: return array
    pivot, left, right = array[0], [], []
    for i in range(1, n):
        if array[i] <= pivot: left.append(array[i])
        else: right.append(array[i])
    left = quicksort_new(left)
    right = quicksort_new(right)
    return left + [pivot] + right


print(arr)

print(quicksort_new(arr))

