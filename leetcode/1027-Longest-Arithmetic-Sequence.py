class Solution(object):
    def longestArithSeqLength(self, A):
        size = len(A)
        if size == 2: return 2
        valIndexes, maxCounter = collections.defaultdict(list), 2
        for i, number in enumerate(A):
            valIndexes[number].append(i)
        for i in range(size):
            j = i + 1
            while j < size:
                k = j
                diff, tmpCounter = A[k] - A[i], 2
                while k < size and A[k] + diff in valIndexes and valIndexes[A[k] + diff][-1] > k:
                    tmpCounter += 1
                    maxCounter = max(maxCounter, tmpCounter)
                    k = valIndexes[A[k] + diff][bisect.bisect(valIndexes[A[k] + diff], k)]
                j += 1
        return maxCounter

