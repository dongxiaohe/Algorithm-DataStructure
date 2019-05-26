class TopVotedCandidate(object):
    def __init__(self, persons, times):
        self.times = times
        self.votes = []
        count = collections.defaultdict(int)
        max_count, most_voted = 0, None
        for i, person in enumerate(persons):
            count[person] += 1
            if count[person] >= max_count:
                most_voted = person
                max_count = count[person]
            self.votes.append(most_voted)
    def q(self, t):
        time = bisect.bisect(self.times, t)
        return self.votes[time - 1]
