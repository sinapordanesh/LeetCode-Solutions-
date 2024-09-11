from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        self.adj = defaultdict(list)

        for i, edg in enumerate(equations):
            a, b = edg
            self.adj[a].append([b, values[i]])
            self.adj[b].append([a, 1/values[i]])

        def bfs(src, dest):
            if src not in self.adj or dest not in self.adj:
                return -1 

            q, visit = deque(), set()
            q.append([src, 1])
            visit.add(src)

            while q: 
                n, w = q.popleft()
                if n == dest:
                    return w
                
                for nei, weight in self.adj[n]:
                    if nei not in visit:
                        q.append([nei, w * weight])
                        visit.add(nei)
            
            return -1

        return [bfs(q[0], q[1]) for q in queries]

