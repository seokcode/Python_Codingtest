# Keys and Rooms

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = [False]*len(rooms)
        keys[0] = True
        d = [0]
        
        while d:
            desti = d.pop()
            
            for i in rooms[desti]:
                if not keys[i]:
                    keys[i] = True
                    d.append(i)  
            
            if all(keys):
                return True
        
        return False