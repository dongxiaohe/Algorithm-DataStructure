def sort_array(arr, digit, base = 10):
    counts = [[] for _ in range(base)]

    for num in arr:
        counts[num // base ** digit % base].append(num)

    result = []
    for bucket in counts:
        result.extend(bucket)
    return result

def radix_sort(arr, digits = 3):
    for digit in range(digits):
        arr = sort_array(arr, digit)
    return arr

arr = [100, 115, 103, 5, 3, 1, 23, 9, 15, 36, 27, 45]

print(radix_sort(arr))
