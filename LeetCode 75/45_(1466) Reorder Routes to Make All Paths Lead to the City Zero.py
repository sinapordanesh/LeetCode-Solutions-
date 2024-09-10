class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        # self.connection = connections
        self.edges = { (a, b) for a, b in connections}
        self.neighbors = { city:[] for city in range(n)}
        self.visit = set()
        self.change = 0

        for a, b in connections:
            self.neighbors[a].append(b)
            self.neighbors[b].append(a)

        def dfs(city):
            for neighbor in self.neighbors[city]:
                if neighbor in self.visit: 
                    continue
                if (neighbor, city) not in self.edges:
                    self.change += 1
                
                self.visit.add(neighbor)
                dfs(neighbor)
        
        self.visit.add(0)
        dfs(0)
        return self.change