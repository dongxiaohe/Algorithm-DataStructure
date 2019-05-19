import bisect
def insertionSort(arr):
    for i in range(1, len(arr)):
        position = bisect.bisect(arr[:i], arr[i]) # if the array is almost sorted, we can use insertion sort, it should be much quicker.
        value = arr[i]
        if position < i:
            arr[position + 1: i + 1] = arr[position: i]
            arr[position] = value

arr = [3,7,1,4,5,9,2,3]
insertionSort(arr)

print(arr)

