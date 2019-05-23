def combine(n, k):
    result, i, p = [], 0, [0 for _ in range(k)]
    while i >= 0:
        p[i] += 1
        if p[i] > n: i -= 1
        elif i == k - 1: result.append(p.copy())
        else:
            i += 1
            p[i] = p[i - 1]
    return result

print(combine(4, 3))

