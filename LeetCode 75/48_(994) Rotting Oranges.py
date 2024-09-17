from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        fresh = 0
        start = []
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh +=1
                elif grid[i][j] == 2:
                    q.append((i, j))
        if fresh == 0:
            return 0

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time = 0

        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                for dx, dy in dirs:
                    x, y = i+dx, j+dy
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh -= 1
                        q.append((x, y))
            time += 1

        return time - 1 if fresh == 0 else -1
