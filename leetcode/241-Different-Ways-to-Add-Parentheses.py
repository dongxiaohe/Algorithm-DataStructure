class Solution:
    def diffWaysToCompute(self, input):
        if input.isdigit(): return [int(input)]
        result = []
        for i in range(len(input)):
            if input[i] in "+-*":
                part1 = self.diffWaysToCompute(input[0:i])
                part2 = self.diffWaysToCompute(input[i + 1:])
                for x in part1:
                    for y in part2:
                        if input[i] == "+": result.append(x + y)
                        elif input[i] == "-": result.append(x - y)
                        else: result.append(x * y)
        return result

