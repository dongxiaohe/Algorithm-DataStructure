class Solution:
    def findItinerary(self, tickets):
        kv = collections.defaultdict(list) 
        for a, b in sorted(tickets)[::-1]:
            kv[a].append(b)
        route = []
        def visit(a, kv):
            while kv[a]:
                visit(kv[a].pop(), kv)
            route.append(a)
        visit("JFK", kv)
        return route[::-1]

