class Solution(object):
    def licenseKeyFormatting(self, S, K):
        deque = collections.deque()
        str_arr, cur_str = S.split('-'), ""
        for i in range(len(str_arr) - 1, -1, -1):
            cur_str = str_arr[i] + cur_str
            size = len(cur_str)
            while size >= K:
                deque.appendleft(cur_str[size - K:].upper())
                cur_str = cur_str[:size - K]
                size = len(cur_str)
            if i == 0 and cur_str:
                deque.appendleft(cur_str.upper())
        return "-".join(deque)

