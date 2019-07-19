class DSU():
    def __init__(self):
        self.parent = range(10001)
    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    def union(self, node1, node2):
        self.parent[self.find(node1)] = self.find(node2)

class Solution(object):
    def accountsMerge(self, accounts):
        dsu = DSU()
        email_to_id, email_to_name = {}, {}
        for i, emails in enumerate(accounts):
            name = emails[0]
            for email in emails[1:]:
                email_to_name[email] = name
                if email not in email_to_id:
                    email_to_id[email] = i
                dsu.union(email_to_id[emails[1]], email_to_id[email])
        result = collections.defaultdict(list)
        for email in email_to_name:
            result[dsu.find(email_to_id[email])].append(email)

        return [[email_to_name[v[0]]] + sorted(v) for v in result.values()]
