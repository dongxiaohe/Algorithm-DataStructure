class Solution(object):
    def getHint(self, secret, guess):
        number = collections.defaultdict(int)
        bulls = cows = 0
        for i in range(len(secret)):
            a, b = secret[i], guess[i]
            if secret[i] == guess[i]: bulls += 1
            else:
                if number[a] < 0: cows += 1
                if number[b] > 0: cows += 1
                number[a] += 1
                number[b] -= 1
        return str(bulls) + 'A' + str(cows) + 'B'


