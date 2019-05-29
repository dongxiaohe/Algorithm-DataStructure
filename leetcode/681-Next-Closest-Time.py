class Solution(object):
    def nextClosestTime(self, time):
        hours, mins = time.split(":")
        digits = collections.defaultdict(bool)
        for digit in time:
            if digit != ":": digits[digit] = True
        next_time = int(hours) * 60 + int(mins) + 1
        while next_time:
            _hours = str(next_time // 60 % 24)
            if len(_hours) < 2: _hours = "0" + _hours
            _mins = str(next_time % 60)
            if len(_mins) < 2: _mins = "0" + _mins
            if _hours[0] in digits and _hours[1] in digits and _mins[0] in digits and _mins[1] in digits: return "{:s}:{:s}".format(_hours, _mins)
            next_time += 1

