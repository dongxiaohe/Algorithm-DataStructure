def selectionSort(arr):
    for i in range(len(arr) - 1):
        imin = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[imin]:
                imin = j
        arr[i], arr[imin] = arr[imin], arr[i]

arr = [3,7,1,4,5,9,2,3]
selectionSort(arr)

print(arr)

