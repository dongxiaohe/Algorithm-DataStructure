class Solution:
      def distanceK(self, root, target, K):
        """
        DFS to build map
        BFS to find based on K
        """
        from collections import defaultdict
        conn = defaultdict(list)

        def _connect(parent, child):
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            if child.left: _connect(child, child.left)
            if child.right: _connect(child, child.right)

        _connect(None, root)
        bfs = [target.val]
        seen = set(bfs) 
        for _ in range(K):
            bfs = [y for x in bfs for y in conn[x] if y not in seen]
            seen.update(bfs)
        return bfs
