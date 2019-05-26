class MyCalendarTwo(object):

    def __init__(self):
        self.meetings = []
        self.overlaps= []

    def book(self, start, end):
        for a, b in self.overlaps:
            if b > start and end > a: return False
        for a, b in self.meetings:
            if b > start and end > a:
                self.overlaps.append([max(a, start), min(b, end)])
        self.meetings.append([start, end])
        return True

