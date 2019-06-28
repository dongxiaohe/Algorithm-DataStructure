def compare(n): 
    def add(a, b):
        tmp = 0
        for i in range(1, 5000):
            tmp += i
        return a + b
    def recordTime(func):
        import time
        start_time = time.time()
        func(n)
        print(" ---- %s seconds ----" % (time.time() - start_time))

    def sumByReduce(n):
        import functools
        result = functools.reduce(add, n)
        print(result)
        return result

    def sumByDivideConquer(n):
        interval = 1
        length = len(n) 
        while interval < length:
            for i in range(0, length - interval, interval * 2):
                n[i] = add(n[i], n[i + interval])
            interval *= 2
        return n[0]

    recordTime(sumByReduce)
    recordTime(sumByDivideConquer)
print(compare(list(range(50000))))
