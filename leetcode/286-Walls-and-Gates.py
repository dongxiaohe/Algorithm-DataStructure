class Solution(object):
    def wallsAndGates(self, rooms):
        if not rooms: return
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue = collections.deque()
                    queue.append((i + 1, j, 1)); queue.append((i, j + 1, 1))
                    queue.append((i - 1, j, 1)); queue.append((i, j - 1, 1))
                    visited = set()
                    while queue:
                        x, y, val = queue.popleft()
                        if 0 <= x < m and 0 <= y < n and rooms[x][y] not in [0, -1] and (x, y) not in visited:
                            visited.add((x, y))
                            rooms[x][y] = min(rooms[x][y], val)
                            queue.append((x + 1, y, val + 1)); queue.append((x, y + 1, val + 1))
                            queue.append((x - 1, y, val + 1)); queue.append((x, y - 1, val + 1))

