class Solution(object):
    def isNStraightHand(self, hand, W):
        if len(hand) % W != 0: return False
        kv = collections.defaultdict(int)
        for each in hand: kv[each] += 1
        time = len(hand) // W # another solution is to use sort. It should be relatively quicker in some scenario coz of cpu misprediction.
        for _ in range(time):
            v = min(kv)
            for j in range(W):
                if kv[v + j] == 0: return False
                kv[v + j] -= 1
                if kv[v + j] == 0: del kv[v + j]
        return True
