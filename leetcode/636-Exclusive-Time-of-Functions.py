class Solution(object):
    def exclusiveTime(self, n, logs):
        result = [0 for _ in range(n)]
        prev = None
        stack = []
        for log in logs:
            task, action, curr = log.split(":")
            if action == "start":
                if stack:
                    result[int(stack[-1])] += int(curr) - prev # bug free
                stack.append(int(task))
                prev = int(curr)
            else:
                result[int(task)] += int(curr) - prev + 1 # bug free
                stack.pop()
                prev = int(curr) + 1
        return result
