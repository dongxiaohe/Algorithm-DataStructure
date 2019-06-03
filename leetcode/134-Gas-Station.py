class Solution:
    def canCompleteCircuit(self, gas, cost):
        debt, tank, start = 0, 0, 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                debt += tank
                start = i + 1
                tank = 0
        return start if debt + tank >= 0 else -1
