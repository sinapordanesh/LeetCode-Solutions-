class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        
        def visiting(room):
            visited.add(room)
            for i in rooms[room]:
                if i not in visited:
                    visiting(i)

        visiting(0)
        return len(visited) == len(rooms)