# coding: utf-8

import collections

class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        room_unlocked = set(list(range(1, len(rooms))))
        queue = collections.deque()
        queue.extend(rooms[0])
        while queue:
            key = queue.popleft()
            if key in room_unlocked:
                room_unlocked.remove(key)
                queue.extend(rooms[key])
        return len(room_unlocked) == 0

if __name__ == "__main__":
    # ipt = [[1], [2], [3], []] 
    ipt = [[1,3],[3,0,1],[2],[0]]
    rtn = Solution().canVisitAllRooms(ipt)
    print(rtn)
