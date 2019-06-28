def sum(nums, n, target, acc, start, result):
    # print(start)
    if start >= n:
        return
    elif target < 0:
        return
    elif target == 0:
        result.append(acc)
        return
    for i in range(0, n):  
        # print(start, i, acc + [nums[i]])
        sum(nums, n, target - nums[i], acc + [nums[i]], i, result)

result = []
sum(range(1, 6), 5, 5, [], 0, result)
print(result)
    
