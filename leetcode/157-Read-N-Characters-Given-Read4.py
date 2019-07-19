class Solution:
    def read(self, buf, n):
        count, eof, tmpBuffer = 0, False, [""] * 4
        while not eof and count < n:
            total = read4(tmpBuffer)

            if total < 4: eof = True

            total = min(total, n - count)
            for i in range(total):
                buf[count] = tmpBuffer[i]
                count += 1
        return count
