"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

Leetcode Problem 91 https://leetcode.com/problems/decode-ways/

1 -> a
11 -> aa, k
111 -> aaa, ak, ka
1111 -> aaaa, kk, aka, aak, kaa

This is a dp problem. dp[n] = dp[n - 1] (if dp[n] > 0) + dp[n - 2] ( 10 <= if dp[n - 1]dp[n] <= 26 )
"""
def numDecodings(s):
    prev, cur, p = 0, 1 if s[0] != "0" else 0, ""
    for t in s:
        prev, cur, p = cur, prev * (10 <= int(p + t) <= 26) + cur * (t != "0"), t
    return cur

print(numDecodings("1111"))
