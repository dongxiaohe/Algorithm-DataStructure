def bubbleSort(arr):
    for last in range(len(arr), 1, -1):
        flag = True
        for i in range(last - 1):
            if arr[i] > arr[i + 1]:
                flag = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i] 
        if flag: break

arr = [3,7,1,4,5,9,2,3]
bubbleSort(arr)

print(arr)
