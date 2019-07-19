class Solution(object):
      def findRedundantConnection(self, edges):
          parents = collections.defaultdict(int)
          sizes = collections.defaultdict(int)
          def find(node):
              while parents[node] != node:
                  parents[node] = parents[parents[node]]
                  node = parents[node]
              return node
          for u, v in edges:
              if u not in parents:
                  sizes[u] = 1
                  parents[u] = u
              if v not in parents:
                  parents[v] = v
                  sizes[v] = 1
              pu, pv = find(u), find(v)
              if pu == pv: return [u, v]
              if sizes[pv] > sizes[pu]: pv, pu = pu, pv
              parents[pv] = pu
              sizes[pu] += sizes[pv]
          return []

