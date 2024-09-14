class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        start = []
        
        if not any(1 in row for row in grid):
            return 0

        for i in range(m):
            if 2 in grid[i]:
                for j in range(n):
                    if grid[i][j] == 2: start.append((i, j, 0))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = collections.deque(start)
        
        time = 0
        while q:
            i, j, curr = q.popleft()
            exe = False
            for dx, dy in dirs:
                x, y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    exe = True
                    grid[x][y] = 2
                    q.append((x, y, curr+1))
            if time < curr:
                time += 1

        if any(1 in row for row in grid):
            return -1
        else: 
            return time
        
