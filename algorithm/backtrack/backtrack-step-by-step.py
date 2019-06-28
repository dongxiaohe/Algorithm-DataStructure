def iterate1(list, start, n, target, acc, result):
    print(acc)
    result.append(acc)
    if start == n: print("loop end"); return
    for i in range(start, n):
        iterate1(list, i + 1, n, target - list[i], acc + [list[i]], result)

def iterate2(list, start, n, target, acc, result):
    # print(acc)
    result.append(acc)
    if start == n: print("loop end"); return
    for i in range(start, n):
        if i > start and list[i - 1] == list[i]: continue
        iterate2(list, i + 1, n, target - list[i], acc + [list[i]], result)

def iterate3(list, start, n, target, acc, result):
    print(acc)
    result.append(acc)
    if target < 0: print("loop end"); return
    if target == 0: print("loop end"); return
    for i in range(start, n):
        iterate3(list, i, n, target - list[i], acc + [list[i]], result)

def iterate4(list, start, n, target, acc, result):
    print(acc)
    result.append(acc)
    if target < 0: print("loop end"); return
    if target == 0: print("loop end"); return
    for i in range(start, n):
        if i > start and list[i - 1] == list[i]: continue
        iterate4(list, i, n, target - list[i], acc + [list[i]], result)

def iterate5(list, i, target, mem):
    key = str(target) + ":" + str(i)
    if str in mem:
        return mem[str]
    if target < 0: return 0
    elif target == 0: return 1
    if i < 0: return 0
    if target < list[i]:
        toReturn = iterate5(list, i - 1, target, mem)
    else:
        toReturn = iterate5(list, i - 1, target, mem) + iterate5(list, i - 1, target - list[i], mem)
    mem[key] = toReturn
    return toReturn


# result = []
# list = [1,2,2,2,3]
# n = len(list)
# iterate3(list, 0, n, 10, [], result)
#
# print(len(result))

list = list(range(30)) + list(range(40))

print(iterate5([1,7,6,3,5,15], 5, 15, {}))


# acc = 0
# tmp = []
# for ele in result:
#     if ele not in tmp:
#         tmp.append(ele)
#         acc += 1
# print(acc)
# print(result)

"""
[]
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
loop end
[1, 2, 3, 5]
loop end
[1, 2, 4]
[1, 2, 4, 5]
loop end
[1, 2, 5]
loop end
[1, 3]
[1, 3, 4]
[1, 3, 4, 5]
loop end
[1, 3, 5]
loop end
[1, 4]
[1, 4, 5]
loop end
[1, 5]
loop end
[2]
[2, 3]
[2, 3, 4]
[2, 3, 4, 5]
loop end
[2, 3, 5]
loop end
[2, 4]
[2, 4, 5]
loop end
[2, 5]
loop end
[3]
[3, 4]
[3, 4, 5]
loop end
[3, 5]
loop end
[4]
[4, 5]
loop end
[5]
loop end
[]
"""