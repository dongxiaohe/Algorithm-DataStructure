# Recursion is fantastic and powerful. I would like to write down some tricks.

Iteration normally comes into two different ways.

## Recusion is in the return statement

Examples:

 - total combination sum (duplicate number is not allowed). i.e. [1, 3, 4, 7, 6] and target 7, the result is 4.

```

def dp(list, i, target, mem):
    key = str(target) + ":" + str(i)
    if str in mem:
        return mem[str]
    if target < 0: return 0
    elif target == 0: return 1
    if i < 0: return 0
    if target < list[i]:
        toReturn = dp(list, i - 1, target, mem)
    else:
        toReturn = dp(list, i - 1, target, mem) + dp(list, i - 1, target - list[i], mem)
    mem[key] = toReturn
    return toReturn

```

## Recursion method carries the result

Examples:

 - Combination sum (duplicate number is allowed).

```
def sum1(list, target, n, acc, result, start):
    if target < 0: return
    elif target == 0:
        result.append(acc)
        return
    else:
        for i in range(start, n):
            if list[i] > target: return
            else:
                sum1(list, target - list[i], n, acc + [list[i]], result, i)
```

 - Combination sum (duplicate number is not allowed).

```
def sum2(list, target, n, acc, result, start):
    if target < 0: return
    elif target == 0:
        result.append(acc)
        return
    else:
        for i in range(start, n):
            if list[i] > target: return
            if i > start and list[i] == list[i - 1]: continue
            else:
                sum2(list, target - list[i], n, acc + [list[i]], result, i + 1)
```

The pattern of this recursion looks like this:

```
def recursion(start, n):
    print(acc)
    if start == n: print("loop end"); return
    for i in range(start, n):
        recursion(i + 1, n)

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
```

- It can be seen the list must be sorted first.
- The first difference is is i + 1.
- The second difference is list[i] == list[i - 1], it make sure not to generate the duplicates list.
```
[1,2,2,3] [1,2] would generate twice from 1.

```