class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        key_list = [0] * len(rooms)

        for i in range(len(rooms)):
            if i != 0: 
                if key_list[i] == 1:
                    for key in rooms[i]:
                        key_list[key] = 1
                else: 
                    return False
            else: 
                for key in rooms[i]:
                        key_list[key] = 1
                        
        return True