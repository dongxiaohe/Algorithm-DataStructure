class Solution:
    def myAtoi(self, str):
        acc = ''
        for s in str:
            if ((s == '+' or s == '-') and acc == '') or s.isdigit():
                acc += s
            elif not s.isdigit() and s != ' ' and acc == '':
                return 0 
            elif not s.isdigit() and acc != '':
                break
        if acc == '' or acc == '-' or acc == '+':
            return 0
        result = int(acc)
        if result > (1 << 31) - 1:
            return (1 << 31) - 1
        elif result < -1 << 31:
            return -1 << 31
        return result 

print(Solution().myAtoi('   -45'))
print(Solution().myAtoi('4193 with words'))
print(Solution().myAtoi('words and 300'))
print(Solution().myAtoi('-91283472332'))
