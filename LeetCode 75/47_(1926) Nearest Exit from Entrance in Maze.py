from collections import defaultdict
class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        self.edges = defaultdict(list)

        self.rs, self.re = 0, len(maze)
        self.cs, self.ce = 0, len(maze[0])

        for i, row in enumerate(maze):
            for j, column in enumerate(row):
                if maze[i][j] == '.':
                    if i > 0 and maze[i-1][j] == '.':
                       self.edges[(i, j)].append([i-1, j])

                    if i < self.re - 1 and maze[i+1][j] == '.':
                        self.edges[(i, j)].append([i+1, j])

                    if j > 0 and maze[i][j-1] == '.':
                        self.edges[(i, j)].append([i, j-1])

                    if j < self.ce - 1 and maze[i][j+1] == '.':
                        self.edges[(i, j)].append([i, j+1])

        self.visit = set()
        self.paths = []

        def bfs(cell, path):
            path += 1
            self.visit.add(tuple(cell))
            if (cell[0] == self.rs or cell[0] == self.re) or (cell[1] == self.cs or cell[1] == self.ce):
                        self.paths.append(path)
                        return
            else:
                for neighbor in self.edges[tuple(cell)]:
                    if tuple(neighbor) not in self.visit:  
                        bfs(neighbor, path)
            self.paths.append(-1)
            return

        bfs(entrance, 0)
        return min(self.paths)
