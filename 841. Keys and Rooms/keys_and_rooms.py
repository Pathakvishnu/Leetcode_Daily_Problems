from typing import List

class Solution:

    def canVisitAllRoomsDFS(self,rooms):
        visited = [False]*len(rooms)
        stack = [0]
        visited[0] = True

        # dfs approach
        while stack:
            roomNum = stack.pop()
            for neg in rooms[roomNum]:
                if not visited[neg]:
                    visited[neg]=True
                    stack.append(neg)

        return all(visited)

    def canVisitAllRoomsBFS(self, rooms: List[List[int]]) -> bool:
        num_rooms = len(rooms)
        visited = [False]*num_rooms

        # bfs approach
        queue = [0]
        while queue:
            temp = list()
            for room_no in queue:
                if not visited[room_no]:
                    visited[room_no]=True
                    for nxt_room_no in rooms[room_no]:
                        temp.append(nxt_room_no)
                queue = temp

        return all(visited)

rooms = [[2,3],[3,0,1],[2,1],[0]]
obj = Solution()
print(obj.canVisitAllRoomsBFS(rooms))